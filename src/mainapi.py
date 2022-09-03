import os
from version import __version__
from ttutils.TTConfigHandler import confighandler

conf_dir = os.environ.get("CONF_DATA", "../conf")
conf_filename = os.path.join(conf_dir, 'app-conf.yml')
confighandler.load_config(conf_filename)
confighandler.update_config("SERVICE_VERSION",  __version__)
import yaml
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

# from api.core import config
from api.core import base
from ttutils.apis_static_codes import router as api_static_router
from ttutils.apis_static_codes import API_DOCS_URLS

from ssr_user import router as ssr_user
from jwt_token import router as jwt_token
from alembic import script
from alembic import config as alembic_congig
from alembic.runtime import migration
from api.dbutils.database import engine
from ttutils.CustomHeadersMiddleware import CustomHeadersMiddleware
from ttutils.TTLogging import tt_logger, console_log_filter, log_file_filter
import uvicorn

from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

# This method checks database version with database model
def check_current_head(alembic_cfg, connectable):
    directory = script.ScriptDirectory.from_config(alembic_cfg)
    with connectable.begin() as connection:
        context = migration.MigrationContext.configure(connection)
        tt_logger.info(f"{context.get_current_revision()}, {directory.get_current_head()}")
        return context.get_current_revision() == directory.get_current_head()

cfg = alembic_congig.Config("alembic.ini")
do_check_database_version = True

console_log_filter.level, log_file_filter.level = confighandler.get_config("CONSOLE_LOG_LEVEL", "DEBUG"), confighandler.get_config("FILE_LOG_LEVEL", "DEBUG")


app = FastAPI(docs_url=API_DOCS_URLS.docs_url, redoc_url=API_DOCS_URLS.redoc_url)

@app.on_event("startup")
async def startup():    
    if do_check_database_version and not check_current_head(cfg, engine):
        tt_logger.info("exit because database current version does not match model version")       

app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
app.add_middleware(CustomHeadersMiddleware)

# base_mdl = base.BASE()
# base_mdl.initialization()

tt_logger.info(f"{confighandler.get_config('SERVICE_NAME')} version: {confighandler.get_config('SERVICE_VERSION')} api started")

app.include_router(api_static_router)
app.include_router(ssr_user)
app.include_router(jwt_token)

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"details": exc.message}
    )

#TODO: activate this section after resolving the following Error in production:
# PermissionError: [Errno 13] Permission denied: 'swagger_docs.yml'
# with open('swagger_docs.yml', 'w') as outfile:
#     yaml.dump(app.openapi(), outfile, default_flow_style=False)

if __name__ == "__main__":
    uvicorn.run(app, host=confighandler.get_config('SERVER_LISTEN_IP', '0.0.0.0'),
                port=confighandler.get_config('SERVER_LISTEN_PORT', "8000"))
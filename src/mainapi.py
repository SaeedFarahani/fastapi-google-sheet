import os

from ttutils.TTConfigHandler import confighandler

from version import __version__

conf_dir = os.environ.get("CONF_DATA", "../conf")
conf_filename = os.path.join(conf_dir, 'app-conf.yml')
confighandler.load_config(conf_filename)
confighandler.update_config("SERVICE_VERSION",  __version__)
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from ttutils.apis_static_codes import router as api_static_router
from ttutils.apis_static_codes import API_DOCS_URLS

from contract_api import router as contract_router
from ttutils.CustomHeadersMiddleware import CustomHeadersMiddleware
from ttutils.TTLogging import tt_logger, console_log_filter, log_file_filter
import uvicorn

console_log_filter.level, log_file_filter.level = confighandler.get_config("CONSOLE_LOG_LEVEL", "DEBUG"), confighandler.get_config("FILE_LOG_LEVEL", "DEBUG")


app = FastAPI(docs_url=API_DOCS_URLS.docs_url, redoc_url=API_DOCS_URLS.redoc_url)

@app.on_event("startup")
async def startup():    
    pass

app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
app.add_middleware(CustomHeadersMiddleware)

# base_mdl = base.BASE()
# base_mdl.initialization()

tt_logger.info(f"{confighandler.get_config('SERVICE_NAME')} version: {confighandler.get_config('SERVICE_VERSION')} api started")

app.include_router(api_static_router)
app.include_router(contract_router)


if __name__ == "__main__":
    uvicorn.run(app, host=confighandler.get_config('SERVER_LISTEN_IP', '0.0.0.0'),
                port=confighandler.get_config('SERVER_LISTEN_PORT', 8000))
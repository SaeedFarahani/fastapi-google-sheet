import os
from version import __version__
from ttutils.TTConfigHandler import confighandler

confighandler.load_config(os.environ.get("CONF_DATA", "../conf/app-conf.yml"))


from fastapi import FastAPI

from ttutils.apis_static_codes import router as api_static_router
from ttutils.apis_static_codes import API_DOCS_URLS

from ttutils.CustomHeadersMiddleware import CustomHeadersMiddleware
from ttutils.TTLogging import tt_logger, console_log_filter, log_file_filter
import uvicorn

print(confighandler.configs)
console_log_filter.level, log_file_filter.level = confighandler.configs['CONSOLE_LOG_LEVEL'], confighandler.configs['FILE_LOG_LEVEL']

x = confighandler.get_config("SERVICE_VERSION")
tt_logger.info(x)
x = confighandler.get_config("SERVICE_VERSION", 1000)
tt_logger.info(x)
confighandler.configs["SERVICE_VERSION"] = __version__
x = confighandler.get_config("SERVICE_VERSION", 1000)
tt_logger.info(x)
x = confighandler.get_config("abc", 1000)
tt_logger.info(x)
print(API_DOCS_URLS.docs_url, API_DOCS_URLS.redoc_url)
app = FastAPI(docs_url=API_DOCS_URLS.docs_url, redoc_url=API_DOCS_URLS.redoc_url)

app.add_middleware(CustomHeadersMiddleware)

tt_logger.info(f"{confighandler.configs['SERVICE_NAME']} version: {confighandler.configs['SERVICE_VERSION']} api started")

app.include_router(api_static_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",
                port=8000)
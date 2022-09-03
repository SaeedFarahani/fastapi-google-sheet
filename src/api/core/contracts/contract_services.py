import os
from multiprocessing import Manager
from threading import Lock
from api.core.googlesheet import read_data_google_api
from api.viewmodels.api_response import ContractResponse
from ttutils.TTLogging import tt_logger

manager = Manager()
emb_all = manager.dict()
write_database_lock = Lock()


async def download_contracts(sheet_url: str, sheet_name: str) -> ContractResponse:
    response = ContractResponse()
    try:
        await read_data_google_api.read_data_sheet_using_google_api(sheet_url, sheet_name)
        return response.set_ok()
    except Exception as ex:
        tt_logger.error(f"error in download_contracts service {ex}")
        return response.set_error_download_sheet()

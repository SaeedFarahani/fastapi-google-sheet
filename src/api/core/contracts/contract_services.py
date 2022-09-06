import os
from multiprocessing import Manager
from threading import Lock

from api.core.googlesheet import read_data_google_api
from api.core.googlesheet.read_data_export_csv import read_data_from_csv_sheet_to_panda
from api.dbutils.redis.redis import get_all_contracts
from api.viewmodels.api_response import ContractResponse
from api.core.contracts.proccess_contracts import ProcessContract
from ttutils.TTLogging import tt_logger

manager = Manager()
emb_all = manager.dict()
write_database_lock = Lock()


async def download_contracts(sheet_url: str, sheet_name: str) -> ContractResponse:
    response = ContractResponse()
    try:
        df = read_data_google_api.read_data_sheet_using_google_api(sheet_url, sheet_name)
        await ProcessContract.process_validate_parse_data_from_data_frame(df)
        return response.set_ok()
    except Exception as ex:
        tt_logger.error(f"error in download_contracts service {ex}")
        return response.set_error_download_sheet()


async def download_contracts_csv(sheet_url: str) -> ContractResponse:
    response = ContractResponse()
    try:
        df = read_data_from_csv_sheet_to_panda(sheet_url)
        await ProcessContract.process_validate_parse_data_from_data_frame(df)
        return response.set_ok()
    except Exception as ex:
        tt_logger.error(f"error in download_contracts service {ex}")
        return response.set_error_download_sheet()


def get_contracts() -> ContractResponse:
    response = ContractResponse()
    try:
        contracts = get_all_contracts()
        return response.set_data(contracts).set_ok()
    except Exception as ex:
        tt_logger.error(f"error in get_contracts service {ex}")
        return response.set_data([]).set_error()

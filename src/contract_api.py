from ttutils.CustomHeadersMiddleware import get_request_id

from api.core.contracts import contract_services
from api.viewmodels.api_response import ContractResponse
from fastapi import APIRouter, File, UploadFile
from ttutils.TTConfigHandler import confighandler
from ttutils.TTLogging import tt_logger
from api.core import base
from api.viewmodels import vm_contract

# from api.core import config

SERVICE_NAME = confighandler.get_config('SERVICE_NAME', 'CONTRACTS')

router = APIRouter()


#####################################################################################################
#    Contract Api
#####################################################################################################

@router.post(f"/{SERVICE_NAME}/api/v1/download-contracts-csv-mode", response_model=vm_contract.ResponseBase,
             tags=["CONTRACTS"])
async def download_contract_csv(sheet: vm_contract.SheetURL):
    request_id = get_request_id()
    response = ContractResponse()
    try:
        tt_logger.info(f"download_contract sheet name as csv file")
        response = await contract_services.download_contracts_csv(sheet.sheet_url)
        response.log()
        return response

    except Exception as ex:
        tt_logger.error(f"Error in download-contracts api request id is {request_id} error is {ex}")
        return response.set_error()


@router.post(f"/{SERVICE_NAME}/api/v1/download-contracts", response_model=vm_contract.ResponseBase, tags=["CONTRACTS"])
async def download_contract(sheet: vm_contract.SheetName):
    request_id = get_request_id()
    response = ContractResponse()
    try:
        tt_logger.info(f"download_contract sheet name {sheet.sheet_name}")
        response = await contract_services.download_contracts_csv(sheet.sheet_url, sheet.sheet_name)
        response.log()
        return response

    except Exception as ex:
        tt_logger.error(f"Error in download-contracts api request id is {request_id} error is {ex}")
        return response.set_error()


@router.get(f"/{SERVICE_NAME}/api/v1/get-contracts", response_model=vm_contract.Contracts, tags=["CONTRACTS"])
async def get_contract():
    request_id = get_request_id()
    response = ContractResponse()
    try:
        tt_logger.info(f"get_contract")
        response = contract_services.get_contracts()
        response.log()
        return response

    except Exception as ex:
        tt_logger.error(f"Error in download-contracts api request id is {request_id} error is {ex}")
        return response.set_data([]).set_error()

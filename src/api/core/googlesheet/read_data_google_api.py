from typing import List
import pickle
import aiohttp
import cv2
import gspread as gs
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from api.dbutils.models.contract import Contract
from ttutils.TTLogging import tt_logger
from api.core import config
from api.dbutils.redis import redis

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../../conf/gs_credentials.json', scope)
gc = gs.authorize(credentials)


def add_to_cache_database(contract: Contract):
    key = contract.firstname + contract.lastname + contract.zip
    redis.set_data_to_cache(key, pickle.dumps(contract))


async def check_images(contracts: List[Contract]):
    for contract in contracts:
        try:
            async with aiohttp.ClientSession() as session:
                url = contract.image
                async with session.get(url) as resp:
                    if resp.status == 200:
                        image_file = await resp.read()
                        image = cv2.imdecode(np.fromfile(image_file, np.uint8), cv2.IMREAD_COLOR)
                        if config.IMAGE_MIN_WIDTH <= image.shape[0] <= config.IMAGE_MAX_WIDTH \
                                and config.IMAGE_MIN_HEIGHT <= image.shape[1] <= config.IMAGE_MAX_HEIGHT:
                            add_to_cache_database(contract)
        except:
            tt_logger.exception(f"image file in this url{contract.image} is not valid")


async def validate_parse_data(df: pd.DataFrame):
    columns = ['firstname', 'lastname', 'street', 'zip', 'city', 'image']
    if not pd.Series(columns).isin(df.columns).all():
        raise Exception('column names are not valid')
    contracts = []
    for index, row in df.iterrows():
        try:
            contracts.append(Contract(row.firstname, row.lastname, row.street, row.zip, row.city, row.image))
        except:
            tt_logger.exception(f"data is not valid in this row{row}")
    tt_logger.info(f"{len(contracts)} contract info fetched from sheet")


async def read_data_sheet_using_google_api(sheet_url: str, sheet_name: str):
    sh = gc.open_by_url(sheet_url)
    ws = sh.worksheet(sheet_name)
    df = pd.DataFrame(ws.get_all_records())
    validate_parse_data(df)


read_data_sheet_using_google_api(
    'https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pubhtml?gid=0&amp;single=true',
    'Sheet1')

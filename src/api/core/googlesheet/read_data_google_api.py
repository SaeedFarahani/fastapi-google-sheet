import os
from typing import List
import pickle
import aiohttp
import gspread as gs
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from api.dbutils.models.contract import Contract
from ttutils.TTLogging import tt_logger
from api.core import config
from api.dbutils.redis import redis
from PIL import ImageFile
from api.dbutils.redis.redis import add_contract_to_cache_database

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
conf_dir = os.environ.get("CONF_DATA", "../conf")
credentials_path = os.path.join(conf_dir, 'gs_credentials.json')

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
gc = gs.authorize(credentials)



async def check_images(contract: Contract):
    try:
        async with aiohttp.ClientSession() as session:
            url = contract.image
            async with session.get(url) as resp:
                if resp.status == 200:
                    image_file = await resp.read()
                    p = ImageFile.Parser()
                    p.feed(image_file)
                    if p.image:
                        if config.IMAGE_MIN_WIDTH <= p.image.size[0] <= config.IMAGE_MAX_WIDTH \
                                and config.IMAGE_MIN_HEIGHT <= p.image.size[1] <= config.IMAGE_MAX_HEIGHT:
                            add_contract_to_cache_database(contract)
    except Exception:
        tt_logger.error(f"image file in this url{contract.image} is not valid")


async def validate_parse_data(df: pd.DataFrame):
    columns = ['firstname', 'lastname', 'street', 'zip', 'city', 'image']
    if not pd.Series(columns).isin(df.columns).all():
        raise Exception('column names are not valid')
    count = 0
    for index, row in df.iterrows():
        try:
            contracts = Contract(row.firstname, row.lastname, row.street, row.zip, row.city, row.image)
            await check_images(contracts)
            count += 1
        except:
            tt_logger.error(f"data is not valid in this row{row}")
    tt_logger.info(f"{count} contract info fetched from sheet")


async def read_data_sheet_using_google_api(sheet_url: str, sheet_name: str):
    try:
        sh = gc.open_by_url(sheet_url)
        ws = sh.worksheet(sheet_name)
        df = pd.DataFrame(ws.get_all_records())
        await validate_parse_data(df)
    except Exception as ex:
        tt_logger.error(f"url of sheet is not valid {sheet_url} exception is {ex}")
        raise Exception(f"url of sheet is not valid {sheet_url}")
#
# read_data_sheet_using_google_api(
#     'https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pubhtml?gid=0&amp;single=true',
#     'Sheet1')

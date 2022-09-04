from typing import List
import pickle
import aiohttp

from api.dbutils.models.contract import Contract

from ttutils.TTLogging import tt_logger
from api.core import config
from api.dbutils.redis import redis
from PIL import ImageFile
import pandas as pd
import numpy as np
from api.dbutils.redis.redis import add_contract_to_cache_database


class ProcessContract:

    @staticmethod
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

    @staticmethod
    async def process_validate_parse_data_from_data_frame(df: pd.DataFrame):
        columns = ['firstname', 'lastname', 'street', 'zip', 'city', 'image']
        if not pd.Series(columns).isin(df.columns).all():
            raise Exception('column names are not valid')
        count = 0
        for index, row in df.iterrows():
            try:
                contracts = Contract(row.firstname, row.lastname, row.street, row.zip, row.city, row.image)
                await ProcessContract.check_images(contracts)
                count += 1
            except:
                tt_logger.error(f"data is not valid in this row{row}")
        tt_logger.info(f"{count} contract info fetched from sheet")

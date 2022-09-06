import pandas as pd
import re
from ttutils.TTLogging import tt_logger


def read_data_from_csv_sheet_to_panda(sheet_url) -> pd.DataFrame:
    try:
        sheet_url = re.sub(r'([^\/]+[#|?])', 'export?format=csv&', sheet_url)
        df = pd.read_csv(sheet_url)
        return df
    except Exception as ex:
        tt_logger.error(f"url of sheet is not valid {sheet_url} exception is {ex}")
        raise Exception(f"url of sheet is not valid {sheet_url}")

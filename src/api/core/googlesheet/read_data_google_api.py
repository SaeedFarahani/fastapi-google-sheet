import os

import gspread as gs
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from ttutils.TTLogging import tt_logger

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
conf_dir = os.environ.get("CONF_DATA", "../conf")

credentials_path = os.path.join(conf_dir, 'gs_credentials.json')

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
gc = gs.authorize(credentials)


def read_data_sheet_using_google_api(sheet_url: str, sheet_name: str):
    try:
        sh = gc.open_by_url(sheet_url)
        ws = sh.worksheet(sheet_name)
        df = pd.DataFrame(ws.get_all_records())
        return df
    except Exception as ex:
        tt_logger.error(f"url of sheet is not valid {sheet_url} exception is {ex}")
        raise Exception(f"url of sheet is not valid {sheet_url}")

import pandas as pd
import re

sheet_url_main = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pub?gid=0&amp;single=true&amp;output=csv"


def read_data_from_csv_sheet_to_panda(sheet_url) -> pd.DataFrame:
    sheet_url = re.sub(r'([^\/]+[#|?])', 'export?format=csv&', sheet_url)
    df = pd.read_csv(sheet_url)
    print(df.head())
    return df


read_data_from_csv_sheet_to_panda(sheet_url_main)

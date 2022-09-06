import pandas as pd
import os
import sys


def test_read_data_as_csv_file():
    from api.core.googlesheet.read_data_export_csv import read_data_from_csv_sheet_to_panda
    sheet_url = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pub?gid=0&amp;single=true&amp;output=csv"
    pd_sheet = read_data_from_csv_sheet_to_panda(sheet_url)
    pd_file = pd.read_csv('tests/sample_data/sheed_data.csv')
    c_result = pd_file[pd_sheet.apply(tuple, 1).isin(pd_file.apply(tuple, 1))]
    print(c_result)
    assert c_result.shape == (4, 6)


def test_read_data_using_google_api():
    from api.core.googlesheet import read_data_google_api
    sheet_url = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pubhtml?gid=0&amp;single=true"
    sheet_name = "Sheet1"
    pd_sheet = read_data_google_api.read_data_sheet_using_google_api(sheet_url, sheet_name)
    pd_file = pd.read_csv('tests/sample_data/sheed_data.csv')
    c_result = pd_file[pd_sheet.apply(tuple, 1).isin(pd_file.apply(tuple, 1))]
    print(c_result)
    assert c_result.shape == (3, 6)

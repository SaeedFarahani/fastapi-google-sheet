import gspread as gs
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import requests


scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../../conf/gs_credentials.json', scope)
gc = gs.authorize(credentials)

# gc = gs.service_account(filename='../../../../conf/gs_credentials.json')

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pubhtml?gid=0&amp;single=true')
ws = sh.worksheet('Sheet1')
df = pd.DataFrame(ws.get_all_records())
print(df.head())

revisions_uri = f'https://www.googleapis.com/drive/v3/files/{sh.id}/revisions'
headers = {'Authorization': f'Bearer {credentials.get_access_token().access_token}'}
response = requests.get(revisions_uri, headers=headers).json()
print(response)

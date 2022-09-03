import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/export?format=csv&gid=0&amp&single=true&amp;output=csv"



df = pd.read_csv(sheet_url)
print(df.head())
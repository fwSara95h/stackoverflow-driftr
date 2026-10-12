# Code from my Stack Overflow answer https://stackoverflow.com/a/74910313 (posted 2022-12-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import pandas as pd
sheetId = '1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo' ## REPLACE WITH YOUR SHEETID
sheetUrl = f'https://docs.google.com/spreadsheets/d/{sheetId}'
sheetDF = pd.read_html(
    sheetUrl, attrs={'class': 'waffle'}, skiprows=1
)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')

# --- block 2 ---
import pandas as pd
import requests
from bs4 import BeautifulSoup

sheetUrl = 'YOUR_SHEET_URL'
cookies = 'PASTE_FROM_https://curlconverter.com/'
headers = 'PASTE_FROM_https://curlconverter.com/' 
req = requests.get(sheetUrl, cookies=cookies, headers=headers)

# in one line, no error-handling
# sheetDF = pd.read_html(req.text, attrs={'class': 'waffle'}, skiprows=1)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')

# req.raise_for_status() # raise error if request fails
if req.status_code != 200: 
    print(req.status_code, req.reason, '- failed to get', url)

soup = BeautifulSoup(req.content)
wTable = soup.find('table', class_="waffle")
if wTable is not None:
    dfList = pd.read_html(str(wTable), skiprows=1) # set skiprows=1 to skip top row with column names A, B, C...
    sheetDF = dfList[0] # because read_html returns a LIST of dataframes
    sheetDF = sheetDF.drop(['1'], axis='columns') # drop row #s 1,2,3...
    sheetDF = sheetDF.dropna(axis='rows', how='all') # drop empty rows
    sheetDF = sheetDF.dropna(axis='columns', how='all') # drop empty columns
    ### WHATEVER ELSE YOU WANT TO DO WITH DATAFRAME ###
else: print('COULD NOT FIND TABLE')

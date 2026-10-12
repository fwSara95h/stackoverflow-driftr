# Code from my Stack Overflow answer https://stackoverflow.com/a/74789229 (posted 2022-12-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
table = soup.find('table', {'data-test': "pre-market-most-active-stocks-table"})

# --- block 2 ---
# import pandas
print(pandas.read_html(table.prettify())[0].to_markdown(index=False))

# --- block 3 ---
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.investing.com/equities/pre-market"
resp = requests.get(url)
# resp.raise_for_status() # halt program right here if bad response

soup = BeautifulSoup(resp.content)
table = soup.find('table', {'data-test':"pre-market-most-active-stocks-table"})

if table is None and resp.status_code == 200: # ok respose, but no table
    hfn = 'MISSING_DATA investing-com_equities_premarket.html'
    with open(hfn, 'wb') as f: f.write(resp.content) 
    print('no such table found - inspect [on editor]: ', os.path.abspath(hfn))
elif table: print(pd.read_html(table.prettify())[0].to_markdown(index=False))
else: print(f'{resp.status_code} {resp.reason} - failed to scrape {url}')

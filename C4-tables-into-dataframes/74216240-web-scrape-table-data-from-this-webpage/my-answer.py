# Code from my Stack Overflow answer https://stackoverflow.com/a/74217598 (posted 2022-10-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import json

### copied from your q ####
import requests
from bs4 import BeautifulSoup

URL = "https://www.lochinvar.com/products/commercial-water-heaters/armor-condensing-water-heater"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
###########################

wrInf = soup.find(lambda l: l.name == 'script' and '__routeInfo' in l.text)
wrInf = wrInf.text.replace('window.__routeInfo = ', '', 1) # remove variable name
wrInf = wrInf.strip()[:-1] # get rid of ; at end
wrInf = json.loads(wrInf) # convert to python dictionary

specsTables = wrInf['data']['product']['specifications'][0]['table'] # get table (tsv string)
specsTables = [tuple(row.split('\t')) for row in specsTables.split('\n')] # convert rows to tuples

# --- block 2 ---
import pandas

headers = specsTables[0]
st_df = pandas.DataFrame([dict(zip(headers, r)) for r in specsTables[1:]])
# or just
# st_df = pandas.DataFrame(specsTables[1:], columns=headers)

print(st_df.head())

# --- block 3 ---
for i, r in enumerate(specsTables):
  print(" | ".join([f'{c:^18}' for c in r]))
  if i == 0: print()

# --- block 4 ---
modelNo = 'AWH1000NPM'

mSpecs = [r for r in specsTables if r[0] == modelNo]
mSpecs = [[]] if mSpecs == [] else mSpecs # in case there is no match
mSpecs = dict(zip(specsTables[0], mSpecs[0])) # convert to dictionary

print(mSpecs)

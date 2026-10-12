# Code from my Stack Overflow answer https://stackoverflow.com/a/74357110 (posted 2022-11-08), extracted verbatim; may need the question's context to run.
import requests
import urllib.parse
from bs4 import BeautifulSoup

sa_key = 'YOUR_API_TOKEN' # paste here
sa_api = 'https://api.scrapingant.com/v2/general'
qParams = {'url': 'https://coinsniper.net/new', 'x-api-key': sa_key}
reqUrl = f'{sa_api}?{urllib.parse.urlencode(qParams)}'  

r = requests.get(reqUrl)
# print(r.text) # --> html
soup = BeautifulSoup(r.content, 'html.parser')

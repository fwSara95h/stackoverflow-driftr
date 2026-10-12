# Code from my Stack Overflow answer https://stackoverflow.com/a/74838470 (posted 2022-12-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import json
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.immoweb.be/en/search/apartment/for-sale/Antwerp/2000?countries=BE&page=1&orderBy=relevance&card=10286959"
page = requests.get(URL)
page.raise_for_status() # raise error if request fails

soup = BeautifulSoup(page.content, "html.parser")

resultsList = json.loads(soup.find('iw-search').get(':results'))
resultIds = [r['id'] for r in resultsList]

# --- block 2 ---
[10083851, 10147541, 9607277, 9614247, 10110818, 10286959, 10067819, 10186552, 10209440, 10135372, 10182817, 7412146, 9309581, 10176146, 10186729, 10157914, 10201488, 10267579, 10267583, 10276232, 10204059, 9802962, 10261577, 10128809, 10250713, 10149009, 10173283, 10285603, 9028052, 10224443]

# --- block 3 ---
# import json

iws_attrs = soup.find('iw-search').attrs
for k, v in iws_attrs.items():
    try: iws_attrs[k] = json.loads(v)
    except: pass

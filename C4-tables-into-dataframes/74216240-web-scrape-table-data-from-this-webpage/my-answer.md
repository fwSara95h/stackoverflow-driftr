---
title: "Web Scrape table data from this webpage"
site: stackoverflow
question_id: 74216240
answer_id: 74217598
url: https://stackoverflow.com/a/74217598
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-27T06:21:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74217598/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ed81808ba7099da877b82f233397b372df0a2a74a07b7aeb4cd091b28c6bd5eb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74217598>, 2022-10-27; **accepted**; score 1. Text as retrieved 2026-10-12.

The page is populated with javascript, but fortunately in this case, much of the data [including the specs table you want] seems to be inside a `script` tag within the fetched html. The script just has one statement, so it's fairly easy to extract it as json

```python
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
```

<hr>

To view it, you could use pandas,
```python
import pandas

headers = specsTables[0]
st_df = pandas.DataFrame([dict(zip(headers, r)) for r in specsTables[1:]])
# or just
# st_df = pandas.DataFrame(specsTables[1:], columns=headers)

print(st_df.head())
```
or you could simply print it
```python
for i, r in enumerate(specsTables):
  print(" | ".join([f'{c:^18}' for c in r]))
  if i == 0: print()
```
output:
```markdown
   Model Number    |    Btu/Hr Input    | Thermal Efficiency | GPH @ 100ÂºF Rise  |         A          |         B          |         C          |         D          |         E          |         F          |         G          |         H          |         I          |         J          |         K          |         L          |         M          |     Gas Conn.      |    Water Conn.     |     Air Inlet      |     Vent Size      |     Ship. Wt.     

    AWH0400NPM     |      399,000       |        99%         |        479         |        45"         |        24"         |      30-1/2"       |      42-1/2"       |      29-3/4"       |      20-1/4"       |        12"         |        20"         |        38"         |       3-1/2"       |      10-1/2"       |      19-1/4"       |        20"         |         1"         |         2"         |         4"         |         4"         |        326        
    AWH0500NPM     |      500,000       |        99%         |        600         |        45"         |        24"         |      30-1/2"       |      42-1/2"       |      29-3/4"       |      20-1/4"       |        12"         |        20"         |        38"         |       3-1/2"       |      10-1/2"       |      19-1/4"       |        20"         |         1"         |         2"         |         4"         |         4"         |        333        
    AWH0650NPM     |      650,000       |        98%         |        772         |        45"         |        24"         |        41"         |        53"         |      30-1/2"       |      15-1/4"       |        12"         |        20"         |        38"         |       3-1/2"       |      10-1/2"       |      19-1/4"       |        20"         |       1-1/4"       |         2"         |         4"         |         6"         |        424        
    AWH0800NPM     |      800,000       |        98%         |        950         |        45"         |        24"         |        41"         |        53"         |      30-1/2"       |      15-1/4"       |        12"         |        20"         |        38"         |       3-1/2"       |      10-1/2"       |      19-1/4"       |        20"         |       1-1/4"       |         2"         |         4"         |         6"         |        434        
    AWH1000NPM     |      999,000       |        98%         |       1,187        |        45"         |        24"         |        48"         |        62"         |      30-1/2"       |      15-3/4"       |        12"         |        20"         |        38"         |       3-1/2"       |      10-1/2"       |      19-1/4"       |        20"         |       1-1/4"       |       2-1/2"       |         6"         |         6"         |        494        
    AWH1250NPM     |     1,250,000      |        98%         |       1,485        |      51-1/2"       |        34"         |        49"         |        59"         |       5-1/2"       |       5-1/2"       |      13-1/2"       |       6-3/4"       |      46-3/4"       |       5-3/4"       |      19-3/4"       |        23"         |      22-1/2"       |       1-1/2"       |       2-1/2"       |         8"         |         8"         |       1,568       
    AWH1500NPM     |     1,500,000      |        98%         |       1,782        |      51-1/2"       |        34"         |      52-3/4"       |      62-3/4"       |       4-1/2"       |       4-1/2"       |      13-1/2"       |       6-3/4"       |      46-3/4"       |       5-3/4"       |      19-3/4"       |        23"         |      22-1/2"       |       1-1/2"       |       2-1/2"       |         8"         |         8"         |       1,649       
    AWH2000NPM     |     1,999,000      |        98%         |       2,375        |      51-1/2"       |        34"         |      65-1/2"       |      75-1/2"       |         7"         |       5-3/4"       |      14-3/4"       |       7-1/4"       |      46-3/4"       |       6-3/4"       |      18-3/4"       |        23"         |      23-1/2"       |       1-1/2"       |       2-1/2"       |         8"         |         8"         |       1,911       
    AWH3000NPM     |     3,000,000      |        98%         |       3,564        |      67-1/4"       |      48-1/4"       |      79-3/4"       |      93-3/4"       |       4-3/4"       |       6-3/4"       |      17-3/4"       |       8-3/4"       |      60-1/4"       |       8-1/2"       |      25-1/2"       |      29-1/2"       |        40"         |         2"         |         4"         |        10"         |        10"         |       3,147       
    AWH4000NPM     |     4,000,000      |        98%         |       4,752        |      67-1/4"       |      48-1/4"       |        96"         |        110"        |         5"         |       7-1/2"       |      17-3/4"       |       8-3/4"       |      60-1/4"       |       8-1/2"       |      25-1/2"       |      29-1/2"       |        40"         |       2-1/2"       |         4"         |        12"         |        12"         |       3,694       
```

<hr>

If you wanted a specific models specs:
```python
modelNo = 'AWH1000NPM'

mSpecs = [r for r in specsTables if r[0] == modelNo]
mSpecs = [[]] if mSpecs == [] else mSpecs # in case there is no match
mSpecs = dict(zip(specsTables[0], mSpecs[0])) # convert to dictionary

print(mSpecs)
```
output:
```markdown
{'Model Number': 'AWH1000NPM', 'Btu/Hr Input': '999,000', 'Thermal Efficiency': '98%', 'GPH @ 100ÂºF Rise': '1,187', 'A': '45"', 'B': '24"', 'C': '48"', 'D': '62"', 'E': '30-1/2"', 'F': '15-3/4"', 'G': '12"', 'H': '20"', 'I': '38"', 'J': '3-1/2"', 'K': '10-1/2"', 'L': '19-1/4"', 'M': '20"', 'Gas Conn.': '1-1/4"', 'Water Conn.': '2-1/2"', 'Air Inlet': '6"', 'Vent Size': '6"', 'Ship. Wt.': '494'}
```

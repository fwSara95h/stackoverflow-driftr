# Code from my Stack Overflow answer https://stackoverflow.com/a/75587185 (posted 2023-02-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
import json
jData = '''
[ { "infos": [{ "localisation": "Kassel" }, { "date": "01.08.2023" }, { "places": "1 freier Platz" }],
    "applying email": "exemple@starke.ma",
    "additional infos": {"name": "jhon", "position": "RH", "email": "email@email.com" }  },
  { "infos": [{ "places": "1 freier Platz" }],
    "applying email": "", "applying link": "www.exemple.com",
    "additional infos": {"name": "jhon", "position": "RH", "email": "email@email.com"} }] 
''' ## I removed the last comma bc it was causing error when parsing

pData = json.loads(jData)

# --- block 2 ---
import pandas as pd
csv_path = 'x.csv' ## path/name of csv file to save to

# pd.DataFrame([flattenObj(d, kSep=' > ') for d in pData]).to_csv(csv_path, index=False)
df = pd.DataFrame([flattenObj(d, kSep=' > ') for d in pData])
df.to_csv(csv_path, index=False)

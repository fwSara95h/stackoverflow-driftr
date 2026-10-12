# Code from my Stack Overflow answer https://stackoverflow.com/a/75929728 (posted 2023-04-04), extracted verbatim; may need the question's context to run.
import pandas as pd
import json

json_fp = 'x.json' ## put the ACTUAL file path here
with open(json_fp) as f: data = json.load(f)

df = pd.json_normalize(data)
df.columns = [c.split('.')[-1] for c in df.columns]

df = df.explode('accountInfo').reset_index(drop=True)
df = pd.concat([df, pd.json_normalize(df['accountInfo'])], axis=1)
df = df.drop(columns=['accountInfo','enquiryInfo','officeInfo'])

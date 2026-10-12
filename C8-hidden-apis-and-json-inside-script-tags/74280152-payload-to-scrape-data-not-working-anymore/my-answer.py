# Code from my Stack Overflow answer https://stackoverflow.com/a/74280997 (posted 2022-11-01), extracted verbatim; may need the question's context to run.
res = requests.post(url, json=payload)
# res.raise_for_status() # just in case

if 'application/json' in res.headers['Content-Type']: 
    data = res.json()
else:
    print('unexpected format')
    break # or however else you want to handle it

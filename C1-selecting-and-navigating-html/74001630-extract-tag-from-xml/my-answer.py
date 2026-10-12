# Code from my Stack Overflow answer https://stackoverflow.com/a/74019286 (posted 2022-10-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
fact_sheet_links = [d['fact_sheet'] for d in Data.json()['data']]

# --- block 2 ---
Data = requests.get(URL, headers={ 'Accept': 'application/xml' })

# --- block 3 ---
tags = Soup.find_all(lambda t: 'fact_sheet' in t.name)

# --- block 4 ---
fact_sheet_links = [t.text for t in tags]

# Code from my Stack Overflow answer https://stackoverflow.com/a/73885525 (posted 2022-09-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
ref = [
    a for a in soup.select('a') if a.text
    and 'Weekly Update' in a.text
]

# --- block 2 ---
ref = soup.find(
    'b', string='Weekly Incremental NPI Files'
).find_next('tr').select('a')

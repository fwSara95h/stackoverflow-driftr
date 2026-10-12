# Code from my Stack Overflow answer https://stackoverflow.com/a/74419291 (posted 2022-11-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
col1 = [
    a.get('href') for a in soup.find_all('a') if a.parent.name == 'td' 
    and a.string == 'info' and not a.parent.find_next_sibling()
]

# --- block 2 ---
col1 = [a.get('href') for a in soup.select('td:last-child a[title="Click for match detail"][href]')]

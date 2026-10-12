# Code from my Stack Overflow answer https://stackoverflow.com/a/74752087 (posted 2022-12-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[a.get('href') for a in crawl.select('*[href*="scp-"]') if 'SCP-' in a.get_text()]

# --- block 2 ---
['/scp-1512', '/scp-2756', '/scp-002', '/scp-004']

# --- block 3 ---
root_url = 'https://PARENT-URL.com' ## replace with the actual parent url

scpLinks = [root_url + l for l, t in list(set([
    (a.get('href'), a.get_text()) for a in crawl.select('*[href*="scp-"]')
])) if 'SCP-' in t]

# --- block 4 ---
['https://PARENT-URL.com/scp-004', 'https://PARENT-URL.com/scp-002', 'https://PARENT-URL.com/scp-1512', 'https://PARENT-URL.com/scp-2756']

# --- block 5 ---
scpLinks = [root_url + l for l, t in list(set([
    (a.get('href'), a.get_text()) for a in crawl.select('*[href*="scp-"]')
])) if 'SCP-' in t and str(param) not in t]

# --- block 6 ---
['https://PARENT-URL.com/scp-004', 'https://PARENT-URL.com/scp-1512', 'https://PARENT-URL.com/scp-2756']

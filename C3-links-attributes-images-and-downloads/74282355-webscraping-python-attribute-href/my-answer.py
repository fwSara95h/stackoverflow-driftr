# Code from my Stack Overflow answer https://stackoverflow.com/a/74283311 (posted 2022-11-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
h4 = site_html.find('h4')
h4.a.get('href')

# --- block 2 ---
[h.a.get('href') for h in site_html.find_all('h4') if h.find('a') and h.a.get('href')]

# --- block 3 ---
[a.get('href') for a in site_html.select('h4 a[href]')]

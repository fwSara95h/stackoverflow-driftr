# Code from my Stack Overflow answer https://stackoverflow.com/a/76553683 (posted 2023-06-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
company_urls = [a['href'] for a in soup.select('a[href*="\/Company\/"]')]

# --- block 2 ---
company_urls = [a['href'] for a in soup.find_all('a', href=lambda h: h and '/Company/' in h)]

# --- block 3 ---
company_urls = [a['href'] for a in soup.find_all('a', href=True) if '/Company/' in a['href']]

# --- block 4 ---
company_urls = [a['href'] for a in soup.select('a[href]') if '/Company/' in a['href'])]

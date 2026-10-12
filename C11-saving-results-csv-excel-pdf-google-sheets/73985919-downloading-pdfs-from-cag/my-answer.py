# Code from my Stack Overflow answer https://stackoverflow.com/a/73986919 (posted 2022-10-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tabId = soup.find(
    lambda t: t.name == 'a' and t.get('href') and 
    t.get('href').startswith('#tab') and # just in case
    'Monthly Key Indicators' == t.get_text(strip=True)
).get('href')

# --- block 2 ---
soup.select(f"{tabId} a[href$='.pdf']")

# --- block 3 ---
pdfLinks = soup.select(f"{tabId} a[href$='.pdf']")
pdfLinks = [pl for pl in pdfLinks if pl.get_text(strip=True) == 'Download']
for link in pdfLinks:
  #download

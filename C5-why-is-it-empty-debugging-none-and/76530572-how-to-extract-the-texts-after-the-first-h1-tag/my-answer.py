# Code from my Stack Overflow answer https://stackoverflow.com/a/76532726 (posted 2023-06-22), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# list_of_urls = ['https://economictimes.indiatimes.com/...
# for url in list_of_urls:
    # response = requests.get(url,.....
    # soup = BeautifulSoup(response.content, 'html.parser')

    header1 = soup.find('h1')
    if not header1:
        print(f'[{response.status_code} {response.reason}] No headers at', url)
        continue

    if header1.next_sibling: hSibs = header1.next_siblings
    else:
        hParent = next((p for p in header1.parents if p.next_sibling), None)
        hSibs = hParent.next_siblings if hParent else []

    h1Sibs = []
    for ns in hSibs:
        if ns.name == 'h1' or (not isinstance(ns,str) and ns.find('h1')): break
        h1Sibs.append(ns)
    h1Sibs_text = '\n---\n'.join(ns.get_text(' ') for ns in h1Sibs)

# --- block 2 ---
if url.startswith('https://economictimes.indiatimes.com/'): ## might need more
    h1Sibs = soup.select('*:has(>h1.artTitle)~*') 
    h1Sibs_text = '\n---\n'.join(ns.get_text(' ') for ns in h1Sibs)

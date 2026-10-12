# Code from my Stack Overflow answer https://stackoverflow.com/a/75272195 (posted 2023-01-29), extracted verbatim; may need the question's context to run.
# url = 'https://en.wikipedia.org/wiki/Chris_Yonge' [ for example ]
# soup = BeautifulSoup(requests.get(url).content)

# item_header = soup.find_all(re.compile('^h[1-6]')) # should be same as
item_header = soup.find_all([f'h{i}' for i in range(1,7)])

skipTags = ['script', 'style'] # any tags you don't want text from
hSections = []

for h in item_header:
    sectionLines = []

    for ns in  h.find_next_siblings():
        if ns in item_header: break # stop if/when next header is reached
        if ns.name in skipTags: continue # skip certain tags

        sectionLines.append(' '.join(ns.get_text(' ').split())) 
        # [ split+join to minimize whitespace ] 

    hSections.append({
        'header_type': h.name, 'header_text': h.get_text(' ').strip(),
        'section_text': '\n'.join([l for l in sectionLines if l])
    })

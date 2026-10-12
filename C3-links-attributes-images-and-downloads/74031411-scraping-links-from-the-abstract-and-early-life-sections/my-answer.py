# Code from my Stack Overflow answer https://stackoverflow.com/a/74036946 (posted 2022-10-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
content = soup.select_one('#mw-content-text > .mw-parser-output').children
splitContent = []

# --- block 2 ---
for c in content:
    if c.name == 'h2' or splitContent == []:
        sectionName = 'Abstract' if splitContent == [] else c.text
        splitContent.append({
            'section': sectionName, 
            'listSoups': [], 'HTML': '', 'asText': ''
        }) 

    splitContent[-1]['listSoups'].append(c)
    splitContent[-1]['HTML'] += str(c)
    if c.name not in ['style', 'script']: 
        splitContent[-1]['asText'] += c.text

# --- block 3 ---
for i in range(len(splitContent)):
    splitContent[i]['asSoup'] = BeautifulSoup(splitContent[i]['HTML'], 'html.parser')

# --- block 4 ---
for h in soup.findAll('span',attrs={'class':'mw-headline'}):
    hLevel = int(h.parent.name.replace('h', ''))
    print(('\t'*(hLevel-2))+'↳', f'[{h.parent.name}] {h.text}')

# --- block 5 ---
sectnTexts_dict = dict([(
    sc['section'].replace(' ', '_'), # section name to key
    sc['asText'] # section text as value
) for sc in splitContent])

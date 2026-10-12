# Code from my Stack Overflow answer https://stackoverflow.com/a/74071424 (posted 2022-10-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
docContents = open('Unknow Data Type.txt', mode='r', encoding='utf-8-sig').read()
formHtml = json.loads(docContents)['form']

# --- block 2 ---
formSoup = BeautifulSoup(formHtml, 'html.parser')

for t in formSoup.find_all('table'):
    print('+'*100)
    for r in t.find_all('tr'):
        cols = [c.text for c in r.find_all(['td', 'th'])]
        cols = [f'{c[:10].strip():^12}' for c in cols] #just formatting
        print(f'| {" | ".join(cols)} |')
    print('+'*100)

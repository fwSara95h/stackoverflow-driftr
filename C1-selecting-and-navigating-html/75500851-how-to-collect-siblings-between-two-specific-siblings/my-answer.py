# Code from my Stack Overflow answer https://stackoverflow.com/a/75504991 (posted 2023-02-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# [ linkToSoup defined at https://pastebin.com/rBTr06vy ]
# soup = linkToSoup('https://en.wikipedia.org/wiki/Coal_gas') 

headerTags = soup.select('h2')
chapter_data, totalCh = [], len(headerTags)
for ci, (h, nxt_h) in enumerate(zip(headerTags, headerTags[1:]+[None]), 1):
    print('', end=f'\rAdding chapter {ci} of {totalCh}') ## track progress

    texts, htmls = '', ''
    for sib in h.next_siblings:
        if sib == nxt_h: break
        if callable(getattr(sib, 'get_text', None)): 
            texts += '\n' + sib.get_text(' ', strip=True)
        htmls += '\n' + str(sib).strip()

    # texts = BeautifulSoup(htmls).get_text(' ', strip=True)
    chapter_data.append({
        'chapter': h.get_text(' ', strip=True),
        'text': texts.strip(), 'html': htmls.strip()
    })
print('\n')

chapters = pd.DataFrame(chapter_data)

# --- block 2 ---
chapter_data = [{
    'chapter': h.get_text(' ', strip=True),
    'html': '\n'.join(
        str(sib) for sib in h.next_siblings if
        sib!=nxt_h and nxt_h not in sib.previous_siblings
    ).strip()
} for h, nxt_h in zip(headerTags, headerTags[1:]+[None])]

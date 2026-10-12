# Code from my Stack Overflow answer https://stackoverflow.com/a/74635364 (posted 2022-11-30), extracted verbatim; may need the question's context to run.
hhSel = 'h2:has(#History)'
htSel = f'{hhSel} ~ *:not(style):not(h2):not({hhSel} ~ h2 ~ *)'
hSectTags = soup.select(htSel)

for hst in hSectTags:
    flatTxt = ' '.join(w for w in hst.get_text(' ').split() if w)
    print(hst.name, '--->', flatTxt[:100] if flatTxt else hst)

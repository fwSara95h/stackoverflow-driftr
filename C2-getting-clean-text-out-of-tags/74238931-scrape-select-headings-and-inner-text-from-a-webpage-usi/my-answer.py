# Code from my Stack Overflow answer https://stackoverflow.com/a/74243113 (posted 2022-10-29), extracted verbatim; may need the question's context to run.

# --- block 1 ---
from bs4 import BeautifulSoup
import requests
import pandas

website = requests.get('https://venngage.com/blog/landing-page-examples/')
preString =  {'h1': '', 'h2': '\t', 'h3':'\t\t', 'h4':'\t\t\t'}


htagNames = [k for k in preString.keys()]
htags = soup.find_all(htagNames)
# if you want from within a particular section
# htags = soup.select_one('article.post').find_all(htagNames) 

for h in htags:
    pStrings = []
    for tag in h.find_next_siblings(htagNames+['p']): 
        if tag.name == 'p' and tag.string is not None: 
            pStrings.append(tag.string)
        if tag.name in htagNames: break

    headingRows.append({
        'headingType': h.name, # 'headingText': h.string, 
        'headingText': preString[h.name] + h.get_text(' ' , strip=True),  
        'paragraphs': '\n'.join(pStrings)
    }) 

# can filter out heading with no paragraphs with
# headingRows = [hr for hr in headingRows if hr['paragraphs']]

# save as csv
pandas.DataFrame(headingRows).to_csv('hRows.csv', index=False)

# --- block 2 ---
tags = soup.find_all(htagNames+['p']) 

lastTag = tags[-1]
headingRows = []
hInit = {'headingType': None, 'headingText': None, 'paragraphs': []}
curHeading = dict(hInit) # copy

for i, t in enumerate(tags): 
    if t.name == 'p' and t.string is not None: 
        curHeading['paragraphs'].append(t.string) 

    if t.name in preString: 
        curHeading['headingType'] = t.name
        #curHeading['preStr'] = preString[t.name]
        curHeading['headingText'] = preString[t.name] + t.get_text(' ' , strip=True) # + t.string

    if t == lastTag or tags[i+1].name in preString:
        # if you want possible paras before 1st heading, remove if condition
        if curHeading['headingType'] is not None :
            curHeading['paragraphs'] ='\n'.join(curHeading['paragraphs'])
            headingRows.append(curHeading)

        curHeading = dict(hInit) # copy
        curHeading['paragraphs'] = []

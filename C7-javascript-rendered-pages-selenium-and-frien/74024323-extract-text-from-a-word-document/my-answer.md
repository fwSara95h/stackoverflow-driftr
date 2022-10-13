---
title: "Extract Text from a word document"
site: stackoverflow
question_id: 74024323
answer_id: 74051264
url: https://stackoverflow.com/a/74051264
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-13T06:22:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74051264/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 331d6c2cab2d9a06f29e69ecc8ce5eb2a37ff19e211e17a4883279cad15672cd
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74051264>, 2022-10-13; **accepted**; score 1. Text as retrieved 2026-10-12.

There are some inconsistencies in the document -  phone numbers starting with *Tel:* sometimes, and *Tel.:* other times, and even *Te:* once, and I noticed one of the emails is just in the last line for that distributor without the *Email:* prefix, and the State isn't always in the last line.... Still, for the most part, most of the data can be extracted with [regex](https://docs.python.org/3/library/re.html) and/or [splits](https://www.w3schools.com/python/ref_string_split.asp).

The distributors are separated by empty lines, and the names are in a different color - so I defined this function to get the font color of any paragraph from its xml:
```python
# from bs4 import BeautifulSoup

def getParaColor(para):
  try:
    return BeautifulSoup(
        para.paragraph_format.element.xml, 'xml'
    ).find('color').get('w:val')
  except:
    return ''
```
The `try...except` hasn't been necessary yet, but just in case...

(The xml is actually also helpful for double-checking that `.text` hasn't missed anything - in my case, I noticed that the email for *Shri Adhya Educational Books* wasn't getting extracted.)

Then, you can process the paragraphs from `docx.Document` with a function like:
```python
# import re

def splitParas(paras):
  ptc = [(
      p.text, getParaColor(p), p.paragraph_format.element.xml
  ) for p in paras]
  curSectn = 'UNKNOWN'
  splitBlox = [{}]

  for pt, pc, px in ptc:
    # double-check for missing text
    xmlText = BeautifulSoup(px, 'xml').text
    xmlText = ' '.join([s for s in xmlText.split() if s != ''])
    if len(xmlText) > len(pt): pt = xmlText

    # initiate
    if not pt:
      if splitBlox[-1] != {}:
        splitBlox.append({})
      continue
    if pc == '20752E':
      curSectn = pt.strip()
      continue
    if splitBlox[-1] == {}:
      splitBlox[-1]['section'] = curSectn
      splitBlox[-1]['raw'] = [] 
      splitBlox[-1]['Name'] = []
      splitBlox[-1]['address_raw'] = []

    # collect
    splitBlox[-1]['raw'].append(pt)   
    if pc == 'D12229':
      splitBlox[-1]['Name'].append(pt)
    elif re.search("^Te.*:.*", pt):
      splitBlox[-1]['tel_raw'] = re.sub("^Te.*:", '', pt).strip()
    elif re.search("^Mob.*:.*", pt):
      splitBlox[-1]['mobile_raw'] = re.sub("^Mob.*:", '', pt).strip()
    elif pt.startswith('Email:') or re.search(".*[@].*[.].*", pt):
      splitBlox[-1]['Email'] = pt.replace('Email:', '').strip()
    else:
      splitBlox[-1]['address_raw'].append(pt)
  
  # some cleanup
  if splitBlox[-1] == {}: splitBlox = splitBlox[:-1]
  for i in range(len(splitBlox)):
    addrsParas = splitBlox[i]['address_raw'] # for later

    # join lists into strings
    splitBlox[i]['Name'] = ' '.join(splitBlox[i]['Name'])
    for k in ['raw', 'address_raw']:
      splitBlox[i][k] = '\n'.join(splitBlox[i][k])

    # search address for City, State and PostCode
    apLast = addrsParas[-1].split(',')[-1]
    maybeCity = [ap for ap in addrsParas if '–' in ap]
    if '–' not in apLast:
      splitBlox[i]['State'] = apLast.strip()
    if maybeCity:
      maybePIN = maybeCity[-1].split('–')[-1].split(',')[0]
      maybeCity = maybeCity[-1].split('–')[0].split(',')[-1]
      splitBlox[i]['City'] = maybeCity.strip()
      splitBlox[i]['PostCode'] = maybePIN.strip()
    
    # add mobile to tel
    if 'mobile_raw' in splitBlox[i]:
      if 'tel_raw' not in splitBlox[i]:
        splitBlox[i]['tel_raw'] = splitBlox[i]['mobile_raw']
      else:
        splitBlox[i]['tel_raw'] += (', ' + splitBlox[i]['mobile_raw'])
      del splitBlox[i]['mobile_raw']

    # split tel [as needed]
    if 'tel_raw' in splitBlox[i]:
      tel_i = [t.strip() for t in splitBlox[i]['tel_raw'].split(',')] 
      telNum = []

      for t in range(len(tel_i)):
        if '/' in tel_i[t]:
          tns = [t.strip() for t in tel_i[t].split('/')]
          tel1 = tns[0]
          telNum.append(tel1)
          for tn in tns[1:]:
            telNum.append(tel1[:-1*len(tn)]+tn)
        else:
          telNum.append(tel_i[t])
      
      splitBlox[i]['Tel_1'] = telNum[0]
      splitBlox[i]['Tel'] = telNum[0] if len(telNum) == 1 else telNum
  
  return splitBlox
```

 - (Since I was getting font color anyway, I decided to add another
   column called "section" to put East/West/etc in. And I added "PostCode" too, since it seems to be on the other side of "City"...)
 - Since "raw" is saved, any other value can be double checked manually at least.
 - The function combines "Mobile" into "Tel" even though they're extracted with separate regex.
    - I'd say "Tel_1" is fairly reliable, but some of the inconsistent patterns mean that other numbers in "Tel" might come out incorrect if they were separated with '/'.
    - Also, "Tel" is either a string or a list of strings depending on how many numbers there were in "tel_raw".

After this, you can just [view as DataFrame](https://i.ibb.co/3sfx70p/Capture.png) with:
```python
#import docx
#import pandas 

content = docx.Document('HE Distributors.docx')
# pandas.DataFrame(splitParas(content.paragraphs)) # <--all Columns
pandas.DataFrame(splitParas(content.paragraphs))[[
    'section', 'Name', 'address_raw', 'City', 
    'PostCode', 'State', 'Email', 'Tel_1', 'tel_raw'
]]
```

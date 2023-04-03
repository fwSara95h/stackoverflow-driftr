---
title: "BS Extract all text between two specified keyword"
site: stackoverflow
question_id: 75914833
answer_id: 75919408
url: https://stackoverflow.com/a/75919408
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-03T12:16:57Z
last_edited: 2023-04-03T12:35:13Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75919408/revisions
accepted: false
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4a87b4b82c074cfb1c01892270eec8232023d637fd6cff93d2270c761dd5fa99
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75919408>, 2023-04-03, last edited 2023-04-03; score 1. Text as retrieved 2026-10-12.

###### Setup:

```py
# from bs4 import BeautifulSoup
# htmlStr = response.text ## if you're fetching with a request
htmlStr = '''
<div>
    <h3>Some Section</h3>
    Some text from Section 1

    <h3> Contact </h3>
    Adresse : Address Line One <br/> Address Line Two <br/>
    Téléphone : 0X XX XX XX XX <br/> 
    Site : <a href="https://example.com/">https://example.com/</a>

    <h3>Some Other Section</h3>
    field 1 : some info 
    field 2 : __ <br/> field 3 : some other info
</div>
'''

soup = BeautifulSoup(htmlStr, 'lxml')
```

<br>

----

<br>

### Getting All Information in a Section

```py
def get_section_info(section_header):
    hName, hList = section_header.name, 'h1,h2,h3,h4,h5,h6'
    hList = [h for h in hList.split(hName)[0].split(',') if h] + [hName]

    section_info, cur_key = {}, None
    for ns in section_header.next_siblings:
        if ns.name in hList: break ## stop if you reach the next section
        if not ((isinstance(ns,str) and not ns.PREFIX) or ns.name): continue ## skip

        nsStr = ' '.join((ns if isinstance(ns,str) else ns.get_text(' ')).split())
        if ':' in nsStr and not nsStr.startswith('http'): 
            cur_key, nsStr = [s.strip() for s in nsStr.split(':',1)]

        ckStr = section_info.get(cur_key, '')
        if ns.name == 'br': section_info[cur_key] = ckStr + ' \n'
        elif nsStr: section_info[cur_key] = ckStr + ' ' + nsStr
    
    section_info = {k:v.strip() for k,v in section_info.items()}
    return section_info[None] if [*section_info]==[None] else section_info
```

<br>

This might look a bit unnecessarily convoluted, but you could get all the contact information with 

```py
if (contact_h3 := soup.find('h3', string=lambda s: s and s.strip()=='Contact')):
    contact_info = get_section_info(contact_h3)
else: contact_info, _ = {}, print('Could not find <h3>Contact</h3>')
```

and `contact_info` would look like 

> ```py
> { 'Adresse': 'Address Line One \n Address Line Two', 
>   'Téléphone': '0X XX XX XX XX', 
>   'Site': 'https://example.com/' }
> ```

<br>

You could even get all the `h3` sections as simply as 

```py
{h3.text.strip(): get_section_info(h3) for h3 in soup.select('h3')}
```

which would return 

> ```py
> {
>   'Some Section': 'Some text from Section 1',
>   'Contact': {
>     'Adresse': 'Address Line One \n Address Line Two',
>     'Téléphone': '0X XX XX XX XX',
>     'Site': 'https://example.com/'
>   },
>   'Some Other Section': {
>     'field 1': 'some info field 2 : __', 'field 3': 'some other info'
>   }
> }
> ```

<sup>Note: `field 2` is merged into `field 1` value because there's nothing separating them in the HTML, so there's no way to know if the key should be `2` or `field 2` or `info field 2` or... so the function assumes that there is a maximum of one field per [NavigableString](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#bs4.NavigableString); and `'Some Section'` only has a string value instead of a dictionary since there doesn't seem to be any `:`s separating field names from the relevant info.</sup>

<br>

---

<br>

### Getting Only One Chunk of Text

If you really just only want the text between two words, you can just use 

```py
def get_textchunk(word1, word2, text):
    if not (word1 in text and word2 in text): return ''
    return text.split(word1)[-1].split(word2)[0]
    ## can refine with more conditions/string-manipulations/regex/etc

get_textchunk('Adresse :', 'Téléphone :', soup.get_text(' '))
```

However, if you're not sure of the next field name, but you're sure that the field names are separated with `:`, you can use this version of `get_section_info`:

```py
def get_text_by_field(soupX, fieldName):
    fsCond = lambda s: s and ':' in s and s.split(':')[0].strip()==fieldName
    fieldStr = soupX.find(string=fsCond)
    hList, myText = [f'h{i}' for i in range(1,7)], fieldStr.split(':',1)[1]
    for ns in (fieldStr.next_siblings if fieldStr else []):
        if ns.name in hList: break ## stop when you reach the next section
        if not ((isinstance(ns,str) and not ns.PREFIX) or ns.name): continue 

        nsStr = ' '.join((ns if isinstance(ns,str) else ns.get_text(' ')).split())
        if ':' in nsStr and not nsStr.startswith('http'): break

        if ns.name == 'br': myText += ' \n'
        elif nsStr: myText += (' ' + nsStr)
    return myText.strip()
```

then `get_text_by_field(soup, 'Adresse')` should return

> ```py
> 'Address Line One \n Address Line Two'
> ```

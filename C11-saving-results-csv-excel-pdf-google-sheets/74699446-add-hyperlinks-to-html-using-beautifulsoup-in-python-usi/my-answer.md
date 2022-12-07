---
title: "Add Hyperlinks to HTML using BeautifulSoup in Python using Anchor Text and URL stored in a CSV File"
site: stackoverflow
question_id: 74699446
answer_id: 74722905
url: https://stackoverflow.com/a/74722905
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-07T21:17:11Z
last_edited: 2023-01-04T16:01:45Z
revisions: 9
revision_history: https://stackoverflow.com/posts/74722905/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0); the revisions listed under edited_by_others are those users' work under CC BY-SA 4.0
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7c3784de22e91b46e47d5ba274174f5b0c32c7d7e1d223dc6e1ced6ca6bbf65a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
edited_by_others:
  - "Abhishek R (https://stackoverflow.com/users/5576536), revisions 3-9, 2022-12-15 to 2023-01-04, CC BY-SA 4.0 — added 47 characters in body; Multiple links in same line loses its space.; added 37 characters in body; Fixed issues with sentences with special characters; Edits to handle special characters that follows words like !.? which were not getting hyperlinked in previous code; Added a few lines of code to prevent the creation of nested hyperlinks; added 1066 characters in body"
---

# My answer — 2022-12-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74722905>, 2022-12-07, last edited 2023-01-04; **accepted**; score 1. Text as retrieved 2026-10-12. Later revisions by other users are listed in the front matter.

You should try with anchor/links on the outer loop and then break down the matching strings in the inner loop:

```python
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from bs4 import element as bs4_element
import csv

html_doc = """
<!-- wp:paragraph -->
<p>This is a existing link <a class="test" href="https://yahoo.com/">Yahoo</a> Text</p>
<!-- /wp:paragraph -->
 
<!-- wp:paragraph -->
<p>This is another Google Text</p>
<!-- /wp:paragraph -->
 
<!-- wp:paragraph -->
<p>This is another lowercase bing Text</p>
<!-- /wp:paragraph -->
 
<!-- wp:paragraph -->
<p>This is another multi word Active Campaign.</p>
<!-- /wp:paragraph -->
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# read the CSV file with anchor text and hyperlinks
with open('file.csv', 'r') as csv_file:
  reader = csv.reader(csv_file)
  hyperlinks = dict(reader)


# from bs4 import element as bs4_element
be_navStr = bs4_element.NavigableString
 
hList = [
    (anchor_text.strip(), hyperlink.strip()) for
    anchor_text, hyperlink in hyperlinks.items()
    if anchor_text.strip() and hyperlink.strip() # no blanks
]
 

print('#'*35, 'OLD', '#'*35, '\n')
print(soup, '\n')
print('#'*75, '\n\n\n')

for txt, link in hList:
    navStrs = [
        d for d in soup.descendants if type(d) == be_navStr 
        # and f' {txt.lower()} ' in f' {d.string.strip().lower()} ' # same as
        # and f' {txt.lower()} ' in f' {d.string.strip().lower()} ' # same as
        # and (' '+txt.lower()+' ') in (' '+d.string.strip().lower()+' ')
        and (' '+re.sub('\W+',' ',txt.lower())+' ') in (' '+re.sub('\W+',' ',d.string.strip().lower())+' ') # Handles special characters like ?.!
    ]


    

    for ns in navStrs: 
        # tLen, remStr = len(txt), f' {ns.get_text().strip()} '
        tLen, remStr = len(txt), f' {ns.string} '
        remLen = len(remStr)
        # tLen, remStr = len(txt), f' {ns.text.strip()} '

        if remStr[1:-1].lower() == txt.lower():
            # to skip if it's already a hyperlink
            if ns.parent.name == 'a': 
                ns.parent['href'] = link # comment if you dont want to replace/update link
                continue 
        # Skip creating nested hyperlinks inside existing hyperlinks       
        if ns.parent.name == 'a': 
          continue 


        i = 0        
        while ' '+re.sub('\W+',' ',txt.lower())+' ' in re.sub('\W+',' ',remStr.lower()) and remStr.lower().find(f'{txt.lower()}') > -1:
            
            #print(txt.lower())
            #print(re.sub('\W+',' ',remStr.lower()))

            sInd = remStr.lower().find(f'{txt.lower()}')
            #print(remStr.lower())
            #print(sInd)
            hlTag = soup.new_tag('a', href=link)
            hlTag.append(remStr[sInd:sInd + tLen])
            #print(hlTag)
            if i == 0:
              newCont = [remStr[1:sInd], hlTag]
            else:
              newCont = [remStr[:sInd], hlTag]
            #print(newCont)

            for addn in newCont: ns.insert_before(addn)
            #print(soup)

            remStr = remStr[sInd + tLen:remLen-1]
            #print(remStr)
            i += 1

        ns.replace_with(remStr)
        #print(soup)

print('#'*35, 'NEW', '#'*35, '\n')
print(soup, '\n')
print('#'*75)
```

printed output:

```html
################################### OLD ################################### 

<!-- wp:paragraph -->
<p>This is a existing link <a class="test" href="https://yahoo.com/">Yahoo</a> Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another Google Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another lowercase bing Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another multi word Active Campaign.</p>
<!-- /wp:paragraph --> 

########################################################################### 



################################### NEW ################################### 

<!-- wp:paragraph -->
<p>This is a existing link <a class="test" href="https://yahoo.com/">Yahoo</a> Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another <a href="https://www.google.com">Google</a> Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another lowercase <a href="https://bing.com">bing</a> Text</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>This is another multi word <a href="https://activecampaign.com">Active Campaign</a>.</p>
<!-- /wp:paragraph --> 

###########################################################################
```

This should work even with multiple matches in the same string as long as they don't overlap (like *"Google Chrome"* and *"Chrome Beta"*)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Abhishek R](https://stackoverflow.com/users/5576536)** (2022-12-09): Is this Python3? I am getting an invalid syntax error in this section `anchor_text, hyperlink in hyperlinks.items()`.   How are you reading the csv file? Are you using the code snippet I am using?
- **me** (2022-12-09): @AbhishekR Sorry I missed a `for` in that list comprehension (I've edited to fix it now),  but yes `hyperlinks.items()` is based on the same `hyperlinks` from your snippet. That statement is the only one I typed out (to fit into your code) without testing since I got my `hList` by processing `pandas.read_html('https://stackoverflow.com/questions/74699446')[0].to_dict('records')`,  which is a list of dictionaries instead of a single dictionary...
- **[Abhishek R](https://stackoverflow.com/users/5576536)** (2022-12-09): I am now getting an error here: `and f' {txt.lower()} ' in f' {d.get_text().strip().lower()} '`   Sorry I am unaware of this syntax.
- **me** (2022-12-09): @AbhishekR what error are you getting there? It's just normalizing the space and making it case-insensitive (so that "bing" or  "Bing" will be matched by "Bing" and "let's use Bing" and "sample bing line", but not "binged", etc), this should be ok in python3 but in case the formatted text is the issue, try *`and f' {} '.format(txt.lower()) in f' {} '.format(d.get_text().strip().lower())`* or **`and (' '+txt.lower()+' ') in (' '+d.get_text().strip().lower()+' ')`** instead
- **[Abhishek R](https://stackoverflow.com/users/5576536)** (2022-12-10): I am getting the error: `SyntaxError: f-string: empty expression not allowed`
- **[Abhishek R](https://stackoverflow.com/users/5576536)** (2022-12-10): Here is my code https://pastebin.com/6LUti6iw
- **me** (2022-12-10): @AbhishekR sorry again, I typed my last comment too carelessly - formatted text should be either like `f'{x}'` or `'{x}'.format(x)` - so it should be **`and ' {} '.format(txt.lower()) in ' {} '.format(d.get_text().strip().lower())`** - but what I was asking was what error did you get with the original *`and f' {txt.lower()} ' in f' {d.get_text().strip().lower()} '`*?
- **me** (2022-12-10): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/250305/discussion-between-driftr95-and-abhishek-r).
- **[Abhishek R](https://stackoverflow.com/users/5576536)** (2022-12-30): Glad we could get this working

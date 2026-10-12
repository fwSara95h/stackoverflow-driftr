# Code from my Stack Overflow answer https://stackoverflow.com/a/74722905 (posted 2022-12-07), extracted verbatim; may need the question's context to run.
# Includes later revisions by: Abhishek R (https://stackoverflow.com/users/5576536), revisions 3-9, 2022-12-15 to 2023-01-04, CC BY-SA 4.0.
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

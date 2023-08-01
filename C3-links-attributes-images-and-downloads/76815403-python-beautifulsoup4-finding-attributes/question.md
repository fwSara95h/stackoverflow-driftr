---
title: "Python BeautifulSoup4 Finding Attributes"
site: stackoverflow
question_id: 76815403
url: https://stackoverflow.com/q/76815403
asked: 2023-08-01T21:50:55Z
asked_by: "Notsuj"
asked_by_url: https://stackoverflow.com/users/9990060
last_edited: never
tags: [python-3.x, beautifulsoup, html-parsing]
score: 0
views_at_snapshot: 33
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ff9a9d016954f1770556c34e34b10736dd66271c16ac438b5d0234c84d77687f
---

# Python BeautifulSoup4 Finding Attributes

Asked by [Notsuj](https://stackoverflow.com/users/9990060) on Stack Overflow, <https://stackoverflow.com/q/76815403>, 2023-08-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Right now i am building a web scraper to grab the actual href link after the <a> tag to then continue and make a file with all of the values I grab. 

I just want to grab the "/groups/1234123" Attribute value and the ID name ("InsertNameHere") but nothing is working.

```
from bs4 import BeautifulSoup

htmltext = ''' <div class="sidenav">
         <div class="sidenav-head" id="InsertNameHere">   
          <a href="/groups/1234123/">
           InsertNameHere
          </a>
         </div>
        </div>'''
 
soup = BeautifulSoup(htmltext, 'html.parser')

s = soup.find_all('a')
link= s.find('href')

print(link)

```



Im getting the

"AttributeError:ResultSet object has no attribute 'find'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?"

I have tried to change the 
`link = s.find('href')`
to 
`link = s.attrs`

It says I have a different Attribute Error after that.
I also need to keep the `s.find_all()` attribute because there are multiple id's that i need to grab.

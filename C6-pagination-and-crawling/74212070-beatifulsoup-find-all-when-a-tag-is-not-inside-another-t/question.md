---
title: "Beatifulsoup find_all when a tag is not inside another tag"
site: stackoverflow
question_id: 74212070
url: https://stackoverflow.com/q/74212070
asked: 2022-10-26T17:45:26Z
asked_by: "hit"
asked_by_url: https://stackoverflow.com/users/11725310
last_edited: never
tags: [python, html, python-3.x, beautifulsoup, html-parsing]
score: -1
views_at_snapshot: 57
answer_count: 1
accepted_answer_id: 74213323
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a29bd01ff42b0b9cdee3537f8455dee320b057cb21b2f6bb605ad493b4c5981d
---

# Beatifulsoup find_all when a tag is not inside another tag

Asked by [hit](https://stackoverflow.com/users/11725310) on Stack Overflow, <https://stackoverflow.com/q/74212070>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
html = """
<html>
   <h2>Top Single Name</h2>
   <table>
      <tr>
         <p>hello</p>
      </tr>
   </table>
   <div>
      <div>
         <h2>Price Return</h2>
      </div>
   </div>
</html>
"""
```
When I Use below code 

```
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html, 'html.parser')
soup.find_all(['p', 'li', 'dl', 'tr', 'div', re.compile("^h[1-6]$")])
```
I am getting output as 
```
[<h2>Top Single Name</h2>,
 <tr><p>hello</p></tr>,
 <p>hello</p>,
 <div>
 <div>
 <h2>Price Return</h2>
 </div>
 </div>,
 <div>
 <h2>Price Return</h2>
 </div>,
 <h2>Price Return</h2>]
```
But what I need is below only three elements
```
[<h2>Top Single Name</h2>,
<tr><p>hello</p></tr>,
<div>
 <div>
 <h2>Price Return</h2>
 </div>
 </div>
]
```
Basically I don't want to extract a specific tag if it is inside another tag, is there any way i can have some mapping like below and use in the code don't extract when the key is inside value
```
{'re.compile("^h[1-6]$")': 'div', 'div':'div', 'p': 'tr'}
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Nuri Taş](https://stackoverflow.com/users/19255749)** (2022-10-26): Don't the second and third elements in the expected output have more than one tag? The output should include `<p>hello</p>` and `<h2>Price Return</h2>`  IIUC?
- **[hit](https://stackoverflow.com/users/11725310)** (2022-10-26): I don't want to extract ```<p>hello</p>``` as it is inside <tr> tag, similarly for ```<h2>Price Return</h2>```

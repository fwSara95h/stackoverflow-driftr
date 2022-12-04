---
title: "print contents of remaining tags after a tag beautifulsoup"
site: stackoverflow
question_id: 74677516
url: https://stackoverflow.com/q/74677516
asked: 2022-12-04T14:24:59Z
asked_by: "Ajay Surya Senthilrajan"
asked_by_url: https://stackoverflow.com/users/20681043
last_edited: 2022-12-04T15:23:19Z
tags: [python, html, python-3.x, beautifulsoup]
score: 0
views_at_snapshot: 50
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9f38c028a678519e05c9dc3888400e217a5f753722382af723b3e38f7ed86d0f
---

# print contents of remaining tags after a tag beautifulsoup

Asked by [Ajay Surya Senthilrajan](https://stackoverflow.com/users/20681043) on Stack Overflow, <https://stackoverflow.com/q/74677516>, 2022-12-04, last edited 2022-12-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i just printed all the contents of **li** using `.find_all('li')` and i want to continue printing **'p'** tags after **li** tag ends, like not **'p'** tags in the beginning of html or inbetween. 'p' tags or remaining tags at the end. please help. Basically need everything after final list-end tag.

```
from bs4 import BeautifulSoup

html_doc = """\
<html>
<p>
don't need this
</p>
<li>
text i need
</li>
<li>
<p>
don't need this
</p>
<p>
don't need this
</p>
<li>
text i need 
    <ol>
    <li>
    text i need but appended to parent li tag
    </li>
    <li>
    text i need but appended to parent li tag
    </li>
    </ol>
</li>
<li>
text i need
</li>
<p>
also need this
</p>
<p>
and this
</p>
<p>
and this too
</p>"""

soup = BeautifulSoup(html_doc, "html.parser")

for li in soup.select("li"):
    if li.find_parent("li"):
        continue
    print(" ".join(li.text.split()))
    print("--sep--")
```

**this prints**


```
text i need
--sep--
text i need text i need but appended to parent li tag text i need but appended to parent li tag
--sep--
text i need
--sep--
```

thanks to @Andrej Kesely

**i need this**

```
text i need
--sep--
text i need text i need but appended to parent li tag text i need but appended to parent li tag
--sep--
text i need
--sep--
also need this
--sep--
and this
--sep--
and this too
--sep--
```

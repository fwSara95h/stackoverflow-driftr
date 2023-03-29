---
title: "How to get text in BS and add a tag around it"
site: stackoverflow
question_id: 75879570
answer_id: 75880227
url: https://stackoverflow.com/a/75880227
author: "Elodin"
author_url: https://stackoverflow.com/users/15637435
posted: 2023-03-29T17:12:51Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3d2a516afebe8e02723fa757ad1cf61ca86707dbb7a0e12135d847157772db8d
role: another answer on the same question, kept as context; not my work
---

# Answer by [Elodin](https://stackoverflow.com/users/15637435) — 2023-03-29

Posted on Stack Overflow, <https://stackoverflow.com/a/75880227>, 2023-03-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is a potential solution, if I understood you correctly. I would go for a simple string replacement instead of doing the whole thing with the soup. 

**Code**


```python
xml = """<p>
    lorem ipsum dolor <hi>a</hi>met.
    Thing_A, <thing>Thing_B</thing>, Thing_C
    </p>"""

things = ['Thing_A', 'Thing_B', 'Thing_C']

# Replicating the soup you already have 
soup = BeautifulSoup(xml, 'lxml')

# Convert soup to string for replacement
new_xml = str(soup)

# To be specified
tag_start = '<thing>'
tag_end = '</thing>'

for thing in things:

    replacement_string = f"{tag_start}{thing}{tag_end}"
    new_xml = new_xml.replace(thing, replacement_string)

# drop potential created duplicates
new_xml = new_xml.replace(f"{tag_start}{tag_start}", tag_start)
new_xml = new_xml.replace(f"{tag_end}{tag_end}", tag_end)

# Create soup again
soup = BeautifulSoup(new_xml, 'lxml')
print(soup)
print(f"Type: {type(soup)}")
```
**Output**
```python
html><body><p>
    lorem ipsum dolor <hi>a</hi>met.
    <thing>Thing_A</thing>, <thing>Thing_B</thing>, <thing>Thing_C</thing>
</p></body></html>
Type: <class 'bs4.BeautifulSoup'>
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[KWunsch](https://stackoverflow.com/users/15513340)** (2023-03-29): I acme up with a working solution: https://pastebin.com/Zyx5wEia (I am actualy talking about ships here I missed making it generic :-D )  Our solutions have the same problem: they move the <body> tag for whole documents around the result. (That would be an issue :-D )
- **[Elodin](https://stackoverflow.com/users/15637435)** (2023-03-29): Can you make an example for "move the <body> tag for whole documents around the result"?
- **[KWunsch](https://stackoverflow.com/users/15513340)** (2023-03-29): added it to the top
- **[KWunsch](https://stackoverflow.com/users/15513340)** (2023-03-29): https://stackoverflow.com/questions/75880413/beautifulsoup-puts-body-tag-around-xml-document  maybe better talk about it here, since technically u answered the question :-D

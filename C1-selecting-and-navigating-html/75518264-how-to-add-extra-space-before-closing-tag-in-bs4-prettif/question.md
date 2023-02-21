---
title: "how to add extra space before closing tag in bs4 prettify?"
site: stackoverflow
question_id: 75518264
url: https://stackoverflow.com/q/75518264
asked: 2023-02-21T09:04:18Z
asked_by: "Pierrick Rambaud"
asked_by_url: https://stackoverflow.com/users/6734243
last_edited: 2023-02-22T17:43:54Z
last_editor: "CrazyChucky"
last_editor_url: https://stackoverflow.com/users/12975140
tags: [python, beautifulsoup]
score: 3
views_at_snapshot: 84
answer_count: 1
accepted_answer_id: 75536103
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 16ded996ff178dcb89cfd47b0094196ab60bb2a5d4bd58e4f0002f52eba94ba6
---

# how to add extra space before closing tag in bs4 prettify?

Asked by [Pierrick Rambaud](https://stackoverflow.com/users/6734243) on Stack Overflow, <https://stackoverflow.com/q/75518264>, 2023-02-21, last edited 2023-02-22 by [CrazyChucky](https://stackoverflow.com/users/12975140). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm using bs4 to parse html output in my test suit and compare them with existing html files. 
prettify and prettier behaviour seems different in how they manage closing tags. 

Using the following inputs: 
```python
from bs4 import BeautifulSoup, formatter

fmt = formatter.HTMLFormatter(indent=2)
str_ = '<video preload="auto"><source src="_static/video.mkv" type=""/></video>'
html = BeautifulSoup(str_, "html.parser")
html.prettify(formatter=fmt)
```

I get the following output:
```html
<video preload="auto">
  <source src="_static/video.mp4" type="video/mp4"/>
</video>
```

But to fully respect standards I should have an extra space before the closing tag (after the attributes of "source"). Is it possible ?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[D Malan](https://stackoverflow.com/users/3486675)** (2023-02-21): I think you forgot to add the output of the first code snippet?
- **[Pierrick Rambaud](https://stackoverflow.com/users/6734243)** (2023-02-21): I'm simply reusing the varaible in the second one, let me edit to clarify
- **me** (2023-02-22): If you pass `void_element_close_prefix=' /'` to *`.HTMLFormatter`* then the `source` tag should end with **`... />`** instead of *`.../>`* [like this](https://i.sstatic.net/2HQs5.png). Is that what you're going for?
- **[Pierrick Rambaud](https://stackoverflow.com/users/6734243)** (2023-02-22): that's exactly what I needed, if you publish it ass an answer I will accept it

---
title: "BeautifulSoup find a href in marquee"
site: stackoverflow
question_id: 74661666
url: https://stackoverflow.com/q/74661666
asked: 2022-12-02T21:28:54Z
asked_by: "facepet"
asked_by_url: https://stackoverflow.com/users/16836514
last_edited: 2022-12-03T09:36:19Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 80
answer_count: 1
accepted_answer_id: 74663126
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4cbe8062a92889cdef636e4f3c0274196c1c710a17dd139a06a0369ae62fa2d6
---

# BeautifulSoup find a href in marquee

Asked by [facepet](https://stackoverflow.com/users/16836514) on Stack Overflow, <https://stackoverflow.com/q/74661666>, 2022-12-02, last edited 2022-12-03 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm using bs4 to scrape links from a scrolling marquee. I'm able to get the marquee data, which is returned as a bs4 resultSet element. However, I cannot seem to access the href's within the data.
I'm sure I'm missing something as I'm new to web scraping, and appreciate any guidance anyone has.


Note: I can get the links easy peasy with selenium and chrome driver, but it takes forever.

---

This returns all of the marquee data:

```python
url = 'https://drugs.globalincidentmap.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

marquee = soup.select('div', class_='h-48') 
print(marquee)

```

---

However when I try to drill down further into the data, I get the empty list or `NoneType`/`KeyError` or `AttributeError`.

```
for a in marquee.find_all('a', href=True):
    link = a.find('div', class_=':nth-child')
```

or 

```
for a in marquee.find_all('a', href=True):
    link = a.find('div', class_='flex p-2')
```

Links in marquee

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-02): what does `print(marquee)` print for you? I'm getting nothing

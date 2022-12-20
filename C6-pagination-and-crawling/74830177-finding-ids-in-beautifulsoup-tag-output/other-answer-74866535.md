---
title: "Finding IDs in BeautifulSoup tag output"
site: stackoverflow
question_id: 74830177
answer_id: 74866535
url: https://stackoverflow.com/a/74866535
author: "Farid Mammadaliyev"
author_url: https://stackoverflow.com/users/10507476
posted: 2022-12-20T17:10:03Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 16f7bebf4e94045ca5ba11fcbe6e04926565a604b0cf4220887079382ff324bb
role: another answer on the same question, kept as context; not my work
---

# Answer by [Farid Mammadaliyev](https://stackoverflow.com/users/10507476) — 2022-12-20

Posted on Stack Overflow, <https://stackoverflow.com/a/74866535>, 2022-12-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I solved the problem. 

The problem was that the website is a dynamic website, therefore BeautifulSoup could not the data of the website correctly. I used Chromedriver before scraping with BeautifulSoup:

```
from selenium import webdriver
from selenium.webdriver import Chrome
drive = Chrome(executable_path =r"/Users/faridmammadaliyev/Desktop/chromedriver")
drive.get('https://www.immoweb.be/en/search/apartment/for-sale/Antwerp/2000?countries=BE&page=1&orderBy=relevance&card=10286959')
```

This launches a separate Chrome window that can be read by BeautifulSoup. Then, I used the following code:

```
soup = BeautifulSoup(drive.page_source, "lxml")
job_elements = soup.find_all(class_= "card__title-link") #"card__title card--result__title")

```
From the outcome (i.e., job_elements) I extracted the links of all listed items:

```
for a in soup.find_all('a', class_= "card__title-link", href=True):
    print("Found the URL_", a['href'])
```

I hope this helps those who are having trouble with scraping dynamic websites.

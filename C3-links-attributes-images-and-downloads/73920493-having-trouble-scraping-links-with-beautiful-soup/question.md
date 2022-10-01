---
title: "having trouble scraping links with beautiful soup"
site: stackoverflow
question_id: 73920493
url: https://stackoverflow.com/q/73920493
asked: 2022-10-01T17:43:01Z
asked_by: "sadie_b"
asked_by_url: https://stackoverflow.com/users/20138813
last_edited: 2022-10-02T05:15:45Z
last_editor: "Jakob F"
last_editor_url: https://stackoverflow.com/users/11327755
tags: [python, web-scraping, beautifulsoup, list-comprehension]
score: -1
views_at_snapshot: 114
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ec0632b8f7543775005e8ddbf8a35cd0c2c7c69499f29aaef0c547da67b6060d
---

# having trouble scraping links with beautiful soup

Asked by [sadie_b](https://stackoverflow.com/users/20138813) on Stack Overflow, <https://stackoverflow.com/q/73920493>, 2022-10-01, last edited 2022-10-02 by [Jakob F](https://stackoverflow.com/users/11327755). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Python student here, learning the basics of web scraping. Trying to pull the links from this bs4 element that I've scraped from a webpage.

```python
house = committee[0].find_all("li")
house
```
Result:

```lang-none
[<li><a href="/committee/house-agriculture/hsag00">Agriculture</a></li>,
<li><a href="/committee/house-appropriations/hsap00">Appropriations</a></li>,
<li><a href="/committee/house-armed-services/hsas00">Armed Services</a></li>,
<li><a href="/committee/house-budget/hsbu00">Budget</a></li>,
<li><a href="/committee/house-education-and-labor/hsed00">Education and ... ]
```

So when I try to pull out the links I'm using list comprehension:

```python
links_h = [link.get(" href")for link in house]
links_h
```
But instead of returning the links, it's returning this:

```python
[None,
None,
None,
None,
None]
```
Not sure if I need to do something different because these are internal links... I'm just kind of lost. Any help is appreciated.

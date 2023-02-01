---
title: "python scraping - How can I Loop between Dates in OddsPortal"
site: stackoverflow
question_id: 75292446
answer_id: 75305011
url: https://stackoverflow.com/a/75305011
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-01T02:14:54Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75305011/revisions
accepted: true
score: 2
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8371406b505f2420b9d699a3436b531479176fe8d8d623a25523a41199881c99
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75305011>, 2023-02-01; **accepted**; score 2. Text as retrieved 2026-10-12.

> ```python
>         span = soup.find('span', {'class': 'next-games-date'})
>         a_tags = span.findAll('a')
> ```

> ```python
>     a_tags = span.findAll('a')
> AttributeError: 'NoneType' object has no attribute 'findAll'
> ```

<sub>You can avoid raising the error by just checking for `None` like **`a_tags = [] if span is None else span.findAll('a')`** [this is something you should do habitually when with `.find`/`.select_one` btw], but you will always get an empty list, due to the reasons explained below.</sub> 

**Why** are you using `.find('span', {'class': 'next-games-date'})` when [as evident in the last screenshot in your q] the links are not contained in a `span` tag, and [as far as I could see from inspecting] there are no elements at all with the `next-games-date` class?? Considering this, it should not be surprising that `.find...` returned `None` and the next line raised the error.

---

Given that the screenshot of the inspect tab shows that one of the ancestor is a `div` with a `tabs` class, and that all the `a` tags have an `h-8` class, you could use something like 

```python
    if return_urls:
        a_cont = soup.find('div', {'class': 'tabs'})
        if a_cont is None: a_tags = [] # check for None to be safe
        else: a_tags =  a_cont.find_all('a', {'class':'h-8', 'href':True}) 
        urls = [
            'https://www.oddsportal.com'+a_tag['href'] for a_tag in a_tags
            if not a_tag['href'].startswith('#') # sections in current page 
            and 'active-item-calendar' not in a_tag['class'] # current page
        ]
```

or, with `.select`:

```python
    if return_urls:
        a_sel = 'div.tabs a.h-8:not([href^="#"]):not(.active-item-calendar)'
        urls = ['https://www.oddsportal.com'+a['href'] 
                for a in soup.select(a_sel)]
```

[Since you've already filtered out current page (which should be that day's) with *`'active-item-calendar' not in a_tag['class']`* or *`:not(.active-item-calendar)`*, there will be no need to `pop` any items...]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-02): The code works beautifully now Thank you for helping me understand scraping which is a lot more than I had before. However, can I please request a bit of change in the way the columns `date` and `game` are extracted? Date should be the title of the page while Game should be the teams without the score. [Please find the explanation for the desired values here](https://imgur.com/a/sT0JF8y)
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-02): Where would I add     `h1 = soup.find('h1').text     m = re.search(r'\d+ \w+ \d{4}$', h1)     game_date = m[0]` for `date` ? I dont know how I would go about getting the `game` col correctly though
- **me** (2023-02-02): @Rander since I feel like this is more relevant to your previous q about scraping this site, I've edited my definition of `generate_matches` there. The date is simple [and I just split by `,` since it felt simpler but if regex works betterr go with that], but the scores are coming from the `div...hidden` adjacent to each team name, so you have to get the teams separately and then join them if you want the `game` column without it.

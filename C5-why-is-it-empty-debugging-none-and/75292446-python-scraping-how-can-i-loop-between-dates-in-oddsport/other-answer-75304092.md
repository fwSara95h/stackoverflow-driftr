---
title: "python scraping - How can I Loop between Dates in OddsPortal"
site: stackoverflow
question_id: 75292446
answer_id: 75304092
url: https://stackoverflow.com/a/75304092
author: "Übermensch"
author_url: https://stackoverflow.com/users/13684789
posted: 2023-01-31T23:12:51Z
last_edited: 2023-02-01T01:59:20Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 294f3662ffbb0916f493964a1183955b89da400b61de923c0121959e7c74170c
role: another answer on the same question, kept as context; not my work
---

# Answer by [Übermensch](https://stackoverflow.com/users/13684789) — 2023-01-31

Posted on Stack Overflow, <https://stackoverflow.com/a/75304092>, 2023-01-31, last edited 2023-02-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The Traceback literally says where and why your code is erroring out. In the parse_data fnc, `soup.find('span', {'class': 'next-games-date'})` failed to find given class. As per [the BeautifulSoup documentation][1], "If find() can’t find anything, it returns None:", thus `span` is assigned NoneType obj. When the the following line-- `a_tags = span.findAll('a')`--is ran, an AtrributeError occurs because NoneType objects don't have a `findAll` method. 

There are 2 additional mistakes with code:<br>
1.) it should be `span.find_all('a)` not `span.findAll('a')` <br>
2.) There is no class attribute next-games-date (at least not that I could find) on the website.

  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find

For some reason the select method is not finding the `div` with class `.flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar`, but I was able to find it with the `find` method and make a list of urls. Heres the code:

```
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def get_page_source(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(3)
        return driver.page_source
    finally: driver.quit()

def grab_button_urls(html, tag, attr):
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find(tag, attr)\
        .find_all('a')
    return [f"https://www.oddsportal.com{tag['href']}" for tag in a_tags]

if __name__ == '__main__':
    website = 'https://www.oddsportal.com/matches/soccer'
    # get page source
    pg_html = get_page_source(website)
    # get urls from date buttons
    tag, class_attr = 'div', {'class':'flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar'}
    tags = grab_button_urls(pg_html, tag, class_attr)
    print(tags)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-31): You are correct. How can I correct that part of the code so that I get the code working again? [I am looking at this link](https://www.oddsportal.com/matches/soccer)
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-31): Thank you! I changed the part from `find_all` to `soup.select`. Got a new error that I dont know how to resolve lol
- **[Übermensch](https://stackoverflow.com/users/13684789)** (2023-01-31): What's the error?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-31): `urls.pop(1)  # Remove url for today: We already have the data for that IndexError: pop from empty list` Updated the code in the question
- **[Übermensch](https://stackoverflow.com/users/13684789)** (2023-01-31): Are you trying to collect all href values from the Yesterday, Today, ..., 07 Feb buttons?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-01): Yes.. Not just values but also the URLs as the dataframe loop will be cycling between those URLs
- **[Übermensch](https://stackoverflow.com/users/13684789)** (2023-02-01): pass `'.flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar a'` to the `select` method. That should return a list of all the child `a` tags of the `div` with `class='flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar'`.
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-01): Thank you, Where exactly in the code should I pass this?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-01): I tried `a_tags = soup.select('.flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar a')` as advised but I still get the same error `urls.pop(1)  # Remove url for today: We already have the data for that IndexError: pop from empty list` . Not sure if I am doing it the correct way as intended.
- **me** (2023-02-01): @Übermensch [about *"For some reason the `select` method is not finding the `div` with class ... but I was able to find it with the `find` "*] CSS selectors need a `.` before *every* class, so `div.flex.gap-2.py-3.overflow-x-auto.text-xs.no-scrollbar` [or maybe even `div[class="flex gap-2 py-3 overflow-x-auto text-xs no-scrollbar"]`] would probably have worked
- **[Übermensch](https://stackoverflow.com/users/13684789)** (2023-02-01): I guess I misunderstood the example in the BeautifulSoup documentation. I appreciate you taking the time to let me know.

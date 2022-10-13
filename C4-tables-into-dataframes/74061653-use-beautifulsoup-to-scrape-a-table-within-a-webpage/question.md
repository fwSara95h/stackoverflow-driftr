---
title: "Use beautifulsoup to scrape a table within a webpage?"
site: stackoverflow
question_id: 74061653
url: https://stackoverflow.com/q/74061653
asked: 2022-10-13T20:49:59Z
asked_by: "zemken12"
asked_by_url: https://stackoverflow.com/users/5157573
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 146
answer_count: 1
accepted_answer_id: 74090309
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2849732d9c75501099c0efbdfe1a003ec5318691f9f2d5d9d83bc29f0ce0c8a4
---

# Use beautifulsoup to scrape a table within a webpage?

Asked by [zemken12](https://stackoverflow.com/users/5157573) on Stack Overflow, <https://stackoverflow.com/q/74061653>, 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am scraping a county website that posts emergency calls and their locations. I have found success webscraping basic elements, but am having trouble scraping the rows of the table.  

(Here is an example of what I am working with codewise)

    location = list.find('div', class_='listing-search-item__sub-title')

Im not sure how to specifically webscrape the rows of the table. Can anyone explain how to dig into the sublevels of html to look for these records ? I'm not sure if I need to dig into tr, table, tbody, td, etc. Could use some guidance on which division or class to assign to dig into the data.

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/m1kWK.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Daraan](https://stackoverflow.com/users/12439683)** (2022-10-13): As a sidenote for tables you can also use [pandas.from_html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html) it sometimes needs some tweaking and filtering to get the correct table - often you get to much results but it often saves a lot of manual hassle of doing it with BS.
- **[eightlay](https://stackoverflow.com/users/13682080)** (2022-10-14): Give us the link to the site, please

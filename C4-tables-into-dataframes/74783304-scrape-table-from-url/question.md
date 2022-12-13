---
title: "Scrape table from url"
site: stackoverflow
question_id: 74783304
url: https://stackoverflow.com/q/74783304
asked: 2022-12-13T10:23:19Z
asked_by: "Raphael Hen"
asked_by_url: https://stackoverflow.com/users/10467327
last_edited: 2022-12-13T10:29:10Z
last_editor: "ScandinavianAvian"
last_editor_url: https://stackoverflow.com/users/295783
tags: [python, html, beautifulsoup]
score: 0
views_at_snapshot: 263
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d6e26a979b721cf7b7888061596a458486268c287f4dc9eb98a4cf3833a376cd
---

# Scrape table from url

Asked by [Raphael Hen](https://stackoverflow.com/users/10467327) on Stack Overflow, <https://stackoverflow.com/q/74783304>, 2022-12-13, last edited 2022-12-13 by [ScandinavianAvian](https://stackoverflow.com/users/295783). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape data from "https://www.investing.com/equities/pre-market" here the picture of what I need :[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/OBe27.png

    class="datatable_table__D_jso PreMarketMostActiveStocksTable_preMarketMostActiveStocksTable__9yGOv datatable_table--mobile-basic__W2ilt datatable_table--freeze-column__7YoIE"

It seems that this HTML code contains the table, I tried to scrape using 
`soup.find` but I get no result. 

here is my code.

    import requests
    from bs4 import BeautifulSoup
    url = "https://www.investing.com/equities/pre-market"
    html = requests.get(url).content
    
    soup = BeautifulSoup(html)
    
    table = soup.find('table', {'class': 'datatable_row__qHMpQ'})
    print(soup)

Thanks!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-12-13): Check your response you may run into a *Cloudflare* issue.
- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-13): What is a Cloudflare  issue?
- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-13): Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. In other words, you're not getting what you want because the site's protected by Cloudflare and they don't want you to scrape them.
- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-13): I see thanks for the answer. BTW how did you know this specific website has Cloudflare ?
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-12-13): As mentioned in the first comment - First at all check the response from the server, cause that is the base for your scraping - In this case it will give you following information *Why have I been blocked? This website is using a security service to protect itself from online attacks. The action you just performed triggered the security solution. There are several actions that could trigger this block including submitting a certain word or phrase, a SQL command or malformed data.*
- **[Lucas Fernandes](https://stackoverflow.com/users/1862049)** (2022-12-13): you can also use a Chrome Extension called Wappalyzer to check which tecnologies these websites are using (like cloudflare)

---
title: "bse result data scraping from bse site"
site: stackoverflow
question_id: 73414578
url: https://stackoverflow.com/q/73414578
asked: 2022-08-19T09:23:02Z
asked_by: "Hirak Dey"
asked_by_url: https://stackoverflow.com/users/8745560
last_edited: 2022-08-19T14:20:00Z
last_editor: "ljmc"
last_editor_url: https://stackoverflow.com/users/17676984
tags: [python, python-3.x, beautifulsoup]
score: 1
views_at_snapshot: 1740
answer_count: 1
accepted_answer_id: 75129525
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c13b6cc192fa72123c6e5100ddcddb49931f8ba05d06f8d770989d41f2486a8e
---

# bse result data scraping from bse site

Asked by [Hirak Dey](https://stackoverflow.com/users/8745560) on Stack Overflow, <https://stackoverflow.com/q/73414578>, 2022-08-19, last edited 2022-08-19 by [ljmc](https://stackoverflow.com/users/17676984). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

"https://www.bseindia.com/corporates/ann.html"

i need to scrap the filed heading of result data with bs4 and request

kindly help

    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.bseindia.com/corporates/ann.html"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 
    10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 
    Safari/537.36'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")

    div_list = soup.find_all('div', attrs={'class': 'row'})
    print(div_list)

please help me to extract the resultn news data

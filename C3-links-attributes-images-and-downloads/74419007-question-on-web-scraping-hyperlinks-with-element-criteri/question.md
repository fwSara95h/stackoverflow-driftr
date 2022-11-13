---
title: "Question on web-scraping hyperlinks with element criteria using python on tennisexplorer.com"
site: stackoverflow
question_id: 74419007
url: https://stackoverflow.com/q/74419007
asked: 2022-11-13T06:43:47Z
asked_by: "NewGuy1"
asked_by_url: https://stackoverflow.com/users/14745788
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 60
answer_count: 2
accepted_answer_id: 74419291
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0d72901cc6ab356dad90f4677ee4d1e4a87b99e6efb0961a5f4a3fa3c6063829
---

# Question on web-scraping hyperlinks with element criteria using python on tennisexplorer.com

Asked by [NewGuy1](https://stackoverflow.com/users/14745788) on Stack Overflow, <https://stackoverflow.com/q/74419007>, 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

The problem I have with the code below is it prints all of the a-href stuff, I want to know how to change it so that it only prints the hyperlinks found in "info" on the far right of the tables on the webpage "https://www.tennisexplorer.com/results/?type=atp-single&year=2022&month=09&day=08".

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    response = requests.get('https://www.tennisexplorer.com/results/?type=atp-single&year=2022&month=09&day=08')
    webpage = response.content
    soup = BeautifulSoup(response.text, "html.parser")

    col1 = [a.get('href') for a in soup.find_all('a')]

    print(pd.DataFrame({"MatchLink":col1}))

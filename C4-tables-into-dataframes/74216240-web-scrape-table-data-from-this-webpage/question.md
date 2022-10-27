---
title: "Web Scrape table data from this webpage"
site: stackoverflow
question_id: 74216240
url: https://stackoverflow.com/q/74216240
asked: 2022-10-27T02:49:10Z
asked_by: "John Provost"
asked_by_url: https://stackoverflow.com/users/7612063
last_edited: 2022-10-27T14:24:24Z
last_editor: "Andrew Ryan"
last_editor_url: https://stackoverflow.com/users/7451892
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 81
answer_count: 2
accepted_answer_id: 74217598
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aa1fbbf6fd9333c458c6bb517681068e983ae87736eb7c3bf4496c865979e86d
---

# Web Scrape table data from this webpage

Asked by [John Provost](https://stackoverflow.com/users/7612063) on Stack Overflow, <https://stackoverflow.com/q/74216240>, 2022-10-27, last edited 2022-10-27 by [Andrew Ryan](https://stackoverflow.com/users/7451892). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape the data from the table in the specifications section of this webpage:
[Lochinvar Water Heaters](https://www.lochinvar.com/products/commercial-water-heaters/armor-condensing-water-heater/)

I'm using beautiful soup 4. I've tried searching for it by class - for example - (class="Table__Cell-sc-1e0v68l-0 kdksLO") but bs4 can't find the class on the webpage. I listed all the available classes that it could find and it doesn't find anything useful. Any help is appreciated.

Here's the code I tried to get the classes


    import requests
    from bs4 import BeautifulSoup

    URL = "https://www.lochinvar.com/products/commercial-water-heaters/armor-condensing-water-heater"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_='Table__Wrapper-sc-1e0v68l-3 iFOFNW')

    classes = [value
               for element in soup.find_all(class_=True)
               for value in element["class"]]
    classes = sorted(classes)

    for cass in classes:
        print(cass)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrew Ryan](https://stackoverflow.com/users/7451892)** (2022-10-27): The reason why the data isn't there is that when using requests just looking at `page.content` there is no Table element -- this is likely because the content is being loaded in with javascript. Therefore you should use something like `selenium` to scrape the data you want.

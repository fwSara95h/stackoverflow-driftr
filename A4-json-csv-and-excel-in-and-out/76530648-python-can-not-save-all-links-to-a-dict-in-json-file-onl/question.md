---
title: "Python: can not save all links to a dict in json file, only the last one"
site: stackoverflow
question_id: 76530648
url: https://stackoverflow.com/q/76530648
asked: 2023-06-22T09:51:15Z
asked_by: "Alberi"
asked_by_url: https://stackoverflow.com/users/19319195
last_edited: never
tags: [python, json, loops, dictionary]
score: 0
views_at_snapshot: 58
answer_count: 3
accepted_answer_id: 76530736
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e56b918ae51680b95e3a99bb2cfbaa56bb0355e99cb54bfdf913fce4a8158525
---

# Python: can not save all links to a dict in json file, only the last one

Asked by [Alberi](https://stackoverflow.com/users/19319195) on Stack Overflow, <https://stackoverflow.com/q/76530648>, 2023-06-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I wrote this code in python to get all the links and to put them in a json file, but for some reason i am only getting the last link (website and class see in the code). Any ideas, why is it not working properly?


```
import requests
from bs4 import BeautifulSoup
import json

headers = {
>     "Accept": "*/*",
>     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0Safari/537.36"
> }

number = 0

for page_number in range(1, 2):
    url = f"https://www.sothebysrealty.com/eng/associates/int/{page_number}-pg"
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    name_link = soup.find_all("a", class_="Entities-card__cta btn u-text-uppercase u-color-sir-blue palm--hide")

    all_links_dict = {}
    for item in name_link:
        value_links = ("https://www.sothebysrealty.com" + item.get("href"))

    all_links_dict[number + 1] = value_links

    with open("all_links_dict.json", "w", encoding="utf-8-sig") as file:
    json.dump(all_links_dict, file, indent=4, ensure_ascii=False)
```

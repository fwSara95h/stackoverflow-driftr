---
title: "Webscrapping with bs4: Type Error - 'NoneType' object is not subscriptable"
site: stackoverflow
question_id: 73913131
url: https://stackoverflow.com/q/73913131
asked: 2022-09-30T19:16:06Z
asked_by: "Suikurix"
asked_by_url: https://stackoverflow.com/users/16294668
last_edited: never
tags: [python, beautifulsoup, request, typeerror, nonetype]
score: -1
views_at_snapshot: 458
answer_count: 1
accepted_answer_id: 73913602
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: eaa22d269986aef814f045477c828534053325169605a9335b8b8c13230ad137
---

# Webscrapping with bs4: Type Error - 'NoneType' object is not subscriptable

Asked by [Suikurix](https://stackoverflow.com/users/16294668) on Stack Overflow, <https://stackoverflow.com/q/73913131>, 2022-09-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to extract "video" from the url and print how many there are in the console. 

But I get this Error:

```TypeError: 'NoneType' object is not subscriptable```

Here is my code:
```
import requests
from bs4 import BeautifulSoup

Web_url = "https://watch.plex.tv/show/hannibal/season/1/episode/9"
r = requests.get(Web_url)

soup = BeautifulSoup(r.content, 'html.parser')

video_tags = soup.find_all("video")
print("Total", len(video_tags), "videos found")

if len(video_tags) !=0:
    for video_tag in video_tags:
        video_url = video_tag.find("a")['href']
        print(video_url)```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Md. Fazlul Hoque](https://stackoverflow.com/users/12848411)** (2022-09-30): At first,you have to specify what data do you wanna scrape?
- **[Md. Fazlul Hoque](https://stackoverflow.com/users/12848411)** (2022-09-30): Is "video" is class name or attr. Thus way can't grab anything

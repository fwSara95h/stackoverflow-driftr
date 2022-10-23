---
title: "Receiving garbled text when attempting to scrape a certain website with Python using bs4"
site: stackoverflow
question_id: 74171187
url: https://stackoverflow.com/q/74171187
asked: 2022-10-23T12:36:24Z
asked_by: "Aaron Vegoda"
asked_by_url: https://stackoverflow.com/users/16793850
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 97
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: deb7985deda25dd7cdfc8ee1ed3789f4f7080581aafb8b378cef03665dd7e500
---

# Receiving garbled text when attempting to scrape a certain website with Python using bs4

Asked by [Aaron Vegoda](https://stackoverflow.com/users/16793850) on Stack Overflow, <https://stackoverflow.com/q/74171187>, 2022-10-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When attempting to scrape [this website][1] (TakeAlot) instead of getting normal html output I am instead receiving a little html but mostly garbled text.

Here is what I am receiving:

[![here is what I am receiving:][2]][2]

And here is my code:

    from bs4 import BeautifulSoup
    import requests
    
    htmlSource = (requests. Get(
        "https://www.takealot.com/?gclid=CjwKCAjwzNOaBhAcEiwAD7Tb6AhZbkyxR6ewJSUswC- 
         GGcilxY3D10zvFd4repwE3SGZDbVn7U6q4RoC5cwQAvD_BwE&gclsrc=aw.ds"
    )).text
    soup = BeautifulSoup(htmlSource, "html.parser")
    print(soup)

I'm unsure as to whether I am doing something wrong, or maybe this website somehow blocks scraping?

Either way I would really appreciate any help as to what the issue is. Thanks in advance

  [1]: https://www.takealot.com/?gclid=CjwKCAjwzNOaBhAcEiwAD7Tb6AhZbkyxR6ewJSUswC-GGcilxY3D10zvFd4repwE3SGZDbVn7U6q4RoC5cwQAvD_BwE&gclsrc=aw.ds
  [2]: https://i.sstatic.net/i39dl.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sharuzzaman Ahmat Raslan](https://stackoverflow.com/users/776988)** (2022-10-23): that is not a garbled text. that is an image encoded in base64

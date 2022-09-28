---
title: "how to get source of img tags inside a web link with beautiful soup 4"
site: stackoverflow
question_id: 73887038
url: https://stackoverflow.com/q/73887038
asked: 2022-09-28T19:48:06Z
asked_by: "Moon"
asked_by_url: https://stackoverflow.com/users/14873033
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 231
answer_count: 2
accepted_answer_id: 73887424
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 688c3bce194a5b2ceed6191e4c6418facc578799a6e20db1cdf114d5f832caa0
---

# how to get source of img tags inside a web link with beautiful soup 4

Asked by [Moon](https://stackoverflow.com/users/14873033) on Stack Overflow, <https://stackoverflow.com/q/73887038>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I`m trying to get the src link of img tags inside a website and print them in console

    from bs4 import BeautifulSoup
    import requests

    r = requests.get("https://welovemanga.one/2777/92578/")
    soup = BeautifulSoup(r.content, "html.parser")
    thumbnail_elements = soup.find_all("img", class_ = "chapter-img")
  
    for element in thumbnail_elements:
        print(element['src'])

the images in this website has a class "chapter-img" with each having its own src link, which is what I want. 

 [![enter image description here][1]][1]


But when I run the code, it returns this for each image in the link:

[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/i6Auh.png
  [2]: https://i.sstatic.net/aCOJw.png

How can I get only the src of the img tags insted of lazy_loading.gif ?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Iain Shelvington](https://stackoverflow.com/users/548562)** (2022-09-28): The src of the img tags is being changed by some JS after the page has loaded, the source does not contain the updated values. You'll need to use some kind of browser driver/emulator to scrape the site instead, Selenium is a popular choice

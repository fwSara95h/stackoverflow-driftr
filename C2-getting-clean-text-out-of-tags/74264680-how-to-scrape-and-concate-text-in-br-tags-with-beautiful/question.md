---
title: "How to scrape and concate text in <br> tags with Beautiful Soup"
site: stackoverflow
question_id: 74264680
url: https://stackoverflow.com/q/74264680
asked: 2022-10-31T14:18:11Z
asked_by: "Benedikt Faude"
asked_by_url: https://stackoverflow.com/users/19809547
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 88
answer_count: 4
accepted_answer_id: 74277990
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a4fc306049ff079746278ceea80a63967adcfabefc8e629cdce356fb3822e8bf
---

# How to scrape and concate text in <br> tags with Beautiful Soup

Asked by [Benedikt Faude](https://stackoverflow.com/users/19809547) on Stack Overflow, <https://stackoverflow.com/q/74264680>, 2022-10-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape parts of this site:

<https://www.booklooker.de/B%C3%BCcher/Bastian-Sick+Der-Dativ-ist-dem-Genitiv-sein-Tod-Ein-Wegweiser-durch-den-Irrgarten-der-deutschen/id/A02ArCkS01ZZy>

More accurate this part:
[![enter image description here][1]][1]


The html looks like this:
[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/jU4ul.png
  [2]: https://i.sstatic.net/kU6Mq.png

I tried this, but it doesn`t work: 

       from bs4 import BeautifulSoup
        import requests
        page = requests.get("https://www.booklooker.de/Bücher/Bastian-Sick+Der-Dativ-ist-dem-Genitiv-sein-Tod-Ein-Wegweiser-durch-den-Irrgarten-der-deutschen/id/A02ArCkS01ZZy")
        
    souped = BeautifulSoup(page.content, "html.parser")
    description = souped.find(class_="propertyItem_13").find_all("br").text

But that doesn`t work. Do you have any idea, how it is possible to scrape all the text?

Thanks in advance!!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Konrad Rudolph](https://stackoverflow.com/users/1968)** (2022-10-31): The `<br>` tag *never* has text content, it's a self-closing (= empty) tag.

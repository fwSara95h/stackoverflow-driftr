---
title: "How to get all results at once?"
site: stackoverflow
question_id: 76545668
url: https://stackoverflow.com/q/76545668
asked: 2023-06-24T10:44:53Z
asked_by: "Anish Thapa"
asked_by_url: https://stackoverflow.com/users/22108493
last_edited: 2023-06-24T10:47:23Z
last_editor: "quamrana"
last_editor_url: https://stackoverflow.com/users/4834
tags: [python, web-scraping, beautifulsoup, request]
score: 0
views_at_snapshot: 67
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 584d3c1dd3ac01867ef43d5d2d15943404631ac1ba89922277426367365bcd57
---

# How to get all results at once?

Asked by [Anish Thapa](https://stackoverflow.com/users/22108493) on Stack Overflow, <https://stackoverflow.com/q/76545668>, 2023-06-24, last edited 2023-06-24 by [quamrana](https://stackoverflow.com/users/4834). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

What am I doing wrong? It shows KeyError: 'One'?  I want to have output in a list displaying:
```
title:""
price:""
rating:""
```

    import requests as r
    from bs4 import BeautifulSoup
    import re
    from random import choice
    
    url = r.get("https://books.toscrape.com/")
    resp = url.content
    soup = BeautifulSoup(resp,"html.parser")
    
    def clean_price(price):
       return float (re.sub("[^0-9.]", " ", price))
    
    def map_rating(rating):
     rating_map = {
        "one": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
     }
     return rating_map[rating]
    
    def extract_book_data (book_tag):
     title = book_tag.find("h3").find("a")["title"]
     price = book_tag.find("p",attrs={"class":"price_color"}).get_text()
     rating = book_tag.find("p",attrs={"class":"star-rating"})["class"][-1]
     return {
        "title": title,
        "price": clean_price(price),
        "rating": map_rating(rating)
     }
    book_tags = soup.find_all("article", attrs={"class":"product_pod"})
    book_data = [extract_book_data(book_tag) for book_tag in book_tags]
    
     print(book_data)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[quamrana](https://stackoverflow.com/users/4834)** (2023-06-24): Please update your question with the full error traceback.
- **[ouroboros1](https://stackoverflow.com/users/18470692)** (2023-06-24): It's a typo. You want to change the key `"one"` to `"One"` inside `rating_map`.
- **[Anish Thapa](https://stackoverflow.com/users/22108493)** (2023-06-24): @ouroboros1 Yes. That was the problem and finally it's solved thank you so much i have started recently and i was stucked for days i was trying every solution and from here i will keep in mind for such things.
- **[ouroboros1](https://stackoverflow.com/users/18470692)** (2023-06-24): You're welcome. One of the most important things is to invest in understanding what a `full error traceback` is telling you. In your case, it will have ended by saying that it failed to execute `return rating_map[rating]`, namely because "One" (stored inside `rating`) does not exist as a `key` in the dictionary `rating_map` (`KeyError: 'One'`). When you look at this dict, indeed, you can see right away that there's a typo. Good luck with your project!

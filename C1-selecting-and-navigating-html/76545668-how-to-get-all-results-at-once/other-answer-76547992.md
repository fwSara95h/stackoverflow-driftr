---
title: "How to get all results at once?"
site: stackoverflow
question_id: 76545668
answer_id: 76547992
url: https://stackoverflow.com/a/76547992
author: "Ahmad Abdelbaset"
author_url: https://stackoverflow.com/users/7987455
posted: 2023-06-24T21:04:58Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e14269abcda93d2056061f59466dd9fa96a80ba64d588f37732ff909da9f1110
role: another answer on the same question, kept as context; not my work
---

# Answer by [Ahmad Abdelbaset](https://stackoverflow.com/users/7987455) — 2023-06-24

Posted on Stack Overflow, <https://stackoverflow.com/a/76547992>, 2023-06-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The ```print(book_data)``` statement was indented incorrectly. It should be aligned with the previous line ```book_data = [extract_book_data(book_tag) for book_tag in book_tags]```.


Your code, will be: 

```
import requests as r
from bs4 import BeautifulSoup
import re
from random import choice

url = r.get("https://books.toscrape.com/")
resp = url.content
soup = BeautifulSoup(resp, "html.parser")

def clean_price(price):
    return float(re.sub("[^0-9.]", " ", price))

def map_rating(rating):
    rating_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    return rating_map[rating.lower()]

def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]
    return {
        "title": title,
        "price": clean_price(price),
        "rating": map_rating(rating)
    }

book_tags = soup.find_all("article", attrs={"class": "product_pod"})
book_data = [extract_book_data(book_tag) for book_tag in book_tags]

print(book_data)

```

Please note that in the ```map_rating``` function, the rating is converted to lowercase using ```rating.lower()``` to handle case sensitivity.

---
title: "How do I combine elements from two loops without issues?"
site: stackoverflow
question_id: 74631667
url: https://stackoverflow.com/q/74631667
asked: 2022-11-30T17:12:27Z
asked_by: "Magicskid"
asked_by_url: https://stackoverflow.com/users/3341926
last_edited: 2022-11-30T18:42:16Z
tags: [python, loops, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 48
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fb13cb3e20a77bd88c4996d9da4213bdbba9ee09f871e2d1066f186bc6beed62
---

# How do I combine elements from two loops without issues?

Asked by [Magicskid](https://stackoverflow.com/users/3341926) on Stack Overflow, <https://stackoverflow.com/q/74631667>, 2022-11-30, last edited 2022-11-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When I execute this code...

```py
from bs4 import BeautifulSoup

with open("games.html", "r") as page:
    doc = BeautifulSoup(page, "html.parser")

titles = doc.select("a.title")
prices = doc.select("span.price-inner")

for game_soup in doc.find_all("div", {"class": "game-options-wrapper"}):
    game_ids = (game_soup.button.get("data-game-id"))

for title, price_official, price_lowest in zip(titles, prices[::2], prices[1::2]):
    print(title.text + ',' + str(price_official.text.replace('$', '').replace('~', '')) + ',' + str(
        price_lowest.text.replace('$', '').replace('~', '')))
```

The output is...
```py
153356
80011
130187
119003
73502
156474
96592
154207
155123
152790
165013
110837
Call of Duty: Modern Warfare II (2022),69.99,77.05
Red Dead Redemption 2,14.85,13.79
God of War,28.12,22.03
ELDEN RING,50.36,48.10
Cyberpunk 2077,29.99,28.63
EA SPORTS FIFA 23,41.99,39.04
Warhammer 40,000: Darktide,39.99,45.86
Marvels Spider-Man Remastered,30.71,27.07
Persona 5 Royal,37.79,43.32
The Callisto Protocol,59.99,69.41
Need for Speed Unbound,69.99,42.29
Days Gone,15.00,9.01

```
But I'm trying to get the value next to the other ones on the same line

Expected output:
```py
Call of Duty: Modern Warfare II (2022),69.99,77.05,153356
Red Dead Redemption 2,14.85,13.79,80011
...
```
Even when adding `game_ids` to `print()`, it spams the same game id for each line.

How can I go about resolving this issue?

HTML file: https://jsfiddle.net/m3hqy54x/

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sarah Messer](https://stackoverflow.com/users/2112722)** (2022-11-30): loop over all elements in the doc and use an "if..elif..." block to figure out whether you should be updating `game_id` or `title`.  But you're probably not going to end up with a single loop so much as various conditionals and nested loops.  Maybe a few variables as well, depending on what you're trying to scrape.
- **[Magicskid](https://stackoverflow.com/users/3341926)** (2022-11-30): I need to run them together, not one or the other
- **me** (2022-11-30): is `110837\nCall of Duty: Modern Warfare II (2022)` from one title?

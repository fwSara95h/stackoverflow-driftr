---
title: "How to create proper formatted JSON file with BeautifulSoup scraped information?"
site: stackoverflow
question_id: 74682012
url: https://stackoverflow.com/q/74682012
asked: 2022-12-04T23:50:20Z
asked_by: "Ryan"
asked_by_url: https://stackoverflow.com/users/20668904
last_edited: 2022-12-04T23:51:52Z
tags: [python, for-loop, beautifulsoup]
score: 0
views_at_snapshot: 46
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 31c737198845f3f6e514a0bf66ff7af83e2358fcf5e8a36f095b173319279920
---

# How to create proper formatted JSON file with BeautifulSoup scraped information?

Asked by [Ryan](https://stackoverflow.com/users/20668904) on Stack Overflow, <https://stackoverflow.com/q/74682012>, 2022-12-04, last edited 2022-12-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When I run this script...
```
from bs4 import BeautifulSoup
import requests
import json

url = "https://stock.adobe.com/search?k=interstellar%20movie"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")

jfile = open('images.json', 'w')

title = soup.find('em', class_='gravel-text').text

for images in soup.find_all('div', class_='thumb-frame'):
    image = images.a['href']

    j = [{'title':title, 'image':image}]

    jstring = json.dumps(j)

    jfile.write(jstring)

jfile.close()

```
The problem that I'm having is that it creates multiple root elements with the title within every element.

Formatted output...
```
[
   {
      "title":"interstellar movie",
      "image":"https://stock.adobe.com/images/gargantua-galaxy-design-graphic-3d-illustration-red-wormhole-or-black-hole-shine-in-space-inspiration-from-interstellar-movie-night-sky-background/90184980"
   }
][
   {
      "title":"interstellar movie",
      "image":"https://stock.adobe.com/images/wanderlust-explorer-discovering-icelandic-natural-wonders/395993532"
   }
][
   {
      "title":"interstellar movie",
      "image":"https://stock.adobe.com/images/panoramic-beautiful-night-sky-and-star-abstract-background-elements-of-this-image-furnished-by-nasa/223412156"
   }
]
```

I've tried moving the j variable outside the loop and writing the title, but can't seem to figure out how to combine the looped variable with the other one. I'm trying to output the title only once with the list of links so the output becomes as such...
```
[{
    "title": "interstellar movie", 
    "image": [
        "https://stock.adobe.com/images/gargantua-galaxy-design-graphic-3d-illustration-red-wormhole-or-black-hole-shine-in-space-inspiration-from-interstellar-movie-night-sky-background/90184980",
        "https://stock.adobe.com/images/wanderlust-explorer-discovering-icelandic-natural-wonders/395993532",
        "https://stock.adobe.com/images/panoramic-beautiful-night-sky-and-star-abstract-background-elements-of-this-image-furnished-by-nasa/223412156"
    ]
}]
```
Thanks in advance :)

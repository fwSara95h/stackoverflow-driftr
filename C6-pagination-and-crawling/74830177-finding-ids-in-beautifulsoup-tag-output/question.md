---
title: "Finding IDs in BeautifulSoup tag output"
site: stackoverflow
question_id: 74830177
url: https://stackoverflow.com/q/74830177
asked: 2022-12-16T22:03:48Z
asked_by: "Farid Mammadaliyev"
asked_by_url: https://stackoverflow.com/users/10507476
last_edited: 2022-12-19T14:49:20Z
tags: [python, beautifulsoup]
score: -2
views_at_snapshot: 69
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e0dfd9601ed8fc31ecc4d9f239a480c6942c1c8b1a9dd41c3af65a99523578b
---

# Finding IDs in BeautifulSoup tag output

Asked by [Farid Mammadaliyev](https://stackoverflow.com/users/10507476) on Stack Overflow, <https://stackoverflow.com/q/74830177>, 2022-12-16, last edited 2022-12-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape a website using BeautifulSoup. I first search on the website. My intention is to extract the IDs of items in the search. Then, I will use these IDs to go to the page of each resulting item and scrape data. The code I use is below:

```import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.immoweb.be/en/search/apartment/for-sale/Antwerp/2000?countries=BE&page=1&orderBy=relevance&card=10286959"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id= "search-app")
 ```

Normally, as a next step, I have to the use find_all function to go to the class where unique IDs are stored. However, in the "results" above, there are no class names. I can still see IDs in the text. How can I extract those IDs?

Here is the result:

[![enter image description here][1]][1]

Thank you in advance. 


  [1]: https://i.sstatic.net/9LkOx.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-17): please explain more about what how you *"can still see IDs in the text"*, preferably with a snippet or screenshot. On browser, the `article` tags with `id="classified_..."` also have `class="card card--result card--xl"` - if you're seeing something different with requests+bs4 and the ids are still there, there's most likely some way to extract them, but we can't help you unless you include at least a sample of the data/`results` you have so far....
- **[Akilan Manivannan](https://stackoverflow.com/users/14970007)** (2022-12-18): It looks like `search-app` is just a parent ID and doesn't hold any content. Instead, you might want to filter for every `article` tag on the site, that seems to have what you want.
- **[Farid Mammadaliyev](https://stackoverflow.com/users/10507476)** (2022-12-19): I added the result.

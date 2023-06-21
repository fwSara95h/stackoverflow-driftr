---
title: "How do I add user input to url in python?"
site: stackoverflow
question_id: 76519157
url: https://stackoverflow.com/q/76519157
asked: 2023-06-21T00:21:10Z
asked_by: "Dan"
asked_by_url: https://stackoverflow.com/users/22105569
last_edited: never
tags: [python, web-scraping, url, beautifulsoup]
score: -1
views_at_snapshot: 664
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 01c3a7cf996bbe0f369770ed09854fc34a183ed577c9013f79bed40c8bc49c9e
---

# How do I add user input to url in python?

Asked by [Dan](https://stackoverflow.com/users/22105569) on Stack Overflow, <https://stackoverflow.com/q/76519157>, 2023-06-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

everyone! I'm a new user of python and I'm trying to figure out this issue for my final class project. I've done research online, so I know I'm on the right track, I just don't know what I'm doing wrong.

I want to scrape the links from a subtitle website (indexsubtitle) for my group class project. This is what I have so far:

```
import requests
from bs4 import BeautifulSoup

find_movie = input('Type name of the movie you want subtitles for: \n')

subs_url = 'https://indexsubtitle.com/'+find_movie
html_text = requests.get(subs_url).text
subs_soup = BeautifulSoup(html_text, 'html.parser')

for link in subs_soup.find_all('a'):
    print(link.get('href'))
```
Without the user input bit (and just using the original url with the info I would ask the user- for example "matilda"), running the program shows all the links just fine. But, when asking the user to input the information ("matilda"), the program runs and ends without any links at all.

Please let me know if I'm going about asking this question wrong, or if you need any more clarifying information, as it's my first time asking a question on this website! I asked my prof about my idea for this and she said it was possible.

Using past questions on this website, I've also tried using 
`subs_url = 'https://indexsubtitle.com/{}'.format(find_movie)` and `subs_url = f'https://indexsubtitle.com/{find_movie}'`, but neither did anything different.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Amadan](https://stackoverflow.com/users/240443)** (2023-06-21): The URL `https://indexsubtitle.com/matilda` does not return any useful information. Please check if you are indeed using the same URL in your two scenarios (and not e.g. `https://indexsubtitle.com/subtitles/matilda/`). Also, that particular webpage (and many others on Cloudflare) seems to be doing some sort of human check on new connections, and not serving the desired content on the first access.
- **[Dan](https://stackoverflow.com/users/22105569)** (2023-06-21): @Amadan ohhh, you're right! i feel like an idiot for getting the url wrong. ok, thank you so much! idk how i missed that!

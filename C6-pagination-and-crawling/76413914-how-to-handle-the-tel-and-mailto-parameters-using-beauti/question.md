---
title: "How to handle the \"tel:\" and \"mailto:\" parameters using BeautifulSoup4?"
site: stackoverflow
question_id: 76413914
url: https://stackoverflow.com/q/76413914
asked: 2023-06-06T10:55:17Z
asked_by: "yuji09"
asked_by_url: https://stackoverflow.com/users/22029363
last_edited: never
tags: [python, python-3.x, beautifulsoup, web-crawler]
score: 0
views_at_snapshot: 136
answer_count: 1
accepted_answer_id: 76414759
closed: 2023-06-06T13:17:55Z (Not suitable for this site)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bd865ec0186a9cfb3584936af4c8561496dec0d722628038b6024871a502e324
---

# How to handle the "tel:" and "mailto:" parameters using BeautifulSoup4?

Asked by [yuji09](https://stackoverflow.com/users/22029363) on Stack Overflow, <https://stackoverflow.com/q/76413914>, 2023-06-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I was creating a small script to crawl website of mine. This script will crawl to the website and will check if the page is broken or not based on their status code. Also, the crawler also will check if the URL have a certain word on it. The thing is, the website have this "tel:" thingies that indicate a phone number, and also "mailto:".

I've tried to add a couple if conditions to handle this sort of things.

But I'm always stuck with the error:
`InvalidSchema: No connection adapters were found for 'tel:0412345678`

Here is the snipped of my code:

```
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def check_url(url):
    if url.startswith(('http://', 'https://')):
        response = requests.get(url)
        return response.status_code
    else:
        return None  # Skip unsupported schemes

def extract_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            parsed_url = urlparse(url)
            if parsed_url.scheme != '' and parsed_url.scheme != 'tel:':
                absolute_url = urljoin(url, href)
                urls.append(absolute_url)

    return urls

def crawl(url, word):
    visited = set()
    dead_pages = set()

    def crawl_helper(url, word):  # Add the 'word' parameter
        if url in visited:
            return
        visited.add(url)

        status_code = check_url(url)
        if status_code == 404:
            dead_pages.add(url)

        if word in url:
            print(f'URL "{url}" contains "{word}".')

        urls = extract_url(url)
        for u in urls:
            crawl_helper(u, word)  # Pass the 'word' parameter

    crawl_helper(url, word)  # Pass the 'word' parameter

    return dead_pages

starting_url = 'https://google.com' # this is just a placeholder
word_to_search = 'test' # this is also a placeholder
dead_pages = crawl(starting_url, word_to_search)

for page in dead_pages:
    print(f'Dead page: {page}')```

I'm still new to BeautifulSoup but eager to learn.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[0stone0](https://stackoverflow.com/users/5625547)** (2023-06-06): What are you trying to do? Parse the phone number?
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2023-06-06): is this website publicly accessible? if so, what's the url?
- **[Luke](https://stackoverflow.com/users/9034824)** (2023-06-06): Have you tried to `print(parsed_url.scheme)`? I've got a feeling that it may not have the `:` on the end and you should be comparing `if parsed_url.scheme != '' and parsed_url.scheme != 'tel':`, but I'm not 100%
- **[yuji09](https://stackoverflow.com/users/22029363)** (2023-06-06): @barry Unfortunately, the website is not publicly accessible. @0stone0 What I'm trying to do is to check all of the URLs on the site,making sure there are no 404 page, but skip any URLs that don't begin with `http://` and/or `https://` @luke I'm not sure either but I'll have a go at it. Thank you.

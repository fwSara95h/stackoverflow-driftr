---
title: "How to use \"for\" to \"loop\" multiple urls while webscraping?"
site: stackoverflow
question_id: 75121723
url: https://stackoverflow.com/q/75121723
asked: 2023-01-14T22:37:35Z
asked_by: "nesqluck"
asked_by_url: https://stackoverflow.com/users/21009472
last_edited: 2023-02-05T22:39:55Z
tags: [python, json, loops, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 84
answer_count: 1
accepted_answer_id: 75123779
closed: 2023-01-15T08:33:10Z (Needs more focus)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f591d83a2b0a21b073d7c84edd8752e39bc78000939a7c7aefae2c3666dcea91
---

# How to use "for" to "loop" multiple urls while webscraping?

Asked by [nesqluck](https://stackoverflow.com/users/21009472) on Stack Overflow, <https://stackoverflow.com/q/75121723>, 2023-01-14, last edited 2023-02-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

The current code is perfect to scrape the information for only one Url, and i would like to be able to scrape from multiple urls at once ( maybe use For url in Urls ) ,Here is the current code for just one url below. Please any help or direction would be appreciated

```
import datetime
from bs4 import BeautifulSoup
import requests

def get_url_data_from_url_request(url):
 print(">> get_url_data_from_url_request: "+str(url))
 url_data = None
 headers = {"user-agent": "Mozilla/5.0 (Windows NT 
 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like 
 Gecko) Chrome/90.0.4430.93 Safari/537.36"}
 s = requests.session()
 s.keep_alive = False
 request = s.get(url, proxies=None, headers=headers)
 print("request.status_code: ", request.status_code )
 url_data = request.text
 request.connection.close()
 s.close()
 return url_data

def main():
 print("bdr.sandbox")
 generated_on = datetime.datetime.now()
 print(generated_on)
 source_product_url = ""
 url_data = get_url_data_from_url_request(url=source_product_url)
 soup = BeautifulSoup(url_data, "lxml")
 id_element = soup.find('span', {"itemprop": "sku"}).text
 print(id_element)
 
if __name__ == '__main__':
main()
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[sudden_appearance](https://stackoverflow.com/users/14882395)** (2023-01-14): So what's the problem using forloop?
- **[baduker](https://stackoverflow.com/users/6106791)** (2023-01-14): Please read [Python For Loop Tutorial](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2023-01-15): Welcome to Stack Overflow. It's hard to understand the question, because it's not clear **why there is a problem**. For example, do you know how to use a `for` loop **for other things**? If so, then why is it a problem to use it for this task? If you don't know, then - how did you know, in the first place, that there is such a thing as a `for` loop? Because you read it somewhere, right? Did you try going back there, and reading some more, to understand how to use it?

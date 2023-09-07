---
title: "Webcrawler for Testing und learn"
site: stackoverflow
question_id: 77060537
url: https://stackoverflow.com/q/77060537
asked: 2023-09-07T14:32:43Z
asked_by: "D1skanime"
asked_by_url: https://stackoverflow.com/users/18557168
last_edited: 2023-09-07T14:34:37Z
tags: [python, beautifulsoup, web-crawler]
score: 0
views_at_snapshot: 56
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 490a0fe7d4b936c41ed913f32343c596627388914d2fae8e80307336e40b7be3
---

# Webcrawler for Testing und learn

Asked by [D1skanime](https://stackoverflow.com/users/18557168) on Stack Overflow, <https://stackoverflow.com/q/77060537>, 2023-09-07, last edited 2023-09-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Hi I wanted to try to program a crawler.

I started with a very simple code but already when I execute it I get an error message.

What is wrong with the code?

I geht this Error at the source point.

```
Exception has occurred: ConnectTimeout
HTTPSConnectionPool(host='www.anisearch.de', port=443): Max retries exceeded with url: /anime/2788,naruto (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000002757873E090>, 'Connection to www.anisearch.de timed out. (connect timeout=None)'))
TimeoutError: [WinError 10060] Ein Verbindungsversuch ist fehlgeschlagen, da die Gegenstelle nach einer bestimmten Zeitspanne nicht richtig reagiert hat, oder die hergestellte Verbindung war fehlerhaft, da der verbundene Host nicht reagiert hat

The above exception was the direct cause of the following exception:

urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x000002757873E090>, 'Connection to www.anisearch.de timed out. (connect timeout=None)')

The above exception was the direct cause of the following exception:

urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.anisearch.de', port=443): Max retries exceeded with url: /anime/2788,naruto (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000002757873E090>, 'Connection to www.anisearch.de timed out. (connect timeout=None)'))

During handling of the above exception, another exception occurred:

  File "C:\Users\admin\Documents\Crawler\anisearch_crawler.py", line 5, in <module>
    source = requests.get(url)
             ^^^^^^^^^^^^^^^^^
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='www.anisearch.de', port=443): Max retries exceeded with url: /anime/2788,naruto (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000002757873E090>, 'Connection to www.anisearch.de timed out. (connect timeout=None)'))
```

It is clear to me that he cannot reach the page, but I do not understand why.
Here my Easy Code

```
`from bs4 import BeautifulSoup
import requests

url = "https://www.anisearch.de/anime/2788,naruto"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'html.parser')

def info_anime(soup):
    # Extracting the name of the anime from the <meta> tag
    anime_name = soup.find('meta', {'name': 'title'})['content']
    print("Anime : " + anime_name)


info_anime(soup)`
```

debug with vs code but i am not really unterstood in what case are the problem. It say "can not request" but why and how i solfe this problem that i can geht this information back.

The site has no api so i try with this methode

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[rasjani](https://stackoverflow.com/users/108538)** (2023-09-07): either the site is/was down or they have blocked your IP address when they detected you tried to scrape the site.
- **[D1skanime](https://stackoverflow.com/users/18557168)** (2023-09-08): What is the solution against theme? I have only made a request nothing more.

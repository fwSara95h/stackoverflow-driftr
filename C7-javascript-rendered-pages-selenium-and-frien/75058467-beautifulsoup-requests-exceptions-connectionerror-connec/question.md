---
title: "Beautifulsoup: requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response"
site: stackoverflow
question_id: 75058467
url: https://stackoverflow.com/q/75058467
asked: 2023-01-09T14:08:34Z
asked_by: "Irra"
asked_by_url: https://stackoverflow.com/users/19689942
last_edited: never
tags: [python, web-scraping, web, beautifulsoup]
score: 0
views_at_snapshot: 1296
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ce1c0543deadcf25163194c7fc95f024e650a8fb80cd9b2d2b42104256aed57
---

# Beautifulsoup: requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response

Asked by [Irra](https://stackoverflow.com/users/19689942) on Stack Overflow, <https://stackoverflow.com/q/75058467>, 2023-01-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to build a python webscraper with beautifulsoup4. If I run the code on my Macbook the script works, but if I let the script run on my homeserver (ubuntu vm) I get the following error msg (see below). I tried a vpn connection and multiple headers without success. 

Highly appreciate your feedback on how to get the script working. THANKS!

Here the error msg:

```
{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7 ChromePlus/1.5.0.0alpha1'}
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1374, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 287, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

[...]

requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
[Finished in 15.9s with exit code 1]
```


Here my code:
```
from bs4 import BeautifulSoup
import requests
import pyuser_agent

URL = f"https://www.edmunds.com/inventory/srp.html?radius=5000&sort=publishDate%3Adesc&pagenumber=2"

ua = pyuser_agent.UA()
headers = {'User-Agent': ua.random}
print(headers)

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
overview = soup.find()
print(overview)
```




I tried multiple headers, but do not get a result

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-09): Can you try it with this header (not the random one): `headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}`  ?
- **[Irra](https://stackoverflow.com/users/19689942)** (2023-01-09): great this works!!! thank you! Can you please provide my a short explanation?
- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-09): I've posted an answer, so you can close the question.

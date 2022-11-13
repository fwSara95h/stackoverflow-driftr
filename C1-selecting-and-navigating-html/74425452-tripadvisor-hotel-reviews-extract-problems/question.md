---
title: "TripAdvisor Hotel Reviews Extract Problems"
site: stackoverflow
question_id: 74425452
url: https://stackoverflow.com/q/74425452
asked: 2022-11-13T23:03:46Z
asked_by: "Shiron Pereira"
asked_by_url: https://stackoverflow.com/users/19443739
last_edited: never
tags: [beautifulsoup, tripadvisor]
score: 0
views_at_snapshot: 179
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cde7b69a6bd33eece5394de9efc50dfda672a17531c03de6ac65ba25df8c7d85
---

# TripAdvisor Hotel Reviews Extract Problems

Asked by [Shiron Pereira](https://stackoverflow.com/users/19443739) on Stack Overflow, <https://stackoverflow.com/q/74425452>, 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Trying to obtain Hotel Reviews from TripAdvisor. I have a code its running but not retreiving any output, need help to retreive data.

```
import requests
from bs4 import BeautifulSoup

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en,mr;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

url = "https://www.tripadvisor.co.uk/Hotel_Review-g304141-d447407-Reviews-or10-Sigiriya_Village_Hotel-Sigiriya_Central_Province.html#REVIEWS"
req = requests.get(url,headers=headers,timeout=5,verify=False)
print (req.status_code)
soup = BeautifulSoup(req.content, 'html.parser')

#review = soup.find_all(class_="XllAv H4 _a").get_text()
#print(review)
for x in soup.body.find_all(class_="bdYc _Q"):
    print(x.text)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Shiron Pereira](https://stackoverflow.com/users/19443739)** (2022-11-14): My expected Output should be only the Review Text

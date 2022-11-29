---
title: "Why is Beautifulsoup's selector showing error while the Scrapy's response.css working absolutely fine?"
site: stackoverflow
question_id: 74620048
url: https://stackoverflow.com/q/74620048
asked: 2022-11-29T20:40:38Z
asked_by: "Pranav Anand"
asked_by_url: https://stackoverflow.com/users/17532236
last_edited: never
tags: [python, html, css, beautifulsoup, scrapy]
score: 0
views_at_snapshot: 502
answer_count: 1
accepted_answer_id: 74635420
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 079f9cade02f325372286104527280e8fb4d5c9eac4c071bf509f898699bd331
---

# Why is Beautifulsoup's selector showing error while the Scrapy's response.css working absolutely fine?

Asked by [Pranav Anand](https://stackoverflow.com/users/17532236) on Stack Overflow, <https://stackoverflow.com/q/74620048>, 2022-11-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape this div tag which has an id attribute equal to today's date. I created a Beautifulsoup object and used the select method but it's showing this error

My code 
```
res = requests.get('https://sports.ndtv.com/fifa-world-cup-2022/schedules-fixtures')
soup = BeautifulSoup(res.text,'html.parser')
date_today = date.today()
d1 = date_today.strftime("%d-%m-%Y")
cont = soup.select('div#'+d1)
```
This is raising the error

```
raise SelectorSyntaxError(msg, self.pattern, index)
soupsieve.util.SelectorSyntaxError: Malformed id selector at position 3
line 1:
div#30-11-2022
```
While when I use Scrapy shell -

```
response.css('div#'+d1)[0].css('span.location::text').get()           
'Ahmad Bin Ali Stadium, Al Rayyan'

```
It's working perfectly fine. Can anyone please suggest what am I doing wrong?
Thanks

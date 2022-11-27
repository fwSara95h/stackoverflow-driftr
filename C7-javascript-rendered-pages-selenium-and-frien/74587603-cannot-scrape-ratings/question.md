---
title: "cannot scrape ratings"
site: stackoverflow
question_id: 74587603
url: https://stackoverflow.com/q/74587603
asked: 2022-11-27T04:53:40Z
asked_by: "Jaevapple"
asked_by_url: https://stackoverflow.com/users/20143343
last_edited: 2022-12-03T17:56:11Z
tags: [python, selenium, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 159
answer_count: 1
accepted_answer_id: 74643531
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ceecf2d42757bc0b164ff7f53cfc4eb60c6dadec1f430873d0c0e5dbdc722ae6
---

# cannot scrape ratings

Asked by [Jaevapple](https://stackoverflow.com/users/20143343) on Stack Overflow, <https://stackoverflow.com/q/74587603>, 2022-11-27, last edited 2022-12-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

My issue is that I cannot use bs4 to scrape sub ratings in its reviews. 
[Below is an example:](https://i.sstatic.net/RQYUR.png)

So far, I have discovered where these stars are, but their codes are the same regardless of the color (i.e., green or grey)... **I need to be able to identify the color to identify the ratings, not just scrape the stars.** Below is my code:

```
url='https://www.glassdoor.com/Reviews/Walmart-Reviews-E715_P2.htm?filter.iso3Language=eng'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
com = soup.find(class_ = "ratingNumber mr-xsm")
com1 = soup.find(class_ = "gdReview")
com1_1 = com1.find(class_ = "content")
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-01): `com` gets you the rating as a number - why do you need the star colors after that?
- **me** (2022-12-01): @Jaevapple- I do understand better now (You should specify in your question that you want the *sub*ratings as well, since the immediately visible ratings have a numeric value as well, so star colors are not important.)

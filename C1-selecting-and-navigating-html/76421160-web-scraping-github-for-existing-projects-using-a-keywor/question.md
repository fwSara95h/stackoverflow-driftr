---
title: "Web Scraping Github for existing projects using a keyword"
site: stackoverflow
question_id: 76421160
url: https://stackoverflow.com/q/76421160
asked: 2023-06-07T08:09:19Z
asked_by: "Baha Dawood ud-Din Rehman"
asked_by_url: https://stackoverflow.com/users/17188138
last_edited: 2023-06-07T08:09:45Z
tags: [python, github, web-scraping, beautifulsoup, web-crawler]
score: -2
views_at_snapshot: 978
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b4c361f9d6378ffeaf5e20bb49531ce37183421fdf2a7fa035f54eaa0ff06ede
---

# Web Scraping Github for existing projects using a keyword

Asked by [Baha Dawood ud-Din Rehman](https://stackoverflow.com/users/17188138) on Stack Overflow, <https://stackoverflow.com/q/76421160>, 2023-06-07, last edited 2023-06-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've written a code for a Github Web Scraper that scrapes the github search page of a specific keyword and scrapes any existing projects that have appeared after the search is done. The code doesn't work and returns empty data frame. Can anyone please help me rectify what went wrong?


```
rep_link=[]
description=[]
date=[]
url = "https://github.com/search?q=excel+import&type=repositories"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.prettify())

for a in soup.findAll('div', attrs={'class':'Box-sc-g0xbh4-0 jUbAHB'}):
    rep = a.find('a',href=True, attrs={'class':'Link__StyledLink-sc-14289xe-0 bJBoUI'})
    descp = a.find('span', attrs={'class':'Text-sc-17v1xeu-0 kWPXhV search-match'})
    dt = a.find('span', attrs={'class':'Text-sc-17v1xeu-0 gPDEWA'})
    rep_link.append(rep.text)
    description.append(descp.text)
    date.append(dt.text)

tem = list(zip(rep_link,description,date))
df = pd.DataFrame(data=tem, columns=["Repo","Description","Date"])
```
Im scraping for projects that have the search terms "Excel import", as mentioned in the url. Then in the various results, I wish to scrape the user repo link, the description and the last updated date. I might have gotten the class attributes wrong, please help me out.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2023-06-07): There's a [GitHub Search API](https://docs.github.com/en/rest/search?apiVersion=2022-11-28) and that's what you should be using instead of scraping.

---
title: "How to make a dictionary from 2 lists from web scraping"
site: stackoverflow
question_id: 74596046
answer_id: 74601446
url: https://stackoverflow.com/a/74601446
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-28T13:38:29Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74601446/revisions
accepted: false
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4d7a24f889d6fe8d4e3ea9bbc04e07144ca33a2aa923727a3510f6289034b4cc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74601446>, 2022-11-28; score 1. Text as retrieved 2026-10-12.

Since each review's rating categories start with either *"Type of Traveller"* or *"Aircraft"* followed by *"Type of Traveller"*, you could split them up into a list of dictionaries with
```python
cr = [(k, v) for k, v in zip(category, rating)]
si = [i for i, (k, v) in  enumerate(cr) if k == 'Type Of Traveller']
si = [(i - 1) if i != 0 and cr[i - 1][0] == 'Aircraft' else i for i in si]
splitCr = [dict(cr[start:end]) for start, end in zip(si, (si[1:] + [len(cr)]))]
```
[![output][1]][1]

---
---

However, it would be better to build a single list of dictionaries as we scrape [rather than to try to zip and split lists that are not guaranteed to have consistent lengths or contents]
```python
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 3 # 5 # 10
page_size = 5 # 1 # 100

revList = []
avgSelRef = {
    'rating10': '.rating-10 span[itemprop="ratingValue"]',
    'header': 'div.info:has(h1[itemprop="name"])',
    'subheader': '.review-count',
    'reviewBody': '.skytrax-rating-mob img.skytrax-rating[alt]'
}
rbSel = '.body[id^="anchor"]'
revSelRef = {
    'rating10': '.rating-10 span[itemprop="ratingValue"]',
    'header': f'{rbSel} h2.text_header',
    'subheader': f'{rbSel} h3.text_sub_header',
    'reviewBody': f'{rbSel} div[itemprop="reviewBody"]'
} 

avgAdded = False
for i in range(1, pages + 1): 
    print("", end=f"Scraping page {i} of {pages} ")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)
    if response.status_code != 200: 
        print(f' -- !ERROR: "{response.raise_for_status()}"" getting {url}')
        continue
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')

    avSoups = parsed_content.select('div.review-info')
    rvSoups = parsed_content.select(f'article[itemprop="review"]:has({rbSel})')
    if avSoups and not avgAdded: rvSoups += avSoups
    for r in rvSoups:
        isAvg = r.name == 'div'
        if isAvg:
            rDets = {'reviewId': '[Average]'} 
            selRef = avgSelRef.items()
            avgAdded = True
        else:
            revId = r.select_one(rbSel).get('id').replace('anchor', '', 1)
            selRef = revSelRef.items()
            rDets = {'reviewId': revId} 
        
        for k, s in selRef:
            rdt = r.select_one(s) 
            if rdt is None: continue
            if 'img' in s and s.endswith('[alt]'):
                rDets[k] = rdt.get('alt') 
            else:
                rDets[k] = ' '.join(w for w in rdt.get_text(' ').split() if w)

        rhSel = 'td.review-rating-header'
        rRows = r.select(f'tr:has({rhSel} + td:is(.stars, .review-value))')
        for rr in rRows: 
            k = rr.select_one(rhSel).get_text(' ').strip()
            k = k.replace(' For ', ' for ').replace(' & ', ' + ') # bit of cleanup
            if k.endswith('Staff Service'): k = 'Staff Service' # bit of cleanup
            if rr.select('td.stars'): 
                rDets[f'[stars] {k}'] = len(rr.select('td.stars span.star.fill'))
            else: 
                rDets[k] = rr.select_one('td.review-value').get_text().strip()

        revList = ([rDets] + revList) if isAvg else (revList + [rDets])
    print(' - ', len(rvSoups), 'reviews --->', len(revList), 'total reviews') 
```
[![op2][2]][2]

---

You could also view just the star ratings: [![op3][3]][3]


  [1]: https://i.sstatic.net/cqWhV.png
  [2]: https://i.sstatic.net/ENtbG.png
  [3]: https://i.sstatic.net/XzwoK.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Raffel Ravionaldo](https://stackoverflow.com/users/18388803)** (2022-11-29): Wow, Thank you for helping me, may I know where you are learning this?
- **me** (2022-11-29): @RaffelRavionaldo [glad it helped!]  it was a few years ago, so I don't remember exactly, but I learned python basics probably from [Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc) or [fcc](https://www.youtube.com/watch?v=rfscVS0vtbw) (and [the docs](https://docs.python.org/3/library/functions.html) are worth a look too); after that, I looked up libraries & approaches according to whatever my projects needed. bs4 I learned almost entirely from [the docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc) as well as [the soupsieve ref](https://facelessuser.github.io/soupsieve/selectors/)

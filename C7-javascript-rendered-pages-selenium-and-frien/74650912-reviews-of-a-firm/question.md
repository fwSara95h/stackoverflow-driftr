---
title: "reviews of a firm"
site: stackoverflow
question_id: 74650912
url: https://stackoverflow.com/q/74650912
asked: 2022-12-02T04:27:14Z
asked_by: "Jaevapple"
asked_by_url: https://stackoverflow.com/users/20143343
last_edited: 2022-12-06T09:14:02Z
tags: [python, selenium, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 117
answer_count: 1
accepted_answer_id: 74663815
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a9bb61f9c2ce5a503ddda7d219ddb123a6258635f4b16f50fcdb9770bdac9ce3
---

# reviews of a firm

Asked by [Jaevapple](https://stackoverflow.com/users/20143343) on Stack Overflow, <https://stackoverflow.com/q/74650912>, 2022-12-02, last edited 2022-12-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

My goal is to scrape the entire reviews of this firm. I tried manipulating @Driftr95 codes:

```
def extract(pg): 
    headers = {'user-agent' : 'Mozilla/5.0'}
    url = f'https://www.glassdoor.com/Reviews/3M-Reviews-E446_P{pg}.htm?filter.iso3Language=eng'
    # f'https://www.glassdoor.com/Reviews/Google-Engineering-Reviews-EI_IE9079.0,6_DEPT1007_IP{pg}.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng'

    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')# this a soup function that retuen the whole html
    return soup

for j in range(1,21,10):
    for i in range(j+1,j+11,1): #3M: 4251 reviews
        soup = extract( f'https://www.glassdoor.com/Reviews/3M-Reviews-E446_P{i}.htm?filter.iso3Language=eng')
        print(f' page {i}')
        for r in soup.select('li[id^="empReview_"]'):
            rDet = {'reviewId': r.get('id')}
            for sr in r.select(subRatSel):
                k = sr.select_one('div:first-of-type').get_text(' ').strip()
                sval = getDECstars(sr.select_one('div:nth-of-type(2)'), soup)
                rDet[f'[rating] {k}'] = sval
    
            for k, sel in refDict.items():
                sval = r.select_one(sel)
                if sval: sval = sval.get_text(' ').strip()
                rDet[k] = sval
    
            empRevs.append(rDet) 
```

In the case where not all the subratings are always available, all four subratings will turn out to be N.A.

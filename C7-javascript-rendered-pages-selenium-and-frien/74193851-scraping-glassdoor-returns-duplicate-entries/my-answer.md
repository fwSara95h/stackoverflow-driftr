---
title: "Scraping Glassdoor returns duplicate entries"
site: stackoverflow
question_id: 74193851
answer_id: 74240970
url: https://stackoverflow.com/a/74240970
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T21:12:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74240970/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [glassdoor stats]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8c3ea0827ca3bf51345b5beb433bffaa495f5a0383f9335091c84ca720d88f6c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74240970>, 2022-10-28; score 1. Text as retrieved 2026-10-12.

I don't think the repetition is due to a code issue - I think glassdoor just starts cycling results after a while. [If interested, [see this gist for some stats](https://gist.github.com/Driftr95/91c463c3e18ac1a121323ab0c7d983a4) - basically, from the 7th page or so, most of the 1st page results seem to be shown on every page onwards. I did a small test manually - with only 5 listings, by id, and even directly on an un-automated browser, they started repeating after a while....]

My suggestion would be to just filter them before looping to the next page - there's a `data-id` attribute for each `li` wrapped around the listings which seems to be a unique identifier. If we add that to the other columns' lists, we can start collecting only un-collected listings; if you just edit the `for page_num` loop to:
```python
    for page_num in range(1, 10):
        time.sleep(10)

        scrapedUrls.append(driver.current_url)

        res = requests.get(driver.current_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # soup = BeautifulSoup(driver.page_source, 'html.parser') # no noticable improvement

        time.sleep(2)

        filteredListings = [
            di for di in soup.select('li[data-id]') if
            di.get('data-id') not in datId_list
        ]
        datId_list += [di.get('data-id') for di in filteredListings] 

        companies_list += [
            t.select_one('.css-l2wjgv.e1n63ojh0.jobLink').get_text(strip=True)
            if t.select_one('.css-l2wjgv.e1n63ojh0.jobLink')
            else None for t in filteredListings
        ]

        positions_list += [
            t.select_one('.jobLink.css-1rd3saf.eigr9kq2').get_text(strip=True)
            if t.select_one('.jobLink.css-1rd3saf.eigr9kq2')
            else None for t in filteredListings
        ]

        locations_list += [
            t.select_one(
                '.css-l2fjlt.pr-xxsm.css-iii9i8.e1rrn5ka0').get_text(strip=True)
            if t.select_one('.css-l2fjlt.pr-xxsm.css-iii9i8.e1rrn5ka0')
            else None for t in filteredListings
        ]

        job_post = [
            t.select('.eigr9kq3 .e1wijj242') for t in filteredListings
        ]
        salaries_list += [
            'Salary Not Found' if not j else
            (j[0].text if len(j) == 1 else [s.text for s in j])
            for j in job_post
        ]

        ratings_list += [
            t.select_one('.e1rrn5ka3').get_text(strip=True)
            if t.select_one('.e1rrn5ka3')
            else 'Rating Not Found' for t in filteredListings
        ]

```
and, if you added `datId_list` to the dataframe, it could serve as a meaningful index
```python
    dfDict = {'Data-Id': datId_list,
              'Company Name': companies_list,
              'Company Rating': ratings_list,
              'Position Title': positions_list,
              'Location': locations_list,
              'Est. Salary': salaries_list
              }
    for k in dfDict:
        print(k, len(dfDict[k]))
    glassdoor_dataset = pd.DataFrame(dfDict)
    glassdoor_dataset.set_index('Data-Id', drop=True)

    glassdoor_dataset.to_csv(r'glassdoor_jobs_scraped.csv')
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Zoya Aqib](https://stackoverflow.com/users/15606732)** (2022-10-29): You're right but that just returns 180 entries which are the ones that could be scraped from just the first 6 pages. Thanks though!

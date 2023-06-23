---
title: "I'm having issues with a python program for scraping TripAdvisor Reviews"
site: stackoverflow
question_id: 76540171
answer_id: 76543548
url: https://stackoverflow.com/a/76543548
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-23T21:23:29Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76543548/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a5b670ddfa910ec31bac252c297ebfafb0c4842fbcd2e34a85a5c23ef4376853
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76543548>, 2023-06-23; **accepted**; score 0. Text as retrieved 2026-10-12.

I couldn't debug your code, your code but I have successfully scraped tripadvisor before (with selenium) using a simple while loop as below. 

---

Using my [`selectForList`](https://pastebin.com/ZnZ7xM6u) function for convenience, with the following selectors:

```py
nxt_pg_sel = 'a[href][data-smoke-attr="pagination-next-arrow"]'
review_sel = 'div[data-automation="reviewCard"]'
rev_dets_sel = {
    'from_page': ('', '"staticVal"'),
    'profile_name': 'span>a[href^="\/Profile\/"]',
    'profile_link': ('span>a[href^="\/Profile\/"]', 'href'),
    'about_reviewer': 'span:has(>a[href^="\/Profile\/"])+div',
    'review_votes': 'button[aria-label="Click to add helpful vote"]>span',
    'bubbles': ('svg[aria-label$=" of 5 bubbles"]', 'aria-label'),
    'review_link': ('a[href^="\/ShowUserReviews-"]', 'href'),
    'review_title': 'a[href^="\/ShowUserReviews-"]',
    'about_review': 'div:has(>a[href^="/ShowUserReviews-"])+div:not(:has(div))',
    'review_body': 'div:has(>a[href^="/ShowUserReviews-"])~div>div',
    'review_date': 'div:has(>a[href^="/ShowUserReviews-"])~div:last-child>div',
}
```

---

For your specific page:

```py
csv_fn_revs = 'Scudamore_s_Punting_Company-tripadvisor_reviews.csv'
csv_fn_pgs = 'Scudamore_s_Punting_Company-tripadvisor_review_pages.csv'
pgNum, maxPages = 0, None
pageUrl = 'https://www.tripadvisor.co.uk/Attraction_Review-g186225-d213774-Reviews-Scudamore_s_Punting_Company-Cambridge_Cambridgeshire_England.html'
```

---

And the rest is as I did before with that simple while loop:

```py
browser = webdriver.Chrome()
browser.maximize_window() # maximize window

reveiws_list, pgList = [], []
while pageUrl and (maxPages is None or pgNum < maxPages):
    pgNum += 1
    pgList.append({'page': pgNum, 'URL': pageUrl})
    try:
        browser.get(pageUrl)
        rev_dets_sel['from_page'] = (pgNum, '"staticVal"')
        pgSoup = BeautifulSoup(browser.page_source, 'html.parser')

        rev_cards = pgSoup.select(review_sel)
        reveiws_list += [selectForList(r, rev_dets_sel) for r in rev_cards]
        pgList[-1]['reviews'] = len(rev_cards)

        next_page = pgSoup.select_one(nxt_pg_sel)
        if next_page:
            pageUrl = 'https://www.tripadvisor.co.uk' + next_page.get('href')
            pgList[-1]['next_page'] = pageUrl
            print('going to', pageUrl)
        else:
            pageUrl = None  # stop condition
    except Exception as e:
        print(f'Stopping on pg{pgNum} due to {type(e)}:\n{e}')
        break

browser.quit() # Close the browser
```

```py
# Save as csv
pd.DataFrame(reveiws_list).to_csv(csv_fn_revs, index=False)
pd.DataFrame(pgList).to_csv(csv_fn_pgs, index=False)
```

---

It's a bit different from how you did it, and the last column [`review_date`] isn't perfect, but I was able to scrape all 1621 reviews from your link (see full results in [this spreadsheet](https://docs.google.com/spreadsheets/d/1vHcLuaeRgcgi3dh6PLG11R4kh2ylnGRiOnv6r1rHVaM/edit?usp=sharing))

[![pglogs][1]][1]

[![revs][2]][2]


  [1]: https://i.sstatic.net/xjv4K.png
  [2]: https://i.sstatic.net/GaNIz.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Leif Moore](https://stackoverflow.com/users/22120006)** (2023-06-27): This was amazingly helpful thank you so much 🙏

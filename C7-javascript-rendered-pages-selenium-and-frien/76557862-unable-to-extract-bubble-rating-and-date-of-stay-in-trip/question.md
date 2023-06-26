---
title: "Unable to extract bubble rating and date of stay in TripAdvisor hotel reviews using Selenium"
site: stackoverflow
question_id: 76557862
url: https://stackoverflow.com/q/76557862
asked: 2023-06-26T14:57:24Z
asked_by: "speeddefiesgravity"
asked_by_url: https://stackoverflow.com/users/10155179
last_edited: never
tags: [python, selenium-webdriver, web-scraping, beautifulsoup, tripadvisor]
score: 0
views_at_snapshot: 108
answer_count: 1
accepted_answer_id: 76558620
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fabff598c1d8db1446331485052db3abe9fd734730bc24f7d984cedc70409e8f
---

# Unable to extract bubble rating and date of stay in TripAdvisor hotel reviews using Selenium

Asked by [speeddefiesgravity](https://stackoverflow.com/users/10155179) on Stack Overflow, <https://stackoverflow.com/q/76557862>, 2023-06-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm currently trying to extract the hotel reviews (body and title) along with the the rating and date of stay. I've come across [@Driftr95](https://stackoverflow.com/questions/76540171/im-having-issues-with-a-python-program-for-scraping-tripadvisor-reviews)'s brilliant solution for scraping data about TripAdvisor attractions, and executed with no issues.

Original URL **(Attraction)**: https://www.tripadvisor.co.uk/Attraction_Review-g186225-d213774-Reviews-Scudamore_s_Punting_Company-Cambridge_Cambridgeshire_England.html

However, when I replace the URL with a *hotel* rather than an attraction, the code fails to return the right data.

Desired URL **(Hotel):** https://www.tripadvisor.com/Hotel_Review-g186405-d215170-Reviews-Portreeves-Arundel_Arun_District_West_Sussex_England.html

As such, I've modified the original code to reflect the new nxt\_*pg_sel* and review\_*sel containers as follows.* However, the bubble rating and review date in the resulting data frame are blank.

```
nxt_pg_sel = 'a.next'
review_sel = 'div[data-test-target="HR_CC_CARD"]'
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

I also attempted to capture the stay_date which broke the code entirely. 

> ```
> 'review_date': 'div:has(>a[href^="/ShowUserReviews-"])~div:last-child>div',
> ```

I've tried looking at the dynamic tags within the new URL but cannot seem to figure out why these elements are not being scrapped. Would appreciate any suggestions. Many many thanks !

PS the original code that works flawlessly (but for attractions) is attached below.

```
##selectforlist
def selectForList(tagSoup, selectors, printList=False):
    if isinstance(selectors, dict):
        return dict(zip(selectors.keys(), selectForList(
            tagSoup, selectors.values(), printList)))
    
    selGen = (( list(sel if isinstance(sel, (tuple, list)) ## generate params
                else [sel])+[None]*2 )[:3] for sel in selectors)
    returnList = [  sel[0] if sel[1] == '"staticVal"' ## [allows placeholders]
                    else selectGet(tagSoup, *sel) for sel in selGen   ]
    
    if printList and not isinstance(printList,str): print(returnList)
    if isinstance(printList,str): print(*returnList, sep=printList)
    return returnList

##original selectors
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

##set variables
csv_fn_revs = 'Scudamore_s_Punting_Company-tripadvisor_reviews.csv'
csv_fn_pgs = 'Scudamore_s_Punting_Company-tripadvisor_review_pages.csv'
pgNum, maxPages = 0, None
pageUrl = 'https://www.tripadvisor.co.uk/Attraction_Review-g186225-d213774-Reviews-Scudamore_s_Punting_Company-Cambridge_Cambridgeshire_England.html'

##scrape data using web driver
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

# Save as csv
pd.DataFrame(reveiws_list).to_csv(csv_fn_revs, index=False)
pd.DataFrame(pgList).to_csv(csv_fn_pgs, index=False)
```

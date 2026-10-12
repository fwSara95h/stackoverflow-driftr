# Code from my Stack Overflow answer https://stackoverflow.com/a/76543548 (posted 2023-06-23), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
csv_fn_revs = 'Scudamore_s_Punting_Company-tripadvisor_reviews.csv'
csv_fn_pgs = 'Scudamore_s_Punting_Company-tripadvisor_review_pages.csv'
pgNum, maxPages = 0, None
pageUrl = 'https://www.tripadvisor.co.uk/Attraction_Review-g186225-d213774-Reviews-Scudamore_s_Punting_Company-Cambridge_Cambridgeshire_England.html'

# --- block 3 ---
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

# --- block 4 ---
# Save as csv
pd.DataFrame(reveiws_list).to_csv(csv_fn_revs, index=False)
pd.DataFrame(pgList).to_csv(csv_fn_pgs, index=False)

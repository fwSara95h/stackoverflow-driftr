# Code from my Stack Overflow answer https://stackoverflow.com/a/76558620 (posted 2023-06-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
'bubbles': ('div[data-test-target="review-rating"]>span', 'class'),

# --- block 2 ---
'stay_date': 'div[data-test-target="review-title"]+div>div:nth-child(2)>span:first-child',

# --- block 3 ---
nxt_pg_sel = 'a.next[href]'  # '[data-smoke-attr="pagination-next-arrow"]'
# review_sel = 'div[data-automation="reviewCard"]'
review_sel = 'div[data-test-target="HR_CC_CARD"]'
rev_dets_sel = {
    'from_page': ('', '"staticVal"'),
    'profile_name': 'span>a[href^="\/Profile\/"]',
    'profile_link': ('span>a[href^="\/Profile\/"]', 'href'),
    # 'about_reviewer': 'span:has(>a[href^="\/Profile\/"])+div',
    'about_reviewer': 'a.ui_social_avatar+div>div+div+div',
    # 'review_votes': 'button[aria-label="Click to add helpful vote"]>span',
    # 'bubbles': ('svg[aria-label$=" of 5 bubbles"]', 'aria-label'),
    'bubbles': ('div[data-test-target="review-rating"]>span', 'class'),
    'review_link': ('a[href^="\/ShowUserReviews-"]', 'href'),
    'review_title': 'a[href^="\/ShowUserReviews-"]',
    # 'about_review': 'div:has(>a[href^="\/ShowUserReviews-"])+div:not(:has(div))',
    'review_body': 'div:has(>a[href^="\/ShowUserReviews-"])~div>div',
    # 'review_date': 'div:has(>a[href^="\/ShowUserReviews-"])~div:last-child>div',
    'stay_date': 'div[data-test-target="review-title"]+div>div:nth-child(2)>span:first-child',
}

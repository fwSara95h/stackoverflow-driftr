---
title: "Unable to extract bubble rating and date of stay in TripAdvisor hotel reviews using Selenium"
site: stackoverflow
question_id: 76557862
answer_id: 76558620
url: https://stackoverflow.com/a/76558620
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-26T16:36:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76558620/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5945f13c48617a14989544a64975ddadf1672648deea1cbfc05fd49dc52d7a0c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76558620>, 2023-06-26; **accepted**; score 0. Text as retrieved 2026-10-12.

> I also attempted to capture the stay_date which broke the code entirely.

Did it raise an error? Could you elaborate on the error? [If it just generates irrelevant data, then that's within normal behavior since that selector now leads to something else.]

<sup>(Also, I'm actually pleasantly surprised by how many of the old selectors still work - you often have to figure out an entirely new set of selectors for a new type of page...)</sup>

---

For the `bubbles`, I suggest now using 

```py
    'bubbles': ('div[data-test-target="review-rating"]>span', 'class'),
```

and for the `stay_date`, try

```py
    'stay_date': 'div[data-test-target="review-title"]+div>div:nth-child(2)>span:first-child',
```

overall, the new set of selectors I'd suggest using for hotels:

```py
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
```

(I've uploaded my results to the same [spreadsheet](https://docs.google.com/spreadsheets/d/1vHcLuaeRgcgi3dh6PLG11R4kh2ylnGRiOnv6r1rHVaM/edit?usp=sharing) as before.)

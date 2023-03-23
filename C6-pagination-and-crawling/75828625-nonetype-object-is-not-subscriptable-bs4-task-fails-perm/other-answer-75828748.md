---
title: "NoneType' object is not subscriptable : bs4 task fails permanently"
site: stackoverflow
question_id: 75828625
answer_id: 75828748
url: https://stackoverflow.com/a/75828748
author: "riley.johnson3"
author_url: https://stackoverflow.com/users/4705390
posted: 2023-03-23T23:14:20Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 70f53707a84728247d92237b64ccfc1e1d25adaf26b5aaadd86cbbf813f975ee
role: another answer on the same question, kept as context; not my work
---

# Answer by [riley.johnson3](https://stackoverflow.com/users/4705390) — 2023-03-23

Posted on Stack Overflow, <https://stackoverflow.com/a/75828748>, 2023-03-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The problem is that the id you're using (`paginationPagesNum`) does not exist in the page. This statement returns `None`:

    soup.find('input', {'id': 'paginationPagesNum'})

You're trying to access the `'value'` attribute from a `NoneType`, which is what causes the error. To fix it, you need to find the right tag. This code sample finds the pagination wrapper, finds the individual elements, and determines their length:

    pagination_wrapper = soup.select_one(
        '#_eu_europa_ec_jrc_dih_web_DihWebPortlet_list-web-page-iterator'
    )
    
    pagination_items = pagination_wrapper.select(
        'ul > li:not(.ecl-pagination__item--next)'
    )

    num_pages = len(pagination_items)
Alternatively, here's a one-liner to achieve the same thing:

    num_pages = len(soup.select('#_eu_europa_ec_jrc_dih_web_DihWebPortlet_list-web-page-iterator > ul > li:not(.ecl-pagination__item--next)'))

Note that the `:not(.ecl-pagination__item--next)` is required to filter out the next page button; otherwise, `num_pages` would be off by 1.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[zero](https://stackoverflow.com/users/525865)** (2023-03-23): good day dear riley - awesome many thanks for the quick help and the explanation - have gathered  a set of data - its a sample. have to find out now how to get the full set of data. all the 700 records - with all the data.. - guess that we are allmost there. - again many thanks for your outstanding help. this is great... and appreciated alot... ;)
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): riley - again many thanks - so encouraging and helpful - btw with the new and updated code i run the script and have gotten back a set of approx 50 lines. But there are 700 or more lines in the dataset.. i have to look how to achieve the full set...
- **[zero](https://stackoverflow.com/users/525865)** (2025-07-31): many thanks for all the hints - and the brilliant help so far!

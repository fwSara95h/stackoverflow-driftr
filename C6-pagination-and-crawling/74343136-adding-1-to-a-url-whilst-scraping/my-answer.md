---
title: "Adding +1 to a URL whilst scraping"
site: stackoverflow
question_id: 74343136
answer_id: 74343296
url: https://stackoverflow.com/a/74343296
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-07T07:35:07Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74343296/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c1c159de514f4fb57b665487a174283361779033c5d42eaaeea0ad5b173c5899
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74343296>, 2022-11-07; score 0. Text as retrieved 2026-10-12.

You could do something like
```python
last_page_num = # set the last page number here

scraped_data = []
for page_num in range(1, last_page_num + 1):
    url = f'youtube.com/user/{page_num}/'
    try:

        ################## SCRAPE URL ################## 
   
        ############ APPEND TO scraped_data ############

    except Exception as err: 
        print(f'unable to scrape {url}\n{str(err)}')
        # break # if you want to stop after first error

################# SAVE scraped_data #################
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user19476773 (account no longer exists)** (2022-11-07): Interesting, thank you for responding. I appreciate it!
- **user19476773 (account no longer exists)** (2022-11-11): what if you don't know the last page number?
- **me** (2022-11-11): @Omar if you know how to detect the last page, add a conditional `break` for it; otherwise, you can set a number you can be sure is the more than the maximum page number, and then either: accept that all iterations after the last page are going to be wasted (and also will print at least 2 lines of error messages each time), **OR** uncomment the `break` in `except:..` (if you're not expecting errors before reaching last page), **OR** add a counter in `except:..` and `break` after a certain number of errors

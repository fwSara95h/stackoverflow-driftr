---
title: "reviews of a firm"
site: stackoverflow
question_id: 74650912
answer_id: 74663815
url: https://stackoverflow.com/a/74663815
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-03T03:38:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74663815/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [getDECstars, linkToSoup, selenium fallback fetcher]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f84dc7dd8701f6ba91476bded6e7f73a54115287a9d140a468fc75eee97e8da9
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74663815>, 2022-12-03; **accepted**; score 0. Text as retrieved 2026-10-12.

> All four subratings will turn out to be N.A.

there were some things that I didn't account for because I hadn't encountered them before, but the [updated version of](https://pastebin.com/Q0GLwRv9) `getDECstars` shouldn't have that issue. (If you use the longer version with argument `isv=True`, it's easier to debug and figure out what's missing from the code...)

---

> I scraped 200 reviews in this case, and it turned out that only 170 unique reviews

Duplicates are fairly easy to avoid by maintaining a list of `reviewId`s that have already been added and checking against it before adding a new review to `empRevs`
```python
scrapedIds = []
# for...
    # for ###
        # soup = extract...

        # for r in ...
            if r.get('id') in scrapedIds: continue # skip duplicate
            ## rDet = ..... ## AND REST OF INNER FOR-LOOP ##

            empRevs.append(rDet) 
            scrapedIds.append(rDet['reviewId']) # add to list of ids to check against
```

---

> Https tends to time out after 100 rounds...

You could try adding breaks and [switching out user-agents](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/) every 50 [or 5 or 10 or...] requests, but I'm quick to resort to selenium at times like this; [this is my suggested solution](https://pastebin.com/RsFHWNnt) - if you just call it like this and pass a url to start with:

```python
## PASTE [OR DOWNLOAD&IMPORT] from https://pastebin.com/RsFHWNnt ##

startUrl = 'https://www.glassdoor.com/Reviews/3M-Reviews-E446.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng'
scrape_gdRevs(startUrl, 'empRevs_3M.csv', maxScrapes=1000, constBreak=False)
```
> [last 3 lines of] printed output:
> ``` lang-none
>  total reviews:  4252
> total reviews scraped this run: 4252
> total reviews scraped over all time: 4252
> ```

It clicks through the pages until it reaches the last page (or maxes out `maxScrapes`). You do have to **log in** at the beginning though, so fill out `login_to_gd` with your username and password or log in manually by replacing the `login_to_gd(driverG)` line with the `input(...)` line that waits for you to login [then press ENTER in the terminal] before continuing. 

I think cookies can also be used instead (with requests), but I'm not good at handling that. If you figure it out, then you can use some version of `linkToSoup` or your `extract(pg)`; then, you'll have to comment out or remove the lines ending in `## for selenium` and uncomment [or follow instructions from] the lines that end with `## without selenium`. [But please note that I've only fully tested the selenium version.]

The CSVs [like "empRevs_3M.csv" and "scrapeLogs_empRevs_3M.csv" in this example] are updated after every page-scrape, so even if the program crashes [or you decide to interrupt it], it will have saved upto the previous scrape. Since it also tries to load form the CSVs at the beginning, you can just continue it later (just set `startUrl` to the url of the page you want to continue from - but even if it's at page 1, remember that duplicates will be ignored, so it's okay - it'll just waste some time though).

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-03): @Jaevapple ah I'm sorry 😅 I missed some things while pasting - the `from selenium.webdriver.common.keys import Keys` line [which allows automated login, but maybe you caught that since you logged in...or did you end up having to manually do it?], the last part of `login_to_gd` [which checks that login worked], and **most importantly**, the `driverG.get(pgUrl)` line which actually takes the browser to the starting page - and that's why nothing was happening. I've update [the paste](https://pastebin.com/RsFHWNnt) and I hope you're up to giving it one more try...
- **me** (2022-12-03): @Jaevapple test it with like `maxScrapes=3` or some other small number first btw
- **me** (2022-12-03): No I don't have that issue [[these are my results](https://docs.google.com/spreadsheets/d/1fReg6NhFbuLk5QjpAPrMww5SxuhY3LqvJSfTay1tfFs/edit?usp=sharing)] - but that's for the selenium version so `getDECstars` doesn't come into play (and I can't access glassdoor with requests anymore, so I can't really test it...).

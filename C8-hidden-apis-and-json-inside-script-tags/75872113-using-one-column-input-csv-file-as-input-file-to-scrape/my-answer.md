---
title: "Using one-column input csv file as input file to scrape webpages (with potential next pages)"
site: stackoverflow
question_id: 75872113
answer_id: 75894956
url: https://stackoverflow.com/a/75894956
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T04:51:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75894956/revisions
accepted: true
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 572ba15643587bd516bc4e51152ea7b225779c18106c6744825c3ff611af865c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75894956>, 2023-03-31; **accepted**; score 0. Text as retrieved 2026-10-12.

Just listing my suggestions from the comments:
- parametrize the search url for `Parser` like `def Parser(self, session, searchUrl)`
  - and then have *`...session.get(searchUrl...as response:...`*
  - in `LoggerParser` read in the URLs with something like 
    ```py
    searchUrls=set(pd.read_csv('input_file.csv', header=None)[0])
    ```
    and loop through them with something like 
    ```py
    for url in searchUrls: await self.Parser(session, url)
    ```
- omit `headers['referer']` unless it's absolutely necessary
- add something to break the infinite *`while True...`* loop
  - `if not links: break` to stop after last page
  - [OR] find the pagination progress with `soup.find('div', class_='row-label')`, but break if that `div` is not found - something like
      ```py
                      # soup:=BeautifulSoup(await response.text(), "lxml"))
                      if not (pgProg:=soup.find('div', class_='row-label')): break
                      ### print('Now extracting:', pgProg, 'from', searchUrl) ## [OPTIONAL]
                      # links = soup.select("div.has-padding-content-block-30.-zb")
      ```
  - [optionally] *`if count>max_page: break`* to limit number of pages
- indent the *`count += 1`* line to move it inside the `while` loop so that the same page isn't scraped over and over
- Use **either** the `params` argument or the query string in `searchUrl`
  - if using `params`, break down `searchUrl` with [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) and rebuild like
    ```py
    # from urllib.parse import urljoin, urlsplit, parse_qsl
    ```
    ```py
            split_url = urlsplit(searchUrl)
            params = dict(parse_qsl(split_url.query) # + [('page',f'{count}')])
            snpUrl = urljoin(f'{split_url.scheme}://{split_url.netloc}', split_url.path)
    ```
    ```py
                params['page'] = count
                async with session.get(snpUrl, params=params) as response:
    ```
  - if using query string in url, just format `count` into it:
    ```py
                async with session.get(f'{searchUrl}&page={count}') as response:
    ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[PressMeister](https://stackoverflow.com/users/21433696)** (2023-04-01): Thanks so much for all your help. Listen, it is customary at stackoverflow to add the cleaned-up script (reformatted without warnings) that worked to the original post? It might help others - or is that not done?
- **me** (2023-04-01): @PressMeister It's definitely not customary, but I couldn't say if there's any consensus against it either. However, in my personal opinion, it *can* make the question look a bit confusing by adding so much to the original, so it might be better to add it as an answer instead (or to just add a small note with a pastebin link [etc] at the end of the question).

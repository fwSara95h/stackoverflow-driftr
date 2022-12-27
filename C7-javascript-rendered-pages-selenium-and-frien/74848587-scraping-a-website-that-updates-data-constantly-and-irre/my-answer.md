---
title: "Scraping a website that updates data constantly and irregularly"
site: stackoverflow
question_id: 74848587
answer_id: 74926301
url: https://stackoverflow.com/a/74926301
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-27T06:26:59Z
last_edited: 2022-12-27T06:32:24Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74926301/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [3-function set]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bcd63f93cc2e0fd2d1f21ebda078b94a7df5159eda13738f2c4fbc40cb6b23a6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74926301>, 2022-12-27, last edited 2022-12-27; **accepted**; score 0. Text as retrieved 2026-10-12.

**Note**: The full definitions for all 3 functions are **[pasted here](https://pastebin.com/sBsByTXt)**, and the outputs have been uploaded to [this spreadsheet](https://docs.google.com/spreadsheets/d/1E1QBKqaWoCB2SPAMyz0A_oe58MaV-yQbaSBGxGMBPC8). [Btw, I used [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) because I'm more comfortable with them, but the XPath equivalents are probably not too different.]

---

### Solution 1 [shorter but limited]

You can scrape the [link in the first row](https://i.sstatic.net/tPGl1.png) [as `thref` below] and then wait until it <sup>[*"link in first column of first row"*]</sup> changes

```python
    # wait = WebDriverWait(driver, maxWait) 

    # while rowCt < maxRows and tmoCt < max_tmo:...

        # parsing the whole table to gather as much data as possible 
        tSoup = BeautifulSoup(driver.find_element(
            By.CSS_SELECTOR, 'table:has(th.text-center) tbody'
        ).get_attribute('outerHTML'), 'html.parser')

        # get link from first column of first row
        thref = tSoup.select_one(
            f'tr:first-child>td:first-child>a[href]'
        ).get('href')

        ################### scrape rows' data from tSoup ###################

        try:
            thref = thref.replace('\\/', '/').replace('/', '\\/')
            thSel = 'table:has(th.text-center) tbody>tr:first-child>'
            thSel += 'td:first-child>a[href^="\/games\/"]'
            wait.until(EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, f'{thSel}:not([href="{thref}"])')))
        except: tmoCt += 1 # program ends if tmoCt gets too high 
```


Using this, the first function (*`scrape_pakakumi_lim`*) tries to scrape a certain number of rows (`maxRows`) and then [uses pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) to save the scraped data to `opfn` ("pakakumi.csv" by default).

The main issues are that 
- you'll need to specify `maxRows` [so you can't just scrape without pre-set limits]
- if you set too large a number as `maxRows`, you could end up using too much memory
- if anything breaks the program [error, interrupt, etc.], *all* the scraped data will be lost 

---

### Solution 2 

*`scrape_pakakumi`* [the 3rd and last function] depends on *`scrape_pakakumi_api`* [the 2nd function] to gather extra data using [the API](https://i.sstatic.net/1FmWc.png) [which returns a [JSON response](https://i.sstatic.net/49CCH.png) if everything goes ok]. The API can fail sometimes, especially if too many requests are sent too rapidly; in such cases just the `hash` and `crash` from the table are saved, but `created_at` is left empty and no `plays` are added.

It lets you remove the `maxRows` limitation by setting it to `None` (although the default is `999`),and also allows you to specify how many new rows you want to wait to load (but it must be lower than 39 because the table only has 40 rows). Instead of checking that the first cell does not not contain the same link anymore, it checks if the the link that used to be at the top is now below the *n<sup>th</sup>* row [*n*=`wAmt` below]. (Don't forget that `maxWait` should be adjusted to allow enough time for *n* new rows to load.)

```python
    # wait = WebDriverWait(driver, maxWait) 

            thSel = 'table:has(th.text-center) tbody'
            if isinstance(wAmt, int) and 1 < wAmt < 39:
                thSel = f'{thSel}>tr:nth-child({wAmt})~tr>td:first-child'
            else: thSel = f'{thSel}>tr:first-child~tr>td:first-child'
            wait.until(EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, f'{thSel}>a[href="{thref}"]')))
        # except: tmoCt += 1
```

If `wAmt` is passed as a float [like `10.0` or `3.5`], then the program just [sleeps](https://docs.python.org/3/library/time.html#time.sleep) for that many seconds instead of scanning for new rows.

```python
        if isinstance(wAmt, float):
            if not gData: # only wait if there's no new data
                time.sleep(wAmt)
            continue # skip rest of loop

        # try....except: tmoCt += 1
```

---

Both solutions keep track of previously added `game_id`s and check against them to avoid duplicates.

In solution 1, `addedIds` is just initiated as an empty list and then the duplicates are simply filtered out using [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).

```python
    addedIds, games, thref = [], [], '' # initiated outside loop

    # and then inside the loop:
        tGames = [t for t in tGames if t['game_id'] not in addedIds] # filter out duplicates

        games += tGames # add to main list

    # [main list (games) saved after loop]
```

In solution 2, the output file is checked for old data first, and since each `game_id` if scraped [with API] for individually [in an inner loop], the duplicates are skipped with `continue`. [The IDs are converted to string because `read_csv` extracts them as numbers, and the JSON also has them as numbers, but they're initially extracted as string from the link.]

```python
    try: # [before loop]
        prevData = pd.read_csv(gfn).to_dict('records') # get data from previous scrape
        addedIds = [str(g['game_id']) for g in prevData if 'game_id' in g][-1*maxIds:]
    except: addedIds = []

    maxIds = maxRows if maxRows and 100 < maxRows < 500 else 100 # for trimming

    # and then inside the loop:
        addedIds = addedIds[-1*maxIds:] # to reduce memory-usage a bit

        # scrape table

        for tg in tGames:
            if str(tg['game_id']) in addedIds: continue
            # tgg, tgp = scrape_pakakumi_api....
        # save scraped data

        addedIds += [str(g['game_id']) for g in gData]
```

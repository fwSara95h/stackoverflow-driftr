---
title: "Scraping Oddsportal for Matches and odds"
site: stackoverflow
question_id: 75058259
answer_id: 75101673
url: https://stackoverflow.com/a/75101673
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-12T19:58:21Z
last_edited: 2023-02-10T02:19:59Z
revisions: 7
revision_history: https://stackoverflow.com/posts/75101673/revisions
accepted: true
score: 2
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 99f15a97c092a5f0dbcb7dab45c9b7812489737f68ff5f0552ca130e9be2f9f8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75101673>, 2023-01-12, last edited 2023-02-10; **accepted**; score 2. Text as retrieved 2026-10-12.

**NOTE** : You can see a **<kbd>[complete solution](https://pastebin.com/Sd0E1Hmm)</kbd>** (compiled, tested and pasted by [@leonardo](https://stackoverflow.com/users/16949484/leonardo)) that includes my answer from below (or my **<kbd>[backup](https://pastebin.com/1XxAfr66)</kbd>** of it [cloned just in case]).


---

> How do I get values in the dataframe? If you could help me with one of the dataframe value positions,

If you use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://facelessuser.github.io/soupsieve/selectors/#selector), you can get *very* specific about the positions.

This [example](https://pastebin.com/vsbKVJ00) uses selectors to extract as much data as I could think of, but for just the positions in your DataFrame:

```python
def generate_matches(pgSoup, defaultVal=None):
    evtSel = {
        'time': 'p.whitespace-nowrap',
        'game': 'a div:has(>a[title])', 
        'score': 'a:has(a[title])+div.hidden', 
        'home_odds': 'a:has(a[title])~div:not(.hidden)',
        'draw_odds': 'a:has(a[title])~div:not(.hidden)+div:nth-last-of-type(3)',
        'away_odds': 'a:has(a[title])~div:nth-last-of-type(2)', 
    }

    events, current_group = [], {}
    pgDate = pgSoup.select_one('h1.title[id="next-matches-h1"]') ## EDIT
    if pgDate: pgDate = pgDate.get_text().split(',', 1)[-1].strip() ## EDIT
    for evt in pgSoup.select('div[set]>div:last-child'):
        if evt.parent.select(f':scope>div:first-child+div+div'):
            cgVals = [v.get_text(' ').strip() if v else defaultVal for v in [
              evt.parent.select_one(s) for s in 
              [ ':scope>div:first-child+div>div:first-child',
                ':scope>div:first-child>a:nth-of-type(2):nth-last-of-type(2)',
                ':scope>div:first-child>a:nth-of-type(3):last-of-type' ]]]
            current_group = dict(zip(['date', 'country', 'league'], cgVals))
            if pgDate: current_group['date'] = pgDate ## EDIT
        
        evtRow = {'date': current_group.get('date', defaultVal)}

        for k, v in evtSel.items():
            v = evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal
            evtRow[k] = ' '.join(v.split()) if isinstance(v, str) else v
        evtTeams = evt.select('a div>a[title]') ## EDIT
        evtRow['game'] = ' – '.join(a['title'] for a in evtTeams) ## EDIT

        evtRow['country'] = current_group.get('country', defaultVal)
        evtRow['league'] = current_group.get('league', defaultVal)

        events.append(evtRow)
    return events
```

would collect:

[![op][1]][1]

---

And change `parse_data` to

```python
def parse_data(url, return_urls=False):
    browser = create_driver() ## as before
    browser.get(url) ## as before
    browser.implicitly_wait(25) ## as before
    soup = bs(browser.page_source, "lxml") ## as before

    game_data = GameData() ## as before
    game_keys = [a for a, av in game_data.__dict__.items() if isinstance(av, list)]
    # game_keys = ['date', 'time', 'game', 'score', 'home_odds', 'draw_odds', 'away_odds', 'country', 'league']
    for row in generate_matches(soup, defaultVal=nan):
        for k in game_keys: getattr(game_data, k).append(row.get(k, nan)) ## OR:
        # game_data.date.append(row.get('date'))
        # game_data.time.append(row.get('time'))
        # game_data.game.append(row.get('game'))
        # game_data.score.append(row.get('score'))
        # game_data.home_odds.append(row.get('home_odds'))
        # game_data.draw_odds.append(row.get('draw_odds'))
        # game_data.away_odds.append(row.get('away_odds'))
        # game_data.country.append(row.get('country'))
        # game_data.league.append(row.get('league'))

    if return_urls: ## as before
        span = soup.find('span', {'class': 'next-games-date'}) ## as before
        a_tags = span.findAll('a') ## as before
        urls = ['https://www.oddsportal.com' + a_tag['href'] for a_tag in a_tags] ## as before
        return game_data, urls ## as before
    return game_data ## as before
```

---

#### EDIT: Suggested Changes to Main Block

[ Main change is how the DataFrame is built up, since [`DataFrame.append`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.append.html) has been deprecated. ]

```python
if __name__ == '__main__':
    games = None ## AS BEFORE
    pool = ThreadPool(5) ## AS BEFORE
    url_today = 'https://www.oddsportal.com/matches/soccer' # [just shortens line]
    game_data_today, urls = pool.apply(parse_data, args=(url_today, True)) 
    # urls.pop(1)  ## [ no longer needed ]
    game_data_results = pool.imap(parse_data, urls)  ## AS BEFORE

    ############################ BUILD  DATAFRAME ############################
    game_data_dfList, added_todayGame = [], False
    for game_data in game_data_results:
        try:
            game_data_dfList.append(pd.DataFrame(game_data.__dict__)) 
            if not added_todayGame:
                game_data_dfList += [pd.DataFrame(game_data_today.__dict__)]
                added_todayGame = True
        except Exception as e:
            game_n = len(game_data_dfList) + 1
            print(f'Error tabulating game_data_df#{game_n}:\n{repr(e)}')
        # finally: pass ## [ redundant ] 
    try: games = pd.concat(game_data_dfList, ignore_index=True)
    except Exception as e: print('Error concatenating DataFrames:', repr(e))
    ##########################################################################

    print('!?NO GAMES?!' if games is None else games) ## print(games)
    # ensure all the drivers are "quitted": ## AS BEFORE
    del threadLocal ## AS BEFORE
    import gc ## AS BEFORE

    gc.collect()  # a little extra insurance ## AS BEFORE
```

You could also add to the final DataFrame one by one (instead of [concatenating](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) them all at once in the end) by replacing the *`# BUILD  DATAFRAME #`* block above with

```python
    game_n, added_todayGame = 0, False
    for game_data in game_data_results:
        try:
            game_n += 1
            gd_df = pd.DataFrame(game_data.__dict__)
            games = gd_df if games is None else pd.concat([games, gd_df])
            if not added_todayGame:
                game_n += 1
                gdt_df = pd.DataFrame(game_data_today.__dict__)
                games, added_todayGame = pd.concat([games, gdt_df]), True
        except Exception as e:
            print(f'Error tabulating game_data_df#{game_n}:\n{repr(e)}') 
```


  [1]: https://i.sstatic.net/wei25.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-13): Thank you. Where in the above code would I replace yours to get the dataframe?
- **me** (2023-01-13): You could wrap my code in `def generate_matches(soup)` and `return events`,  and then right after *`soup = bs(browser.page_source, "lxml")`* iterate through the events with *`for row in generate_matches(soup)...`* like `game_data.date.append(row.get('date'))` and `game_data.time.append(row.get('time'))` and so on
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-28): Apologies for a late response however I dont quite follow your advice about wrapping. Can you please update the parent code with your answer?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-29): Thank you!. I edited my code including your inputs [please find entire code here](https://pastebin.com/nF47vSwE) however I am getting an error at line 92 `a_tags = span.findAll('a') AttributeError: 'NoneType' object has no attribute 'findAll'` How do I correct this error?
- **me** (2023-01-29): @Rander it's because *`soup.find('span', {'class': 'next-games-date'})`* returned `None` - either test for that (something like `a_tags = [] if span is None else span.find_all('a')`) or use `.select` instead of `.find...` like **`a_tags = soup.select('span.next-games-date a[href]')`**
- **me** (2023-01-29): Again, I highly recommend learning about CSS selectors - chaining multiple `.find...` calls often leads to this `AttributeError`. [ For single elements, you should also check against `None` before trying to extract text or any attribute - like I did with *`v.get_text(' ').strip() if v else defaultVal`* and *`evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal`* ]
- **me** (2023-02-02): @Rander edited code lines are marked with `## EDIT`
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-05): Thanks thats great! I noticed a few things. Please find an [explanation for the points here](https://imgur.com/a/Krzewlx). Namely, 1. The extracts are for all the pages except the landing page. I used `pd.DataFrame(urls)` to get this. 2. For some reason, the site is resisting scraping. Different runs yield different `count` of rows for `games`. Is there a better way than `browser.implicitly_wait(25)`? I tried `browser.implicitly_wait(50)` but the run time remains the same. Probably the statement can be optimally placed?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-05): I am sorry, I am not getting enough time to test all of this very diligently however, I will open source this solution on github when I get it working correctly as Oddsportal is one of the most scraped sites for betting odds and many of the packages (repos) are failing due to the redesign. Your work will go a long way to help everybody!
- **me** (2023-02-05): @Rander I guess you could try an [explicit wait](https://selenium-python.readthedocs.io/waits.html#explicit-waits) instead (like `WebDriverWait(browser, 30).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[set]>div:last-child a:has(a[title])~div:not(.hidden)")))` is supposed to wait till all the odds are loaded) but I'm not really sure...have you checked on your browser that the site content itself doesn't vary?
- **me** (2023-02-05): btw, in your `for i in range(8)...` loop, why is there a `try...except` with what looks like identical `try` and `except` blocks?
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-02-05): Yes, I can try `explicit wait` where would I put this statement? Replace `implicitly wait`? I will check the same. I did not cause of the `headless` option enabled. Will test all your points and respond tomorrow. (Typing from phone). As you can tell, my CSS and HTML scripting skills are abysmal to quite follow your questions. I had built this code from SO help. I am a data analyst myself hence the incompetence. I honestly apologise.
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-06): Thank you @Driftr95 for the answer. I see the same issue as the browser does not load fully . I am trying to replace `browser.implicitly_wait(25)` with `WebDriverWait(browser, 30).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[set]>div:last-child a:has(a[title])~div:not(.hidden)")))` however, what would `EC` be in part `until( EC.presence_of_all_elements...` stand for? Also, how would I modify the code to include Rander's point of "Todays Matches" in the extract? I guess the `for i in range(8)` part was for the 8 `a_tags` collected however they dont seem to be the case now.
- **me** (2023-02-06): @leonardo please see the imports in the first example in the [explicit waits documentation](https://selenium-python.readthedocs.io/waits.html#explicit-waits) - both `EC` (*`selenium.webdriver.support.expected_conditions`*) and `WebDriverWait` (*`selenium.webdriver.support.wait.WebDriverWait`*) are imported classes/sub-packages (as is `By`).
- **me** (2023-02-06): About the *`for i in range(8)`* I'm not entirely sure why they wouldn't apply any more, but I've suggested some alterations (see *`EDIT: Suggested Changes to Main Block`*) although I'm not confident in it at all as I have very little experience with thread pools
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-07): You are doing great work! I have [compiled the code as per your suggestions here](https://pastebin.com/RYnbGC8Y). While I understand the [Explicit Wait](https://selenium-python.readthedocs.io/waits.html#explicit-waits) exists, I really dont know where to apply the same in the code. Can you please help me insert the part in the code? Also, The dataframe is being constructed twice. i.e. the code loops twice. How can I correct the same?
- **me** (2023-02-08): @leonardo what happens when you replace *`browser.implicitly_wait(25)`* with `WebDriverWait(browser, 30).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[set]>div:last-child a:has(a[title])~div:not(.hidden)")))`? Is there an error raised?
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-09): No, there is no error raised however I noticed when I disabled `self.driver.quit()` and `del threadLocal` the page does not load fully. The scraped data is just of the visible dataframe which is quite short. After scrolling the page manually, the page continues to load till the end (there is no indefinite scrolling which I noticed as the matches and odds are timestamped so new date is displayed on the respective page) which can explain why `EC` could not be helpful here. Can you help introduce scrolling using `webdriver` and `selenium` for `n` seconds and then build the dataframe?
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-09): So I tried `browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")`  [following this solution](https://stackoverflow.com/questions/63532066/fix-lazy-loading-in-selenium-python) for scrolling the page which helped get more data but the scrolling stopped at 1. Usually on weekends, there are thousands of events and hence maybe the scroll has to happen 30-50 times the `document.body.scrollHeight` so I tried `browser.execute_script("window.scrollTo(10, document.body.scrollHeight);")`  but it stopped at 1 only. Can you help me understand this and help scroll the page more times?
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-09): This is great progress! I cannot thank you enough for the progress so far!
- **me** (2023-02-09): @leonardo are you scrolling in a loop? The first parameter of [`window.scrollTo`](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo) is just an x-coordinate, so manipulating it will make no difference to the number of times it scrolls - for that you'll need to loop, and you should add some delay inside the loop to allow new data to load, just like in the solution you mentioned
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-09): Can you please help me write the loop? I really appreciate it!
- **me** (2023-02-09): @leonardo this covers it quite well:   https://stackoverflow.com/a/27760083/6146136
- **[leonardo](https://stackoverflow.com/users/16949484)** (2023-02-10): Super Sweet my man! Now I am getting a consistent result. I would not for the life of me had figured out about scrolling and infinite loading pages if it were not for you! You are literally godsend! Bless you man! Can you please post [this code as the final answer](https://pastebin.com/Sd0E1Hmm) considering that the code is as efficiently built as it can be? This should be accepted. @Rander the code works now.
- **me** (2023-02-10): @leonardo I've only edited in the link to it [but it's right at the top] since this question is about a bs4-related error. I'm glad to hear that a working solution has been reached!
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-03-15): @Driftr95 I guess the website changed a bit. Can you please help answer [this question](https://stackoverflow.com/questions/75740238/missing-values-while-scraping-oddsportal-using-beautifulsoup)?

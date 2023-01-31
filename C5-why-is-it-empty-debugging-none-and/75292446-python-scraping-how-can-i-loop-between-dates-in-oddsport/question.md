---
title: "python scraping - How can I Loop between Dates in OddsPortal"
site: stackoverflow
question_id: 75292446
url: https://stackoverflow.com/q/75292446
asked: 2023-01-31T03:30:01Z
asked_by: "Rander"
asked_by_url: https://stackoverflow.com/users/19267166
last_edited: 2023-01-31T23:43:02Z
tags: [python, web-scraping, beautifulsoup]
score: 3
views_at_snapshot: 651
answer_count: 2
accepted_answer_id: 75305011
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6159f30e54e05b71e7ae2532f8a509c05e73f3e6893fd285b08fdb7728749ed5
---

# python scraping - How can I Loop between Dates in OddsPortal

Asked by [Rander](https://stackoverflow.com/users/19267166) on Stack Overflow, <https://stackoverflow.com/q/75292446>, 2023-01-31, last edited 2023-01-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape Oddsportal and the below code however when I run it, I get `IndexError`

Code:

    import threading
    from datetime import datetime
    from math import nan
    from multiprocessing.pool import ThreadPool
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver
    
    
    
    class Driver:
        def __init__(self):
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            # Un-comment next line to supress logging:
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Chrome(options=options)
    
        def __del__(self):
            self.driver.quit()  # clean up driver when we are cleaned up
            # print('The driver has been "quitted".')
    
    
    threadLocal = threading.local()
    
    
    def create_driver():
        the_driver = getattr(threadLocal, 'the_driver', None)
        if the_driver is None:
            the_driver = Driver()
            setattr(threadLocal, 'the_driver', the_driver)
        return the_driver.driver
    
    
    class GameData:
        def __init__(self):
            self.date = []
            self.time = []
            self.game = []
            self.score = []
            self.home_odds = []
            self.draw_odds = []
            self.away_odds = []
            self.country = []
            self.league = []
    
    
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
        for evt in pgSoup.select('div[set]>div:last-child'):
            if evt.parent.select(f':scope>div:first-child+div+div'):
                cgVals = [v.get_text(' ').strip() if v else defaultVal for v in [
                    evt.parent.select_one(s) for s in
                    [':scope>div:first-child+div>div:first-child',
                     ':scope>div:first-child>a:nth-of-type(2):nth-last-of-type(2)',
                     ':scope>div:first-child>a:nth-of-type(3):last-of-type']]]
                current_group = dict(zip(['date', 'country', 'league'], cgVals))
    
            evtRow = {'date': current_group.get('date', defaultVal)}
            for k, v in evtSel.items():
                v = evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal
                evtRow[k] = ' '.join(v.split()) if isinstance(v, str) else v
            evtRow['country'] = current_group.get('country', defaultVal)
            evtRow['league'] = current_group.get('league', defaultVal)
    
            events.append(evtRow)
        return events
    
    
    def parse_data(url, return_urls=False):
        browser = create_driver()
        browser.get(url)
        browser.implicitly_wait(25)
        soup = bs(browser.page_source, "lxml")
    
        game_data = GameData()
        game_keys = [a for a, av in game_data.__dict__.items() if isinstance(av, list)]
        for row in generate_matches(soup, defaultVal=nan):
            for k in game_keys: getattr(game_data, k).append(row.get(k, nan))
        if return_urls:
            span = soup.find('span', {'class': 'next-games-date'})
            a_tags = soup.select('span.next-games-date a[href]') # Instead of a_tags = soup.select('span.next-games-date a[href]')
            urls = ['https://www.oddsportal.com' + a_tag['href'] for a_tag in a_tags]
            return game_data, urls
        return game_data
    
    
    if __name__ == '__main__':
        games = None
        pool = ThreadPool(5)  # We will be getting, however, 7 URLs
        # Get today's data and the Urls for the other days:
        game_data_today, urls = pool.apply(parse_data, args=('https://www.oddsportal.com/matches/soccer', True))
        urls.pop(1)  # Remove url for today: We already have the data for that
        game_data_results = pool.imap(parse_data, urls)
        for i in range(8):
            try:
                game_data = game_data_today if i == 1 else next(game_data_results)
                result = pd.DataFrame(game_data.__dict__)
                if games is None:
                    games = result
                else:
                    games = games.append(result, ignore_index=True)
            except ValueError:
                game_data = game_data_today if i == 1 else next(game_data_results)
                result = pd.DataFrame(game_data.__dict__)
                if games is None:
                    games = result
                else:
                    games = games.append(result, ignore_index=True)
            finally:
                pass
        # print(games)
        # ensure all the drivers are "quitted":
        del threadLocal
        import gc
    
        gc.collect()  # a little extra insurance

Error:

      File "C:\Users\User\AppData\Roaming\JetBrains\PyCharmCE2022.1\scratches\scratch_1.py", line 114, in <module>
        urls.pop(1)  # Remove url for today: We already have the data for that
    IndexError: pop from empty list



While the looping is to scrape between dates available, I am unable to get it to work in entirety.



[![Loop Between Dates][2]][2]

I dont want to check for `a_tags = [] if span is None else span.find_all('a')` as it does not serve my purpose

This part of the code:

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
        for evt in pgSoup.select('div[set]>div:last-child'):
            if evt.parent.select(f':scope>div:first-child+div+div'):
                cgVals = [v.get_text(' ').strip() if v else defaultVal for v in [
                  evt.parent.select_one(s) for s in 
                  [ ':scope>div:first-child+div>div:first-child',
                    ':scope>div:first-child>a:nth-of-type(2):nth-last-of-type(2)',
                    ':scope>div:first-child>a:nth-of-type(3):last-of-type' ]]]
                current_group = dict(zip(['date', 'country', 'league'], cgVals))
            
            evtRow = {'date': current_group.get('date', defaultVal)}
            for k, v in evtSel.items():
                v = evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal
                evtRow[k] = ' '.join(v.split()) if isinstance(v, str) else v
            evtRow['country'] = current_group.get('country', defaultVal)
            evtRow['league'] = current_group.get('league', defaultVal)
    
            events.append(evtRow)
        return events

collects

[![pandas.DataFrame(events)][1]][1]


Edit: Changed `a_tags = soup.select('span.next-games-date a[href]')` to `a_tags = soup.select('span.next-games-date a[href]')`


  [1]: https://i.sstatic.net/FqZ2y.png
  [2]: https://i.sstatic.net/JjS1x.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-02-01): Just a note: if there's a chance of the list not having the index you're about to `pop` from, do something like `if len(urls)>1: urls.pop(1)`; you can print a warning in `else:..` so that you'll know there's something missing, but at least you won't lose the data gathered until then due to the program crashing. Ofc, your actual issue is probably that the list is empty at all - hopefully, my answer resolves that

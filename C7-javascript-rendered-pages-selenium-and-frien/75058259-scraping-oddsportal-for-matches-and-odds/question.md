---
title: "Scraping Oddsportal for Matches and odds"
site: stackoverflow
question_id: 75058259
url: https://stackoverflow.com/q/75058259
asked: 2023-01-09T13:52:41Z
asked_by: "Rander"
asked_by_url: https://stackoverflow.com/users/19267166
last_edited: 2023-01-09T20:46:34Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 1365
answer_count: 1
accepted_answer_id: 75101673
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1d5f7d02d99239d37c3fffe2c869a946ef237ae061ca5fdd0f7e7a2a1c08c89f
---

# Scraping Oddsportal for Matches and odds

Asked by [Rander](https://stackoverflow.com/users/19267166) on Stack Overflow, <https://stackoverflow.com/q/75058259>, 2023-01-09, last edited 2023-01-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Code used to scrape Oddsportal however now I am getting an error with this code.

    import os
    import re
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
            print('The driver has been "quitted".')
    
    
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
    
    
    def generate_matches(table):
        tr_tags = table.findAll('tr')
        for tr_tag in tr_tags:
            if 'class' in tr_tag.attrs and 'dark' in tr_tag['class']:
                th_tag = tr_tag.find('th', {'class': 'first2 tl'})
                a_tags = th_tag.findAll('a')
                country = a_tags[0].text
                league = a_tags[1].text
            else:
                td_tags = tr_tag.findAll('td')
                if len(td_tags) > 5:  # or just if td_tags
                    yield [td_tags[0].text, td_tags[1].text, td_tags[2].text, td_tags[3].text,
                           td_tags[4].text, td_tags[5].text, country, league]
    
    
    def parse_data(url, return_urls=False):
        browser = create_driver()
        browser.get(url)
        browser.implicitly_wait(25)
        soup = bs(browser.page_source, "lxml")
        div = soup.find('div', {'id': 'col-content'})
        table = div.find('table', {'class': 'table-main'})
        h1 = soup.find('h1').text
        print(h1)
        m = re.search(r'\d+ \w+ \d{4}$', h1)
        game_date = m[0]
        game_data = GameData()
        for row in generate_matches(table):
            game_data.date.append(game_date)
            game_data.time.append(row[0])
            game_data.game.append(row[1])
            # Score present?
            if ':' not in row[2]:
                # No, shift a few columns right:
                row[5], row[4], row[3], row[2] = row[4], row[3], row[2], nan
            game_data.score.append(row[2])
            game_data.home_odds.append(nan if row[3] == '-' else row[3])
            game_data.draw_odds.append(nan if row[4] == '-' else row[4])
            game_data.away_odds.append(nan if row[5] == '-' else row[5])
            game_data.country.append(row[6])
            game_data.league.append(row[7])
    
        if return_urls:
            span = soup.find('span', {'class': 'next-games-date'})
            a_tags = span.findAll('a')
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
        print(games)
        # ensure all the drivers are "quitted":
        del threadLocal
        import gc
    
        gc.collect()  # a little extra insurance

Model Output:

    Unnamed: 0         date   time                                               game     score home_odds  draw_odds  away_odds                country                               league
    0              0  08 Jan 2023  00:30                       Boca Juniors - Independiente       0:0      1.93       3.23       3.91              Argentina                    Torneos De Verano
    1              1  08 Jan 2023  00:45                            CSP U20 - Sao Paulo U20       0:4     11.27       5.85       1.21                 Brazil           Copa Sao Paulo de juniores
    2              2  08 Jan 2023  01:00               U. de Deportes (Per)  - Aucas (Ecu)        0:0      1.94       3.28       3.74                  World                        Club Friendly
    3              3  08 Jan 2023  01:10                                     Atlas - Toluca       NaN    postp.       2.04       3.40                 Mexico                              Liga MX
    4              4  08 Jan 2023  01:30            Inac Kobe Leonesa W - Albirex Niigata W       2:1      1.22       5.42      12.01                  Japan                      WE League Women
    5              5  08 Jan 2023  02:00                        Tampico Madero - Lobos ULMX       1:0      1.41       4.69       6.25                 Mexico                 Liga Premier Serie A

However currently I am getting error:

    Traceback (most recent call last):
      File "C:\Users\User\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\Scraping_New.py", line 111, in <module>
        game_data_today, urls = pool.apply(parse_data, args=('https://www.oddsportal.com/matches/soccer', True))
      File "C:\Program Files\Python37\lib\multiprocessing\pool.py", line 261, in apply
        return self.apply_async(func, args, kwds).get()
      File "C:\Program Files\Python37\lib\multiprocessing\pool.py", line 657, in get
        raise self._value
      File "C:\Program Files\Python37\lib\multiprocessing\pool.py", line 121, in worker
        result = (True, func(*args, **kwds))
      File "C:\Users\User\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\Scraping_New.py", line 78, in parse_data
        table = div.find('table', {'class': 'table-main'})
    AttributeError: 'NoneType' object has no attribute 'find'

How do I resolve this?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-09): @qharr can you please help me resolve the error?
- **me** (2023-01-09): if you just want to avoid the error, add a line with `if not div: return []` before the *`table = div.find....`* line. If you want to save some information to try to figure out what caused the `div` to be missing, you can use something like this [`logError_scrapes`](https://pastebin.com/cxGH50Mc) function [*`if not div: return logError_scrapes('', url, msg=f"table container div#col-content not found", rSoup=soup, conf={'reqUrl':browser.current_url}, returnVal=[])`*]
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-10): I dont want to avoid the error. This code worked before and since the website did a redesign, I am unable to ron the same. When I run `rows = table.find_all("tr")` I get the error _rows = table.find_all("tr") AttributeError: 'NoneType' object has no attribute 'find_all'_
- **me** (2023-01-10): The error happens because the fetched html doesn't contain the table you're looking for. If some sites just don't have the table, then you can just skip (that's what I meant by avoiding the error), if ALL sites raise the error then you need to rewrite your scraper, and if some sites raise the error and some don't *and you're not sure why* that's when you use something like the function I mentioned previously to log the sites that raised the error (so you can go back and try to figure out why) and the program can still continue collecting as much data as possible from the non-problematic sites
- **[Rander](https://stackoverflow.com/users/19267166)** (2023-01-11): How do I get values in the dataframe? If you could help me with one of the dataframe value positions, I will figure out the rest.. (I hope). E.g. game column value

---
title: "missing values while scraping Oddsportal using beautifulsoup"
site: stackoverflow
question_id: 75740238
url: https://stackoverflow.com/q/75740238
asked: 2023-03-15T03:19:19Z
asked_by: "PyNoob"
asked_by_url: https://stackoverflow.com/users/14833958
last_edited: 2023-03-15T16:49:53Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, pandas, dataframe, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 487
answer_count: 1
accepted_answer_id: 75747651
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6382cf43d406061198fc614bc58b59513fbf3bff1d32fed39fe58822156a7a07
---

# missing values while scraping Oddsportal using beautifulsoup

Asked by [PyNoob](https://stackoverflow.com/users/14833958) on Stack Overflow, <https://stackoverflow.com/q/75740238>, 2023-03-15, last edited 2023-03-15 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

This scraper scrapes a dataframe from [https://www.oddsportal.com/matches/football/][1] like the below dataframe:

scraper:

    import os
    import time
    import threading
    import pandas as pd
    from math import nan
    from multiprocessing.pool import ThreadPool
    from bs4 import BeautifulSoup as bs
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    
    
        class Driver:
        def __init__(self):
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
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
        pgDate = pgSoup.select_one('h1.title[id="next-matches-h1"]')
        if pgDate: pgDate = pgDate.get_text().split(',', 1)[-1].strip()
        for evt in pgSoup.select('div[set]>div:last-child'):
            if evt.parent.select(f':scope>div:first-child+div+div'):
                cgVals = [v.get_text(' ').strip() if v else defaultVal for v in [
                    evt.parent.select_one(s) for s in
                    [':scope>div:first-child+div>div:first-child',
                     ':scope>div:first-child>a:nth-of-type(2):nth-last-of-type(2)',
                     ':scope>div:first-child>a:nth-of-type(3):last-of-type']]]
                current_group = dict(zip(['date', 'country', 'league'], cgVals))
                if pgDate: current_group['date'] = pgDate
    
            evtRow = {'date': current_group.get('date', defaultVal)}
    
            for k, v in evtSel.items():
                v = evt.select_one(v).get_text(' ') if evt.select_one(v) else defaultVal
                evtRow[k] = ' '.join(v.split()) if isinstance(v, str) else v
            evtTeams = evt.select('a div>a[title]')
            evtRow['game'] = ' – '.join(a['title'] for a in evtTeams)
            evtRow['country'] = current_group.get('country', defaultVal)
            evtRow['league'] = current_group.get('league', defaultVal)
    
            events.append(evtRow)
        return events
    
    
    def parse_data(url, return_urls=False):
        browser = create_driver()
        browser.get(url)
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[set]>div:last-child a:has(a[title])~div:not(.hidden)")))
        # ########## For page to scroll to the end ###########
        scroll_pause_time = 2
    
        # Get scroll height
        last_height = browser.execute_script("return document.body.scrollHeight")
    
        while True:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
            # Wait to load page
            time.sleep(scroll_pause_time)
    
            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        # ########## For page to scroll to the end ###########
        time.sleep(5)
        soup = bs(browser.page_source, "lxml")
    
        game_data = GameData()
        game_keys = [a for a, av in game_data.__dict__.items() if isinstance(av, list)]
        for row in generate_matches(soup, defaultVal=nan):
            for k in game_keys: getattr(game_data, k).append(row.get(k, nan))
        if return_urls:
            if return_urls:
                a_cont = soup.find('div', {'class': 'tabs'})
                if a_cont is None:
                    a_tags = []
                else:
                    a_tags = a_cont.find_all('a', {'class': 'h-8', 'href': True})
                urls = [
                    'https://www.oddsportal.com' + a_tag['href'] for a_tag in a_tags
                    if not a_tag['href'].startswith('#')  # sections in current page
                    and 'active-item-calendar' not in a_tag['class']  # current page
                ]
                print(pd.DataFrame(urls, columns=['urls']))  # If you want to see the URLs then uncomment this line else, comment it out.
            return game_data, urls
        return game_data
    
    
    if __name__ == '__main__':
        games = None
        pool = ThreadPool(5)
        # Get today's data and the Urls for the other days:
        url_today = 'https://www.oddsportal.com/matches/soccer'
        game_data_today, urls = pool.apply(parse_data, args=(url_today, True))
        game_data_results = pool.imap(parse_data, urls)
        # ############################ BUILD  DATAFRAME 
    
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
        try:
            games = pd.concat(game_data_dfList, ignore_index=True)
        except Exception as e:
            print('Error concatenating DataFrames:', repr(e))
        # #########################################################################
        print('!?NO GAMES?!' if games is None else games)
        # ensure all the drivers are "quitted":
        del threadLocal  # a little extra insurance
        import gc
    
        gc.collect()
    
    games.to_csv()
    
    
    df:
    
    |    | date        | time   | game                        | score   |   home_odds |   draw_odds |   away_odds | country                | league              |
    |---:|:------------|:-------|:----------------------------|:--------|------------:|------------:|------------:|:-----------------------|:--------------------|
    |  0 | 13 Mar 2023 | 00:00  | Mrkonjic Grad – Kozara      | 2:2     |        1.94 |        3.42 |        3.42 | Bosnia and Herzegovina | Prva Liga - RS      |
    |  1 | 13 Mar 2023 | 00:00  | Patrocinense – Democrata SL | 2:0     |        2.01 |        3.12 |        3.74 | Brazil                 | Campeonato Mineiro  |
    |  2 | 13 Mar 2023 | 00:00  | Cameta – Bragantino         | 2:0     |        2.2  |        3.15 |        3.05 | Brazil                 | Campeonato Paraense |
    |  3 | 13 Mar 2023 | 00:00  | Tonnerre – Aigle Moungo     | 1:1     |        3.3  |        3.2  |        2.16 | Cameroon               | Elite Two           |
    |  4 | 13 Mar 2023 | 00:00  | Vendsyssel – Sonderjyske    | 2:3     |        2.73 |        3.44 |        2.4  | Denmark                | 1st Division        |


However, instead of getting just 7 URLs from [![desired urls][2]][2]
from


    if return_urls:
    if return_urls:
    a_cont = soup.find('div', {'class': 'tabs'})
    if a_cont is None:
    a_tags = []
    else:
    a_tags = a_cont.find_all('a', {'class': 'h-8', 'href': True})
    urls = [
                    'https://www.oddsportal.com' + a_tag['href'] for a_tag in a_tags
    if not a_tag['href'].startswith('#')  # sections in current page
    and 'active-item-calendar' not in a_tag['class']  # current page
                ]

I am however getting the calendar list of urls i.e. 41 urls in this case which is not desired.

Also, the dataframe scraped is missing score values.

[![scores][3]][3]

While the current output is:

|| date        | time   | game                                    |   score |   home_odds |   draw_odds |   away_odds | country   | league                |
|---:|:------------|:-------|:----------------------------------------|--------:|------------:|------------:|------------:|:----------|:----------------------|
0 | 27 Feb 2023 | 00:00  | St Eloi Lupopo (Drc)  – Al Akhdar (Lby) |     nan |        1.61 |        3.5  |        5.62 | Africa    | CAF Confederation Cup |
1 | 27 Feb 2023 | 00:00  | Mazembe (Drc)  – Monastir (Tun)         |     nan |        1.54 |        3.5  |        7.36 | Africa    | CAF Confederation Cup |
2 | 27 Feb 2023 | 00:00  | Sao Francisco – Tapajos                 |     nan |        3.55 |        3.33 |        1.99 | Brazil    | Campeonato Paraense   |
3 | 27 Feb 2023 | 00:00  | Inter Star – Dynamik                    |     nan |        1.83 |        3.24 |        4.33 | Burundi   | Primus League         |
4 | 27 Feb 2023 | 00:00  | Vital'O – Kayanza                       |     nan |        1.49 |        4.04 |        5.97 | Burundi   | Primus League         |


How can I get the correct URLs and the columns correctly populated?


  [1]: https://www.oddsportal.com/matches/football/
  [2]: https://i.sstatic.net/34Hn2.png
  [3]: https://i.sstatic.net/UcX3W.png

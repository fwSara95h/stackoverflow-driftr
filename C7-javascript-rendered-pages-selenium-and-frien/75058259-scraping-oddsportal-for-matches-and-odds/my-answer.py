# Code from my Stack Overflow answer https://stackoverflow.com/a/75101673 (posted 2023-01-12), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
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

# --- block 4 ---
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

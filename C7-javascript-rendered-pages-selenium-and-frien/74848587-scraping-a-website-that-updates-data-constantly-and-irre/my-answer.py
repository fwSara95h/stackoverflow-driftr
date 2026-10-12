# Code from my Stack Overflow answer https://stackoverflow.com/a/74926301 (posted 2022-12-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
# wait = WebDriverWait(driver, maxWait) 

        thSel = 'table:has(th.text-center) tbody'
        if isinstance(wAmt, int) and 1 < wAmt < 39:
            thSel = f'{thSel}>tr:nth-child({wAmt})~tr>td:first-child'
        else: thSel = f'{thSel}>tr:first-child~tr>td:first-child'
        wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, f'{thSel}>a[href="{thref}"]')))
    # except: tmoCt += 1

# --- block 3 ---
if isinstance(wAmt, float):
    if not gData: # only wait if there's no new data
        time.sleep(wAmt)
    continue # skip rest of loop

# try....except: tmoCt += 1

# --- block 4 ---
addedIds, games, thref = [], [], '' # initiated outside loop

# and then inside the loop:
    tGames = [t for t in tGames if t['game_id'] not in addedIds] # filter out duplicates

    games += tGames # add to main list

# [main list (games) saved after loop]

# --- block 5 ---
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

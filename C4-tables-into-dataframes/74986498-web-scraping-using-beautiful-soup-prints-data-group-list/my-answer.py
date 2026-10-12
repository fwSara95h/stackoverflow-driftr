# Code from my Stack Overflow answer https://stackoverflow.com/a/74988076 (posted 2023-01-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[
  (name0, pers0, all_splits_0_LIST),
  (name1, pers1, all_splits_1_LIST),
  (name2, pers2, all_splits_2_LIST),
  ## AND SO ON...
]

# --- block 2 ---
names_stats = pd.DataFrame([tuple([n, p] + s) for n, p, s in zip(names_list, pers, statslist)])

# --- block 3 ---
def GetStats(statsurl):
    statsreq = requests.get(statsurl)
    statssoup = BeautifulSoup(statsreq.text, 'lxml')
    t = statssoup.select('main#fittPageContainer div.Table__Scroller > table > tbody')
    all_splits = [h.text for h in t[0].find_all('tr')[1].find_all('td')]
    split_list = [elem.split() for elem in all_splits]

    pers = statsurl.split('/id/', 1)[-1].split('.', 1)[0]
    yr = statsurl.split('/year/', 1)[-1].split('.', 1)[0]
    # name = statssoup.select_one('h1.PlayerHeader__Name').get_text(' ').strip() # not as safe as:
    name = ' '.join([n.get_text(' ').strip() for n in statssoup.select('h1.PlayerHeader__Name') if n.get_text().strip()])
    statslist.append([name, yr, pers] + split_list)

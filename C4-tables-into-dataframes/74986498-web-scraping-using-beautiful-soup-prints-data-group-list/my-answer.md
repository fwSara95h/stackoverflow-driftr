---
title: "Web Scraping Using Beautiful Soup (prints data group listed into one cell instead of across individual cells)"
site: stackoverflow
question_id: 74986498
answer_id: 74988076
url: https://stackoverflow.com/a/74988076
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-03T00:08:18Z
last_edited: 2023-01-03T00:24:33Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74988076/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 031e4336591b2aab61a676d833865f5e083b042e5c9dfd0e3a8ea21c599a365f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74988076>, 2023-01-03, last edited 2023-01-03; score 0. Text as retrieved 2026-10-12.

I think the issue is that `names_list` and `pers` are flat lists but `statslist` is list of lists, so just zipping the 3 together directly results in a list of tuples like 

```python
[
  (name0, pers0, all_splits_0_LIST),
  (name1, pers1, all_splits_1_LIST),
  (name2, pers2, all_splits_2_LIST),
  ## AND SO ON...
]
```

instead you might want to do something like

```python
names_stats = pd.DataFrame([tuple([n, p] + s) for n, p, s in zip(names_list, pers, statslist)])
```

---

I don't think zipping separately obtained lists together is the best way to ensure that the right data is matched up to the right name...wouldn't it be be more reliable to get the name and person# from `statssoup` and `statsurl`?

```python
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
```

and then you can just form the DataFrame with **`names_stats = pd.DataFrame(statslist)`**.

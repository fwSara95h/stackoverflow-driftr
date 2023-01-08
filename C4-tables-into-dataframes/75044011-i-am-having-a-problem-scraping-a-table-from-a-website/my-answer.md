---
title: "I am having a problem scraping a table from a website"
site: stackoverflow
question_id: 75044011
answer_id: 75045322
url: https://stackoverflow.com/a/75045322
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T03:29:24Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75045322/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9ce361b60f05b04e11dd0838001bfdb7e6d5a7eb9183ed2946649a0a76102dec
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75045322>, 2023-01-08; score 0. Text as retrieved 2026-10-12.

> **Output:**
> 
> ```
> In[28]: runfile('/Users/dannyscott/Documents/Python Web Scraping/discord bot code V1.py', wdir='/Users/dannyscott/Documents/Python Web Scraping')
> ```
> ```
> In[29]: table
> ```

These don't look like outputs - they look more like commands from the console [or something] that just don't have any outputs. Speaking of which, if you run code with one output and have multiple  statements that return something [like just `page.text`/`soup`/`table` in your code], then only the last statement's return will  show up. If you want to view them all, you should [`print`](https://www.w3schools.com/python/ref_func_print.asp) them instead.

---

> **also, if I try to `table.find_all` , it will say *"'NoneType' object has no attribute 'find_all''"***

If you tried `print(table)` you would probably see nothing, but if you tried `print([table])` you might have seen **`[None]`** in the output; and that's also the reason for the error - no `table` with that class was found, and you can't apply `find...` to a null value.

---

> ```python
> table = soup.find('table', {'class' : "tablesaw tablesaw-swipe"})
> ```

When the expected element is not found, you can try widening the search with something like *`tables = soup.find_all('table')`* to [see all the tables](https://i.sstatic.net/8Zoz1.png) or just print the classes, row count and some of the text from each table with 

```python
for t in soup.find_all('table'): 
    rows = f"[{len(t.select('tr')):>2} rows]"
    txtPrevw = ' '.join(t.get_text(' ').split())
    if len(txtPrevw) > 100: txtPrevw = txtPrevw[:97] + '...'
    print(f"> {str(t.get('class')):>20}", rows, ' --> ', txtPrevw)
```

output:

> ```lang-none
>   ['game', 'played'] [ 5 rows]  -->  Final Score Boston (28-12) at San Antonio (13-27) 121 116 Box Score Regular Season
>       ['game_stats'] [ 1 rows]  -->  Box Score Regular Season
> ['game', 'unplayed'] [ 5 rows]  -->  8:00 PM ET Utah (20-21) at Chicago (18-21) Preview Regular Season
>       ['game_stats'] [ 1 rows]  -->  Preview Regular Season
> ['game', 'unplayed'] [ 5 rows]  -->  8:00 PM ET New Orleans (24-15) at Dallas (22-17) Preview Regular Season
>       ['game_stats'] [ 1 rows]  -->  Preview Regular Season
> ['game', 'unplayed'] [ 5 rows]  -->  8:30 PM ET Orlando (14-25) at Golden State (20-19) Preview Regular Season
>       ['game_stats'] [ 1 rows]  -->  Preview Regular Season
> ['game', 'unplayed'] [ 5 rows]  -->  10:00 PM ET L.A. Lakers (18-21) at Sacramento (20-17) Preview Regular Season
>       ['game_stats'] [ 1 rows]  -->  Preview Regular Season
>         ['tablesaw'] [31 rows]  -->  # Team GP MPG PPG FGM FGA FG% 3PM 3PA 3P% FTM FTA FT% ORB DRB RPG APG SPG BPG TOV PF 1 Boston 40 ...
> ```

---

I'm not sure if this is the one you were trying to get, but with **`soup.find('table', {'class' : "tablesaw"})`** you can get this table:

[![table.tablesaw][1]][1]



  [1]: https://i.sstatic.net/VJT7h.png

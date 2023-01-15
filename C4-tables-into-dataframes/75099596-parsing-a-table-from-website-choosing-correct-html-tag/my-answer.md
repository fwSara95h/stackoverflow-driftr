---
title: "Parsing a table from website (choosing correct HTML tag)"
site: stackoverflow
question_id: 75099596
answer_id: 75123132
url: https://stackoverflow.com/a/75123132
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-15T05:28:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75123132/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: [get_text with separator]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 60ac993f055896606464b367bfdf1a5e7fb813c801f780f5ff5342b4ef5f55ff
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75123132>, 2023-01-15; score 0. Text as retrieved 2026-10-12.

<sup>**NOTE:** you can get the table as a DataFrame in one statement with [`.read_html`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html), but the [DataFrame returned][1] by `pd.read_html('http://pitzavod.ru/products/upakovka/')[0]` will not retain line breaks.</sup>

*`.find('table', id="tab3")`* searches for **`table` tags with `id="tab3"`**, and there are no such elements in that page's HTML. 

There's a **`div`** with [`id="tab3"`][2] (as you've notice), *but it does not contain any tables*. 

The  [only table on the page][3] is contained in a `div` with **`id="tab4"`**, so you might have used *`table1 = soup.find('div', id="tab4").table`* [although I prefer using [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) for targeting nested tags].

---

Suggested solution:

```python
kre = requests.get('http://pitzavod.ru/products/upakovka/')
# print(kre.status_code, kre.reason, 'from', kre.url)
kre.raise_for_status()
soup = BeautifulSoup(kre.content, 'lxml')

# table = soup.select_one('div#tab4>div.table-responsive>table')
table = soup.find('table') # soup.select_one('table')
tData = [{
    1 if 'center' in c.get('style', '') else ci: '\n'.join([
        l.strip() for l in c.get_text('\n').splitlines() if l.strip()
    ]) for ci, c in enumerate(r.select('td'))
} for r in table.select('tr')]
df = pandas.DataFrame(tData)

## combine the top 2 rows to form header ##
df.columns = ['\n'.join([
    f'{d}' for d in df[c][:2] if pandas.notna(d)
]) for c in df.columns]
df = df.drop([0,1], axis='rows').reset_index(drop=True)

# print(df.to_markdown(tablefmt="fancy_grid"))
```

[![fop][4]][4]

<sub>(Normally, I would use [this function](https://pastebin.com/wQ0D6S3B) if I wanted to specify the separator for tag-contents inside cells, but the middle cell in the 2nd header row [would be shifted][5] if I used `.DataFrame(read_htmlTable(table, tSep='\n', asObj='dicts'))` - the *`1 if 'center' in c.get('style', '') else ci`* bit in the above code is for correcting that.)</sub>


  [1]: https://i.sstatic.net/yRDWm.png
  [2]: https://i.sstatic.net/ih7zh.png
  [3]: https://i.sstatic.net/MwmiX.png
  [4]: https://i.sstatic.net/Vnldi.png
  [5]: https://i.sstatic.net/e8RGZ.png

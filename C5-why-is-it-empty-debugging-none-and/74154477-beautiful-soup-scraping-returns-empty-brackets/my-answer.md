---
title: "Beautiful Soup Scraping returns empty brackets"
site: stackoverflow
question_id: 74154477
answer_id: 74159271
url: https://stackoverflow.com/a/74159271
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-21T21:22:47Z
last_edited: 2022-12-03T09:33:23Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74159271/revisions
accepted: false
score: 1
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6e64ea6f6a291b8736e4c9fd25320181ad96eefdb03a0a8889991b5c23846492
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74159271>, 2022-10-21, last edited 2022-12-03; score 1. Text as retrieved 2026-10-12.

There is no `table` with that id on that page; in fact, I don't think Wikipedia uses id attributes for their table elements at all. I believe you are trying to target [this table 🖥️][1], under the heading "Banks by Country or Territory" which is actually nested inside a `span` *with the id you're using* within in an `h3` element contained in the same parent element as the table.

So you can get it with 
```python
table = soup.find(
    'span', {'id': 'By_market_capitalization'}
).find_parent('h2').find_next_sibling('table')
```
but this uses 3 `find` calls, and therefore has 2 points where an error might be raised [if one of them returns `None`]; it might be better to instead use `select` with [css selectors](https://www.w3schools.com/cssref/css_selectors.asp) :
```python
table = soup.select_one('h2:has(span#By_market_capitalization) ~ table')
```

this would be very simple and easy to display with `pandas.read_html(str(table))[0]`, but you can also print it with

```python
colwidth = [10, 50, 30] # set column widths

for r in table.select('tr'):
  cells = [
      (c.text.strip()[:cw], cw) for c, cw 
      in zip(r.select('td,th'), colwidth)
  ]
  bottomBorder = ''
  if r.find('th'):
    bottomBorder = ' | '.join(['+'*c for c in colwidth])
    bottomBorder = f'\n| {bottomBorder} |'
  cells = ' | '.join([
      ("{0:^"+str(cw)+"}").format(c) for c, cw in cells
  ])
  print(f'| {cells} |{bottomBorder}')
```

Output:

```markdown
|    Rank    |                     Bank name                      |    Market cap(US$ billion)     |
| ++++++++++ | ++++++++++++++++++++++++++++++++++++++++++++++++++ | ++++++++++++++++++++++++++++++ |
|     1      |                   JPMorgan Chase                   |           400.37[6]            |
|     2      |      Industrial and Commercial Bank of China       |             295.65             |
|     3      |                  Bank of America                   |             279.73             |
|     4      |                    Wells Fargo                     |             214.34             |
|     5      |              China Construction Bank               |             207.98             |
|     6      |             Agricultural Bank of China             |             181.49             |
|     7      |                 HSBC Holdings PLC                  |             169.47             |
|     8      |                   Citigroup Inc.                   |             163.58             |
|     9      |                   Bank of China                    |             151.15             |
|     10     |                China Merchants Bank                |             133.37             |
|     11     |                Royal Bank of Canada                |             113.80             |
|     12     |               Toronto-Dominion Bank                |             106.61             |
|     13     |                     HDFC Bank                      |             105.9              |
|     14     |                 Commonwealth Bank                  |             99.77              |
|     15     |                    U.S. Bancorp                    |             84.40              |
|     16     |                   Goldman Sachs                    |             78.70              |
|     17     |                  Banco Santander                   |             75.47              |
|     18     |                   Banco Bradesco                   |             74.67              |
|     19     |                   Morgan Stanley                   |             73.93              |
|     20     |                      Westpac                       |             67.84              |
|     21     |           Mitsubishi UFJ Financial Group           |             66.20              |
|     22     |                     Scotiabank                     |             65.48              |
|     23     |               PNC Financial Services               |             63.11              |
|     24     |               Bank of Communications               |             61.85              |
|     25     |                    BNP Paribas                     |             59.36              |
|     26     |      Australia and New Zealand Banking Group       |             54.88              |
|     27     |              National Australia Bank               |             51.68              |
|     28     |                Lloyds Banking Group                |             51.19              |
|     29     |          Sumitomo Mitsui Financial Group           |             49.85              |
|     30     |                  Bank of Montreal                  |             48.12              |
|     31     |                        UBS                         |             45.92              |
|     32     |                     ING Group                      |             44.97              |
|     33     |                    Capital One                     |             43.22              |
|     34     |            The Bank of New York Mellon             |             42.58              |
|     35     |                China Minsheng Bank                 |             39.13              |
|     36     |                  China CITIC Bank                  |             38.55              |
|     37     |          Banco Bilbao Vizcaya Argentaria           |             37.42              |
|     38     |               Mizuho Financial Group               |             36.95              |
|     39     |                  Intesa Sanpaolo                   |             36.90              |
|     40     |                  Crédit Agricole                   |             34.89              |
|     41     |         Canadian Imperial Bank of Commerce         |             34.87              |
|     42     |               Royal Bank of Scotland               |             33.95              |
|     43     |                      Barclays                      |             33.26              |
|     44     |                   Credit Suisse                    |             30.75              |
|     45     |                       Nordea                       |             29.59              |
|     46     |                 Standard Chartered                 |             29.37              |
|     47     |                      KBC Bank                      |             27.40              |
|     48     |                     UniCredit                      |             26.88              |
|     49     |                  Société Générale                  |             21.27              |
|     50     |                   Deutsche Bank                    |             15.77              |
```


  [1]: https://i.sstatic.net/SVUzr.png

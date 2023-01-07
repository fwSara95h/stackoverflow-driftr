---
title: "How to scrape website with mouseover events and no class on most elements"
site: stackoverflow
question_id: 75037540
answer_id: 75037729
url: https://stackoverflow.com/a/75037729
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-07T02:31:02Z
last_edited: 2023-01-07T20:01:52Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75037729/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b80b38ac2912249580591512cc9ef5e700cc4763ac44e201da9b14420cc7e15f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75037729>, 2023-01-07, last edited 2023-01-07; **accepted**; score 0. Text as retrieved 2026-10-12.

#### Notes

It might be better to not use `list` as a variable name since it already means something in python....

Also, I can't test any of the suggestions below without having access to your HTML. It would be helpful if you include how you fetched the HTML to parse with BeautifulSoup. (Did you use some form of requests? Or something like selenium? Or do you just have the HTML file?) With requests or even selenium, sometimes the HTML fetched is not what you expected, so that's another issue...

---

#### The Reason behind the Issue

You can't apply `.text`/`.get_text` to the ResultSets (lists), which are what `.find_all` and `.select` return. You *can* apply `.text`/`.get_text` to Tags like the ones returned by **`.find`** or **`.select_one`** (but you should check first `None` was not returned - which happens when nothing is found). 

So `date[0].get_text()` might have returned something, but since you probably want all the dates and flags, that's not the solution. 

---

#### Solution Part 1 Option A: Getting the Rows with `.find...` chain

Instead of iterating through tables directly, you need to get the rows first (`tr` tags) before trying to get at the cells (`td` tags); if you have only one `table` with `class= "report"`, you could just do something like:

```python
rows = soup.find('table', class_= "report").find_all('tr',  {'onmouseover': True}) 
```

But it's risky to chain multiple `.find...`s like that, because an error will be raised if any of them return `None` before reaching the last one.

---

#### Solution Part 1 Option B: Getting the Rows More Safely with `.find...`

It would be safer to do something like

```python
table = soup.find('table', class_= "report")
rows = table.find_all('tr',  {'onmouseover': True}) if table else []
```

or, if there might be more than one `table` with `class= "report"`, 

```python
rows = []
for table in soup.find_all('table', class_= "report"): 
    rows += table.find_all('tr',  {'onmouseover': True})
```

---

#### Solution Part 1 Option C: Getting the Rows with `.select`

However, I think the most convenient way is to use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php)  

```python
# if there might be other tables with report AND other classes that you don't want:
# rows = soup.select('table[class="report"] tr[onmouseover]') 

rows = soup.select('table.report tr[onmouseover]')
```

this method is only unsuitable if there might be more than one `table` with `class= "report"`, but you only want rows from the first one; in that case, you might prefer the *`table.find_....if table else []`* approach.

---

#### Solution Part 2 Option A: Iterating Over `rows` to Print Cell Contents

Once you have `rows`, you can iterate over them to print the date and flag cell contents:

```python
for r in rows:
    date, flag = r.find('td', class_= "time"), r.find('td', class_= "flag")
    info = [i.get_text() if i else i for i in [date, flag]]
    if any([i is not None for i in info]): print(info) 
    # [ only prints if there are any non-null values ]
```

---

#### Solution Part 2 Option B: Iterating Over `rows` with a Fucntion

Btw, if you're going to be extracting multiple tag attributes/texts repeatedly, you might find my [`selectForList`](https://pastebin.com/ZnZ7xM6u) function useful - it could have been used like 

```python
for r in rows: 
    info = selectForList(r, ['td.time', 'td.flag'], printList=True)
    if any([i is not None for i in info]): print(info) 
```

or, to get a list of dictionaries like *`[{'time': time_1, 'flag': flag_1}, {'time': time_2, 'flag': flag_2}, ...]`*,

```python
infList = [selectForList(r, {
    'time': 'td.time', 'flag': 'td.flag', ## add selectors for any info you want 
}) for r in soup.select('table.report tr[onmouseover]')]
infList = [d for d in infoList if [v for v in d.values() if v is not None]]
```

----

#### Added EDIT:

To get all displayed cell contents:

```python
for r in rows: 
    info = [(td.get_text(),''.join(td.get('style','').split())) for td in r.select('td')]
    info = [txt.strip() for txt, styl in r.select('td') if 'display:none' not in styl]
    # info = [i if i else 0 for i in info] # fill blanks with zeroes intead of ''
    if any(info):  print(info) ## or write to CSV
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): The site has some proprietary data and requires login which is why I didn't want to include it. Should have included these though, apologies. ```python response = requests.get('https://vector.propreports.com/report.php', params=params, cookies=cookies, headers=headers)  soup = BeautifulSoup(response.content, 'html.parser') ``` Also forgot to mention that the website requires login. I used cookies for that but I suspect I will need to change it in order to automate as the site kicks you out after a while.
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): the ```python table = soup.find('table', class_= "report") rows = table.find_all('tr',  {'onmouseover': True}) if table else []``` works for the whole table but still get all the "<td class="time">05/11/22</td> <td class="flag">Eq</td>" etc.
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): I was unable to use selectForList as I am still very much clueless to many intricacies of additional modules etc. Your version, however, gave me a great output, pretty much exactly what I need but again only for the first two columns. [link]https://imgur.com/3LXa4Mr
- **me** (2023-01-07): @tracemuch did you iterate over rows [like this](https://i.sstatic.net/DPsQc.png) or as suggested in the last section? (Just in case it was unclear, I re-structured my answer sections - you need an option from part 1 followed by an option from part 2 for any full solution)
- **me** (2023-01-07): @tracemuch that's great! as for `selectForList`, although you could download into a file (let's say "selectForList.py") and then do something like `from selectForList import selectForList` (or`from selectForList import *` to use both fuctions inside), I usually just paste it into the code right after the imports (it may be easier to paste [from the raw](https://pastebin.com/raw/ZnZ7xM6u), although if you use PasteBin yourself you might see [the `copy` button](https://i.sstatic.net/ziszd.png))....it's not so important though, if you have v few details you want to extract like just flag+date
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): I spent all day updating the code and now I have a working automated login with credentials instead of cookies and integrated your code for the first two columns. If I just manage to scrape the rest of the table I will have all the data I need to work on. Any ideas how I can finish this? https://imgur.com/4EulRjq
- **me** (2023-01-07): @tracemuch (It might be better to post a separate question for that, with a html snippet [pasteable, not just a screenshot] containing at least 2 *relevant* `tr` tags, preferably as different as they can get from each other, and also maybe a sample of the desired output...) but based on the `tr` in your screenshot, I guess you could first try adding a line **`info += [td.get_text().strip() for td in r.select('td:not([class]):not([style])') if td.get_text().strip()]`** right before the *`if any(...): print(info)`* line and see if that leads to the results you want
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): Absolutely! One last thing I'm struggling with. There are blank spaces in some rows which cause the data to be structured weird when I try to write it to a file: https://imgur.com/v2vT2on How can I for example output "0" for every blank cell or alternatively restructure how the .csv is written. This is what I have so far: https://imgur.com/qqKH1ZV How the CSV looks: https://imgur.com/4Jfy8lk
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): Example of 6 blank cells before the next entry: https://imgur.com/0C67HlM
- **me** (2023-01-07): @tracemuch get rid of the ` if td.get_text().strip()` part (of  *`info += ...`*) if you don't want to skip blank cells, and add another line right after *`info += ...`*  with **`info = [i if i else 0 for i in info]`** to replace blanks
- **me** (2023-01-07): @tracemuch now that I've seen the blank cells that you might want, and that some of the the wanted cells can have `style` attribute, I think you should change the selector in *`info += ...`* to **`td:not([class]):not([style*="display:none"]):not([style*="display: none"])`**
- **me** (2023-01-07): @tracemuch or just change the whole line to `info += [td.get_text().strip() for td in r.select('td:not([class])') if 'display:none' not in td.get('style', '').replace(' ', '')]`
- **me** (2023-01-07): @tracemuch actually, you can just have `info = [td.get_text().strip() for td in r.select('td') if 'display:none' not in td.get('style', '').replace(' ', '')]` and skip the first two lines in the *`for r in rows:...`* block [I'm adding in an edit to the answer]
- **[tracemuch](https://stackoverflow.com/users/20949243)** (2023-01-07): @ Driftr95 The first solution worked perfectly! You are amazing, my friend! Thank you again!

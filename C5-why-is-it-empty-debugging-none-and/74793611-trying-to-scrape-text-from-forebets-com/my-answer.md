---
title: "Trying to scrape text from forebets.com"
site: stackoverflow
question_id: 74793611
answer_id: 74818698
url: https://stackoverflow.com/a/74818698
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-15T23:33:27Z
last_edited: 2022-12-15T23:38:48Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74818698/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca19e5df7647dd7f40a061dcc618b596b01e63b1c90cadc70627e67c35a6fddf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74818698>, 2022-12-15, last edited 2022-12-15; score 0. Text as retrieved 2026-10-12.

You're looping through hyperlinks with `tnmscn` class, but that [covers only teams and date info](https://i.sstatic.net/QuxBr.png); if you also want more data like location/weather/scores/odds/etc., you need to [cover the whole row](https://i.sstatic.net/qAsyr.png)

```python
# teams = soup.find_all('a', class_= 'tnmscn')
rows = soup.find_all('div', {'class': 'rcnt'})
# for team in teams:
for r in rows:
    hometeam = r.find('span',class_= 'homeTeam').text
    #### AND SO ON ####
```
<sub>(You can also loop with `for team in soup.find_all('div', {'class': 'rcnt'})` and continue using `team.find...` inside the loop - it won't make a difference in terms of results, but I thought `for r in rows...` makes better sense [in terms of readability] now that it's looping over whole rows [instead of just the home/away teams column].)</sub>

---

About getting the location with this line:

> ```python
>     location = team.find('name address', 'content').text
> ```

I get an [AttributeError](https://stackoverflow.com/q/8949252/6146136) on this line because **`.find('name address', 'content')`** returns `None` [and you can't get `.text` from `None`]. I'd be rather surprised if you don't also get such an error, because the main input to [`.find`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find) is expected to be a [tag name](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id12) and trying to find `name address` would never return anything as html tag names don't have spaces in them.

---

And about getting the predicted score with this line:

> ```python
>     predictedscore = team.select_one('div', class_='ex_sc tabonly')
> ```

`class_` is not an argument you can pass to [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)/`.select_one`, so it'll just be selecting the first `div` inside `team`. You can pass more elaborate [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) so it should have been like **`.select_one('div.ex_sc.tabonly')`**.

What *should* be used instead is **`.find('span', {'itemprop': 'location'}).meta['content']`** to get the `content` attribute of `meta` tags [such as this](https://i.sstatic.net/NIcfx.png).

Also, please not that this actually [gets you the **correct score**](https://i.sstatic.net/0i590.png) rather than the *predicted* score.

---

> to scrape the predicted score, correct score and weather

If you're looping over the whole row, then you can use
- **`.find('span', class_='forepr').text`** to get predicted score
- **`.find('div', class_='ex_sc tabonly').text`** to get correct score
- **`.find('div', class_="prwth tabonly")`** to get weather, but it may be missing, so you should
  - have *`if weather: weather = weather.text`* in another line to avoid getting AttributeError
  - [and add another line with *`else: continue`* if you want to skip such "rows"]

---
---

#### Suggested Solution:

Even though it's only really an issue for the weather data here, it's always safer to check where `.find...` or `.select...` returned anything before trying to get `.text`; and since you're doing this [`.find....text`] repeatedly, it's more convenient to just have it as a function.

I already [a function for this](https://pastebin.com/ZnZ7xM6u) that I often use when scraping with bs4, but it uses `.select_one` (not `.find`). All you need is a list of selectors and you can get all the data in one statement if you use [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp):

```python
# def selectForList.... # PASTE FROM https://pastebin.com/ZnZ7xM6u

rData = [selectForList(r, [
  'span.homeTeam', 'span.awayTeam', # home/away teams
  'span.forepr', 'div.ex_sc.tabonly', # pred/correct scores
  'span.date_bah', # date [location below]
  ('span[itemprop="location"]>meta[itemprop="name address"][content]', 'content'), 
  'div.prwth.tabonly>span.wnums', # temperature
]) for r in soup.select('div.rcnt')]
```

You could just print [by setting the print option](https://i.sstatic.net/BcSAM.png) of `selectForList` with `printList=' '`, or you could loop through `rData` to have more control over how it's printed.

```python
for r in rData: 
    print(f'# {r[0]} vs {r[1]}: {r[3] if r[3] else "score_unknown"}', 
          f'[pred: {r[2]}] on {r[4]} (at {r[5]})', 
          f'[{("temp: "+r[6]) if r[6] else "no_weather_data"}]')
    
### PRINTED OUTPUT BELOW ###

# Argentina vs France: 2 - 2 [pred: X] on 18/12/2022 16:00 (at Lusail Iconic Stadium) [temp: 21°]
# Croatia vs Morocco: 0 - 0 [pred: X] on 17/12/2022 16:00 (at Khalifa International Stadium) [temp: 22°]
# Argentina vs Croatia: 1 - 1 [pred: X] on 13/12/2022 20:00 (at Lusail Iconic Stadium) [temp: 22°]
# France vs Morocco: 3 - 1 [pred: 1] on 14/12/2022 20:00 (at Al Bayt Stadium) [temp: 22°]
# Juventus W vs Zurich (W): score_unknown [pred: 1] on 15/12/2022 18:45 (at Allianz Stadium) [no_weather_data]
# SL Benfica (W) vs Barcelona (W): score_unknown [pred: 2] on 15/12/2022 21:00 (at Caixa Futebol Campus) [no_weather_data]
```

--- 

For slightly more structured output, you could define [instead of a list] a reference dictionary (`selRef`) for the selectors and then get the data as list of dictionaries with the same keys as `selRef`:

```python
selRef = {'home_team': 'span.homeTeam', 'away_team': 'span.awayTeam', 'pred-y_n': ('div[class^="predict"]:has(>span.forepr)', 'class'), 'pred': 'span.forepr', 'correct_score': 'div.ex_sc.tabonly', 'date': 'span.date_bah', 'location': ('span[itemprop="location"]>meta[itemprop="name address"][content]', 'content'), 'temperature': 'div.prwth.tabonly>span.wnums', 'weather_icon': ('div.prwth.tabonly>img.wthc[src]', 'src')}

rdList = [dict(zip(
    selRef.keys(), selectForList(r, selRef.values()) #, printList=' ')
)) for r in soup.select('div.rcnt')]
```

then you could use [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) to covert it to DataFrame as simply as **`pandas.DataFrame(rdList)`**. [ [View DataFrame](https://i.sstatic.net/tkZE8.png) ]  

---

You might notice that in addition to splitting up the predictions, I've also added a `weather_icon` column. This column can be used to add in a descriptions of the weather

```python
wiRef = {'w-32': 'sunny', 'w-31': 'clear', 'w-30':'cloudy-day', 'w-29':'cloudy-night', 'w-20': 'fog', 'w-12': 'rainy-day', 'w-11': 'rainy-night'}

for ri, w in ([(i, r['weather_icon']) for i, r in enumerate(rdList) if r['weather_icon']]):
    rdList[ri]['weather_icon'] = f'https://www.forebet.com{w}' # replace with full link
    w = w.split('/')[-1].split('.png')[0].strip()
    rdList[ri]['weather'] = wiRef[w] if w in wiRef else f'{w}.png'

# import pandas
pandas.DataFrame(rdList).to_csv('wcPreds.csv', index=False)
```

The full list of weather icons as well the contents of the output 'wcPreds.csv' can be found in [this spreadsheet](https://docs.google.com/spreadsheets/d/1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo/edit?usp=sharing).

---

You can use **`print(pandas.DataFrame(rdList).drop(['weather_icon'], axis=1).rename({'temperature':'temp'}, axis=1).to_markdown(index=False))`** to print the markdown for table below: 

| home_team      | away_team     | pred-y_n   | pred   | correct_score   | date             | location                      | temp   | weather   |
|:---------------|:--------------|:-----------|:-------|:----------------|:-----------------|:------------------------------|:-------|:----------|
| Argentina      | France        | predict    | X      | 2 - 2           | 18/12/2022 16:00 | Lusail Iconic Stadium         | 21°    | clear     |
| Croatia        | Morocco       | predict    | X      | 0 - 0           | 17/12/2022 16:00 | Khalifa International Stadium | 22°    | clear     |
| Argentina      | Croatia       | predict_no | X      | 1 - 1           | 13/12/2022 20:00 | Lusail Iconic Stadium         | 22°    | clear     |
| France         | Morocco       | predict_y  | 1      | 3 - 1           | 14/12/2022 20:00 | Al Bayt Stadium               | 22°    | clear     |
| Juventus W     | Zurich (W)    | predict_y  | 1      |                 | 15/12/2022 18:45 | Allianz Stadium               |        | nan       |
| SL Benfica (W) | Barcelona (W) | predict_y  | 2      |                 | 15/12/2022 21:00 | Caixa Futebol Campus          |        | nan       |

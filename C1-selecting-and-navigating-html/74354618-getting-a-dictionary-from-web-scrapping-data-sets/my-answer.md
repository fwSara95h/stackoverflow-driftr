---
title: "Getting a dictionary from web-scrapping data sets"
site: stackoverflow
question_id: 74354618
answer_id: 74373728
url: https://stackoverflow.com/a/74373728
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-09T10:55:38Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74373728/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a77291680bcb4673bf361b108b8ecd90c13fa78a9cf204177fb92e9b812d383
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74373728>, 2022-11-09; score 0. Text as retrieved 2026-10-12.

> comparison_state is the string of state names, but if you print that it prints all of them, not just one; same thing with the sunlight

Is there one single cell with all the state names and another single cell with all the sunlight hours? Because otherwise that shouldn't be happening with the current code....(I'd really like to see the html you're working with - I can't be sure of anything below otherwise.)

<hr>

> but how do I put that into a dictionary or array of dictionaries

You could initiate the dictionary **before** the for-loop with `sunlightHrs_byState = {}` and then update the dictionary **inside** the loop by adding at the end: `sunlightHrs_byState[comparison_state] = sunlight`; but I think it would be much simpler if you replaced the loop entirely with [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) and a [selector](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) [`tr:has(td~td)`] that only targets rows [`tr` tags] with at least 2 cells [`td` tags]:
```python
table = soup.find('table')
sunlightHrs_byState = dict([(
    str(r.find('td').text.strip().lower()), # state name
    float(r.select_one('td ~ td').text.split()[0]) # sunlight
) for r in table.select('tr:has(td~td)')])
```
That should create a dictionary which has the state names (or whatever is in the first column) as keys paired up with the corresponding sunlight hours (or whatever is in the second column) as values - from every row in the table that has two (or more) columns.

<hr><hr>

I can't test on *your* html since you've not shared it, but the code below is tailored for [this table][1] on [FootprintHero](https://footprinthero.com/peak-sun-hours-calculator#peak-sun-hours-map), which looks similar how I think yours probably is:
```python
sunlightHrs_byState = dict([(
    r.find('td').get_text(strip=True), # state name
    (sum(
        float(a.strip()) for a in r.select_one('td ~ td').text.split('-')
    )/len(r.select_one('td ~ td').text.split('-'))) # averages sunlight hours
) for r in soup.select('table#tablepress-4 tr:has(td~td)')])
print(sunlightHrs_byState)
```
and that prints
```python
{'Alabama': 4.7, 'Alaska': 2.5, 'Arizona': 5.5, 'Arkansas': 4.550000000000001, 'California': 5.05, 'Colorado': 4.800000000000001, 'Connecticut': 4.0, 'Delaware': 4.199999999999999, 'Florida': 5.1, 'Georgia': 4.65, 'Hawaii': 5.05, 'Idaho': 4.1, 'Illinois': 4.15, 'Indiana': 4.1, 'Iowa': 4.1, 'Kansas': 4.699999999999999, 'Kentucky': 4.2, 'Louisiana': 4.85, 'Maine': 3.65, 'Maryland': 4.1, 'Massachusetts': 3.9, 'Michigan': 3.7, 'Minnesota': 3.75, 'Mississippi': 4.7, 'Missouri': 4.35, 'Montana': 3.9000000000000004, 'Nebraska': 4.4, 'Nevada': 5.199999999999999, 'New Hampshire': 3.65, 'New Jersey': 4.1, 'New Mexico': 5.5, 'New York': 3.8, 'North Carolina': 4.45, 'North Dakota': 3.9, 'Ohio': 3.9, 'Oklahoma': 4.9, 'Oregon': 4.05, 'Pennsylvania': 3.8499999999999996, 'Puerto Rico': 5.25, 'Rhode Island': 4.0, 'South Carolina': 4.7, 'South Dakota': 4.2, 'Tennessee': 4.3, 'Texas': 5.25, 'Utah': 4.95, 'Vermont': 3.5999999999999996, 'Virginia': 4.25, 'Washington': 3.6, 'Washington DC': 4.15, 'West Virginia': 4.0, 'Wisconsin': 3.8, 'Wyoming': 4.4}
```

<hr>

BTW, <sub>I'm not entirely sure what you're expecting `dict = {comparison_state : 1, sunlight : 2}` to do, but it's just going to create a dictionary named `dict` with two [values](https://www.programiz.com/python-programming/methods/dictionary/values) (`1` and `2`); and also, it's **NOT** a good idea to assign variable names that are already [reserved words](https://flexiple.com/python/python-reserved-words/) or [built-in data types](https://www.w3schools.com/python/python_datatypes.asp) (like `dict` is).</sub>

  [1]: https://i.sstatic.net/L9Jhl.png

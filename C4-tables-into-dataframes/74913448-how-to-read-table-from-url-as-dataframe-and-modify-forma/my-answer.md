---
title: "How to read table from url as DataFrame and modify format of data in one column in Python Pandas?"
site: stackoverflow
question_id: 74913448
answer_id: 74915155
url: https://stackoverflow.com/a/74915155
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-25T18:23:08Z
last_edited: 2022-12-25T18:31:09Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74915155/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 315f0ad5cc88b2797ee9b164390ac61f887ac34ef49d88547677393142badf96
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74915155>, 2022-12-25, last edited 2022-12-25; score 0. Text as retrieved 2026-10-12.

> read this table as DataFrame 

You can probably just use [`pandas.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) directly.

```python
# import pandas
khdf = pandas.read_html('https://www.timeanddate.com/holidays/kenya/2022')[0]
```

and to clean up a bit by resetting the column headers and getting rid of empty rows:

```python
khdf = khdf.set_axis(
    ['Date', 'Day', 'Name', 'Type'], axis='columns'
).dropna(axis='rows', how='all')
```

---

> Convert column "Date" so as to have date format like "01.01.2022"

You can parse the date with [`dateutil.parser`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse) and then format it with [`.strftime`](https://www.programiz.com/python-programming/datetime/strftime).

```python
# from dateutil.parser import parse as duParse
y = 2022
khdf['Date'] = [duParse(f'{y} {d}').strftime('%d.%m.%Y') for d in khdf['Date']]
```

---

> how to create column "Day" where will be value like: sobota, niedziela and so on

As it is so far, we already have a `Day` column with Monday/Tuesday/etc., but if you want them in Polish, you could use a translation dictionary [like `daysDict` below].

```python
daysDict = {'Monday': 'Poniedziałek', 'Tuesday': 'Wtorek', 'Wednesday': 'Środa', 'Thursday': 'Czwartek', 'Friday': 'Piątek', 'Saturday': 'Sobota', 'Sunday': 'Niedziela'}
khdf['Day'] = [daysDict[d] if d in daysDict else d for d in khdf['Day']]
```

<br>

If you want to translate *everything* [except for `Date`], you could use the [`googletrans`](https://pypi.org/project/googletrans/) module. (I think the version installed by default has some issues, but `3.1.0a0` works for me.)

```python
# !pip install googletrans==3.1.0a0
# from googletrans import Translator
translator = Translator()
for c in ['Day', 'Name', 'Type']:
    khdf[c] = [translator.translate(d, src='en', dest='pl').text for d in khdf[c]]
```

---
---

> [because you commented about] *"sample of code with loop"*

Since the page links have a consistent format, you can loop through various countries and years.

First, import the necessary libraries and define the translation dictionary along with a function that *tries* to parse and format the date (but returns a null value (`None`) if it fails):

```python
import pandas
from dateutil.parser import parse as duParse

daysDict = {'Monday': 'Poniedziałek', 'Tuesday': 'Wtorek', 'Wednesday': 'Środa', 'Thursday': 'Czwartek', 'Friday': 'Piątek', 'Saturday': 'Sobota', 'Sunday': 'Niedziela'}

def try_dup(dStr, yr):
    try: return duParse(f'{yr} {dStr}').strftime('%d.%m.%Y') 
    except: return None
```

then, set the start and end years as well as a list of countries:

```python
startYear, endYear = 2010, 2030
countryList = ['kenya', 'tonga', 'belgium']
```

now, we're ready to loop though the countries and years to collect data:

```python
dfList = []
for country in countryList:
    for y in range(startYear, endYear+1):
        try: 
            cyUrl = f'https://www.timeanddate.com/holidays/{country}/{y}'
            cydf = pandas.read_html(cyUrl)[0]

            cydf = cydf.drop(# only the first 4 columns are kept
                [c for c in cydf.columns[4:]], axis='columns'
            ).set_axis(['Date', 'Day', 'Name', 'Type'], axis='columns')
            cydf['Date'] = [try_dup(d, y) for d in cydf['Date']] # parse+format date
            cydf['Country'] = country.capitalize() # add+fill a column with country name

            dfList.append(cydf.dropna(axis='rows', subset=['Date'])) # only add rows with Date
            # print('', end=f'\r{len(dfList[-1])} holidays scraped from {cyUrl}')
        # except: continue ## skip without printing error
        except Exception as e: 
            print('\n', type(e), e, '- failed to scrape from', cyUrl)
# print('\n\n', len(dfList), 'dataframes with', sum([len(d) for d in dfList]),'holidays scraped overall')
```

After looping, all the DataFrames can be combined into one before translating the days:

```python
acydf = pandas.concat(dfList, ignore_index=True)
acydf['Day'] = [daysDict[d] if d in daysDict else d for d in acydf['Day']] # translate days
acydf = acydf[['Country', 'Date', 'Day', 'Name', 'Type']] # rearrange columns
```

A sample of `acydf` [printed with `print(acydf.loc[::66].to_markdown(index=False))`]:

```lang-none
| Country   | Date       | Day          | Name                                          | Type                        |
|:----------|:-----------|:-------------|:----------------------------------------------|:----------------------------|
| Kenya     | 01.01.2012 | Niedziela    | New Year's Day                                | Public holiday              |
| Kenya     | 19.07.2015 | Niedziela    | Eid al-Fitr                                   | Public holiday              |
| Kenya     | 10.10.2018 | Środa        | Moi Day                                       | Public holiday              |
| Kenya     | 10.10.2021 | Niedziela    | Huduma Day                                    | Public holiday              |
| Kenya     | 26.12.2023 | Wtorek       | Boxing Day                                    | Public holiday              |
| Kenya     | 01.01.2027 | Piątek       | New Year's Day                                | Public holiday              |
| Kenya     | 14.04.2030 | Niedziela    | Eid al-Adha (Tentative Date)                  | Optional Holiday            |
| Tonga     | 17.09.2012 | Poniedziałek | Birthday of Crown Prince Tupouto'a-'Ulukalala | Public Holiday              |
| Tonga     | 25.04.2016 | Poniedziałek | ANZAC Day                                     | Public Holiday              |
| Tonga     | 04.12.2019 | Środa        | Anniversary of the Coronation of King Tupou I | Public Holiday              |
| Tonga     | 04.06.2023 | Niedziela    | Emancipation Day                              | Public Holiday              |
| Tonga     | 01.01.2027 | Piątek       | New Year's Day                                | Public Holiday              |
| Tonga     | 04.11.2030 | Poniedziałek | Constitution Day                              | Public Holiday              |
| Belgium   | 06.12.2011 | Wtorek       | St. Nicholas Day                              | Observance                  |
| Belgium   | 06.12.2013 | Piątek       | St. Nicholas Day                              | Observance                  |
| Belgium   | 06.12.2015 | Niedziela    | St. Nicholas Day                              | Observance                  |
| Belgium   | 15.11.2017 | Środa        | Day of the German-speaking Community          | Regional government holiday |
| Belgium   | 01.11.2019 | Piątek       | All Saints' Day                               | National holiday            |
| Belgium   | 31.10.2021 | Niedziela    | Halloween                                     | Observance                  |
| Belgium   | 23.09.2023 | Sobota       | September Equinox                             | Season                      |
| Belgium   | 15.08.2025 | Piątek       | Assumption of Mary                            | National holiday            |
| Belgium   | 11.07.2027 | Niedziela    | Day of the Flemish Community                  | Regional government holiday |
| Belgium   | 10.06.2029 | Niedziela    | Father's Day                                  | Observance                  |
```

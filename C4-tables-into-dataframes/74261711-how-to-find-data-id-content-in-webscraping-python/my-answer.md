---
title: "How to find data-id content in webscraping (python)"
site: stackoverflow
question_id: 74261711
answer_id: 74270546
url: https://stackoverflow.com/a/74270546
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T01:14:46Z
last_edited: 2022-11-01T01:36:56Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74270546/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c22ed40c72d0fe8231ef18410c95c47005113e88df73632996847036bf168722
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74270546>, 2022-11-01, last edited 2022-11-01; score 0. Text as retrieved 2026-10-12.

`.find_all('tr', attrs=('data-id'))` is not the correct way to use `find`; if you want rows that have a `data-id` attribute, you can use `select` with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php), and if you want *value* of the `data-id` attribute, you can use `.get`:
```python
for row in WholeDoc.select('div[data-type="Photobook"] tbody tr[data-id]'): 
    print(row.get('data-id'))
```
(`select` is really good for targeting nested elements, so you don't even have to more than one for-loop here!)

<hr>

Since you're using pandas, you can use 
```python
dataType_tables = [{
    'type': t.get('data-type') + ' -> ' + t.get('data-subtype', 'NO_SUBTYPE'), 
    'headers': ['Data-ID'] + [
        col.get_text(strip=True) for col in t.select('th')], 
    'data': [[r.get('data-id')] + [
        col.get_text(strip=True) for col in r.select('td')
    ] for r in t.select('tr:has(td)')]
} for t in doc.select('div[data-type]')]
```
to get a list of dictionaries representing all the tables on the page, and the view them with
[![sample op][1]][1]

<hr><hr>

You can print *all* the tables under any `data-type` with
```python
for t in doc.select('div[data-type]'): 
    titleLine = t.get('data-type').upper()
    if t.get('data-subtype'): 
        titleLine += ' --> ' + t.get('data-subtype').upper()
    print(titleLine)

    divider = ('| ' + ' | '.join([
        '+'*40 if i == 1 else ('+'*20 if i == 0 else '+'*15) 
        for i in range(len(t.select('th'))+1)
    ]) + ' |')
    print(divider)
    print('|', ' | '.join([
        f'{c[:40]:^40}' if i == 1 else 
        (f'{c[:20]:^20}' if i == 0 else f'{c[:15]:^15}') 
        for i, c in enumerate(
            ['Data-ID'] + [col.text.strip() for col in t.select('th')]
    )]), '|')
    print(divider)
    for r in t.select('tr:has(td)'):
        print('|', ' | '.join([
            f'{c:^40}' if i == 1 else (f'{c:^20}' if i == 0 else f'{c:^15}') 
            for i, c in enumerate(
                [r.get('data-id', '')] + 
                [col.text.strip() for col in r.select('td')]
        )]), '|')
    print(divider, '\n')
```
Output:
```lang-none
PHOTOBOOK --> LANDSCAPE
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |             Fotoboek Liggend             |      Prijs      | Per extra pagin | Linnen kaft met |  Foto op kaft   |   Leren kaft    | Platliggend pre | Hoogglans meerp |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_354        |    Liggend S (Harde kaft  13 x 10 cm)    |     € 10,99     |     € 0,39      |        -        |     € 2,50      |     € 3,95      |        -        |     € 0,03      |
|       PAP_109        |   Liggend M (Zachte kaft  20 x 15 cm)    |     € 16,49     |     € 0,55      |        -        |        -        |        -        |        -        |     € 0,03      |
|       PAP_130        |    Liggend M (Harde kaft  20 x 15 cm)    |     € 18,99     |     € 0,51      |        -        |     € 1,00      |     € 5,00      |        -        |     € 0,03      |
|       PAP_350        |   Liggend L (Zachte kaft  28 x 21 cm)    |     € 21,99     |     € 0,71      |        -        |        -        |        -        |        -        |     € 0,04      |
|       PAP_347        |    Liggend L (Harde kaft  28 x 21 cm)    |     € 26,99     |     € 0,67      |        -        |     € 5,50      |     € 9,45      |     € 0,39      |     € 0,21      |
|       PAP_355        |   Liggend XL (Harde kaft  39 x 29 cm)    |     € 48,49     |     € 1,31      |        -        |     € 12,00     |     € 10,00     |     € 0,63      |     € 0,21      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

PHOTOBOOK --> SQUARE
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |           Fotoboeken Vierkant            |      Prijs      | Per extra pagin | Linnen kaft met |  Foto op kaft   |   Leren kaft    | Platliggend pre | Hoogglans meerp |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_203        |   Vierkant S (Zachte kaft  10 x 10 cm)   |     € 6,99      |     € 0,43      |        -        |        -        |        -        |        -        |     € 0,03      |
|       PAP_205        |   Vierkant M (Zachte kaft  14 x 14 cm)   |     € 12,49     |     € 0,47      |        -        |        -        |        -        |        -        |     € 0,03      |
|       PAP_360        |   Vierkant M (Harde kaft  14 x 14 cm)    |     € 15,99     |     € 0,57      |        -        |     € 1,50      |     € 5,00      |        -        |     € 0,03      |
|       PAP_204        |   Vierkant L (Zachte kaft  21 x 21 cm)   |     € 20,49     |     € 0,71      |        -        |        -        |        -        |        -        |     € 0,03      |
|       PAP_324        |   Vierkant L (Harde kaft  21 x 21 cm)    |     € 25,49     |     € 0,63      |        -        |     € 5,00      |     € 7,95      |     € 0,39      |     € 0,03      |
|       PAP_194        |   Vierkant XL (Harde kaft  30 x 30 cm)   |     € 45,99     |     € 0,95      |        -        |     € 2,50      |     € 10,00     |     € 0,45      |     € 0,21      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

PHOTOBOOK --> PORTRAIT
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |             Fotoboek Staand              |      Prijs      | Per extra pagin | Linnen kaft met |  Foto op kaft   |   Leren kaft    | Platliggend pre | Hoogglans meerp |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_201        |    Staand M (Harde kaft  15 x 20 cm)     |     € 18,99     |     € 0,51      |        -        |     € 1,00      |     € 5,00      |        -        |     € 0,03      |
|       PAP_349        |    Staand L (Zachte kaft  21 x 28 cm)    |     € 21,99     |     € 0,71      |        -        |        -        |        -        |        -        |     € 0,04      |
|       PAP_348        |    Staand L (Harde kaft  21 x 28 cm)     |     € 26,99     |     € 0,67      |        -        |     € 5,50      |     € 9,45      |     € 0,39      |     € 0,21      |
|       PAP_202        |    Staand XL (Harde kaft  27 x 36 cm)    |     € 48,49     |     € 1,31      |        -        |     € 12,00     |     € 10,00     |        -        |     € 0,21      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

WALLART --> ALUMINIUM
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |            Foto op aluminium             |      Prijs      |   Oriëntatie    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_510        |     Foto op aluminium ( 30 x 20 cm)      |     € 26,99     |     Liggend     |
|       PAP_511        |     Foto op aluminium ( 40 x 30 cm)      |     € 43,49     |     Liggend     |
|       PAP_512        |     Foto op aluminium ( 60 x 40 cm)      |     € 57,99     |     Liggend     |
|       PAP_513        |     Foto op aluminium ( 70 x 50 cm)      |     € 91,99     |     Liggend     |
|       PAP_514        |     Foto op aluminium ( 80 x 60 cm)      |    € 144,99     |     Liggend     |
|       PAP_515        |     Foto op aluminium ( 100 x 70 cm)     |    € 159,99     |     Liggend     |
|       PAP_516        |     Foto op aluminium ( 120 x 80 cm)     |    € 219,99     |     Liggend     |
|       PAP_517        |     Foto op aluminium ( 20 x 30 cm)      |     € 26,99     |     Staand      |
|       PAP_518        |     Foto op aluminium ( 30 x 40 cm)      |     € 43,49     |     Staand      |
|       PAP_519        |     Foto op aluminium ( 40 x 60 cm)      |     € 57,99     |     Staand      |
|       PAP_520        |     Foto op aluminium ( 50 x 70 cm)      |     € 91,99     |     Staand      |
|       PAP_521        |     Foto op aluminium ( 60 x 80 cm)      |    € 144,99     |     Staand      |
|       PAP_522        |     Foto op aluminium ( 70 x 100 cm)     |    € 159,99     |     Staand      |
|       PAP_523        |     Foto op aluminium ( 80 x 120 cm)     |    € 219,99     |     Staand      |
|       PAP_531        |     Foto op aluminium ( 20 x 20 cm)      |     € 23,99     |    Vierkant     |
|       PAP_524        |     Foto op aluminium ( 30 x 30 cm)      |     € 39,49     |    Vierkant     |
|       PAP_525        |     Foto op aluminium ( 40 x 40 cm)      |     € 47,49     |    Vierkant     |
|       PAP_526        |     Foto op aluminium ( 50 x 50 cm)      |     € 79,99     |    Vierkant     |
|       PAP_527        |     Foto op aluminium ( 60 x 60 cm)      |     € 94,99     |    Vierkant     |
|       PAP_528        |     Foto op aluminium ( 70 x 70 cm)      |    € 114,99     |    Vierkant     |
|       PAP_529        |     Foto op aluminium ( 80 x 80 cm)      |    € 159,99     |    Vierkant     |
|       PAP_530        |    Foto op aluminium ( 100 x 100 cm)     |    € 209,99     |    Vierkant     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

WALLART --> CANVAS
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |              Foto op canvas              |      Prijs      | Zwevende lijst  |   Oriëntatie    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_418        |       Foto op canvas ( 30 x 20 cm)       |     € 20,49     |     € 15,99     |     Liggend     |
|       PAP_403        |       Foto op canvas ( 40 x 30 cm)       |     € 25,49     |     € 20,49     |     Liggend     |
|       PAP_404        |       Foto op canvas ( 60 x 40 cm)       |     € 38,49     |     € 24,49     |     Liggend     |
|       PAP_405        |       Foto op canvas ( 70 x 50 cm)       |     € 40,49     |     € 27,99     |     Liggend     |
|       PAP_427        |       Foto op canvas ( 80 x 60 cm)       |     € 57,49     |     € 30,49     |     Liggend     |
|       PAP_408        |      Foto op canvas ( 100 x 70 cm)       |     € 74,99     |     € 37,99     |     Liggend     |
|       PAP_409        |      Foto op canvas ( 120 x 80 cm)       |    € 119,99     |     € 39,99     |     Liggend     |
|       PAP_420        |       Foto op canvas ( 20 x 30 cm)       |     € 20,49     |     € 15,49     |     Staand      |
|       PAP_421        |       Foto op canvas ( 30 x 40 cm)       |     € 25,49     |     € 20,99     |     Staand      |
|       PAP_422        |       Foto op canvas ( 40 x 60 cm)       |     € 38,49     |     € 23,99     |     Staand      |
|       PAP_423        |       Foto op canvas ( 50 x 70 cm)       |     € 40,49     |     € 26,99     |     Staand      |
|       PAP_426        |       Foto op canvas ( 60 x 80 cm)       |     € 57,49     |     € 29,99     |     Staand      |
|       PAP_424        |      Foto op canvas ( 70 x 100 cm)       |     € 74,99     |     € 36,99     |     Staand      |
|       PAP_425        |      Foto op canvas ( 80 x 120 cm)       |    € 119,99     |     € 41,99     |     Staand      |
|       PAP_428        |       Foto op canvas ( 20 x 20 cm)       |     € 6,49      |     € 14,99     |    Vierkant     |
|       PAP_410        |       Foto op canvas ( 30 x 30 cm)       |     € 21,99     |     € 17,49     |    Vierkant     |
|       PAP_411        |       Foto op canvas ( 40 x 40 cm)       |     € 31,99     |     € 22,99     |    Vierkant     |
|       PAP_412        |       Foto op canvas ( 50 x 50 cm)       |     € 38,49     |     € 24,99     |    Vierkant     |
|       PAP_413        |       Foto op canvas ( 60 x 60 cm)       |     € 50,99     |     € 26,99     |    Vierkant     |
|       PAP_414        |       Foto op canvas ( 70 x 70 cm)       |     € 57,49     |     € 29,99     |    Vierkant     |
|       PAP_415        |       Foto op canvas ( 80 x 80 cm)       |     € 60,49     |     € 35,99     |    Vierkant     |
|       PAP_417        |      Foto op canvas ( 100 x 100 cm)      |     € 92,99     |     € 39,99     |    Vierkant     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

WALLART --> FOREX
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |              Foto op forex               |      Prijs      |   Oriëntatie    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_540        |       Foto op forex ( 30 x 20 cm)        |     € 23,99     |     Liggend     |
|       PAP_541        |       Foto op forex ( 40 x 30 cm)        |     € 33,49     |     Liggend     |
|       PAP_542        |       Foto op forex ( 60 x 40 cm)        |     € 39,99     |     Liggend     |
|       PAP_543        |       Foto op forex ( 70 x 50 cm)        |     € 70,99     |     Liggend     |
|       PAP_544        |       Foto op forex ( 80 x 60 cm)        |     € 99,99     |     Liggend     |
|       PAP_545        |       Foto op forex ( 100 x 70 cm)       |    € 109,99     |     Liggend     |
|       PAP_546        |       Foto op forex ( 120 x 80 cm)       |    € 159,99     |     Liggend     |
|       PAP_547        |       Foto op forex ( 20 x 30 cm)        |     € 23,99     |     Staand      |
|       PAP_548        |       Foto op forex ( 30 x 40 cm)        |     € 33,49     |     Staand      |
|       PAP_549        |       Foto op forex ( 40 x 60 cm)        |     € 39,99     |     Staand      |
|       PAP_562        |       Foto op forex ( 50 x 70 cm)        |     € 70,99     |     Staand      |
|       PAP_563        |       Foto op forex ( 60 x 80 cm)        |     € 99,99     |     Staand      |
|       PAP_552        |       Foto op forex ( 70 x 100 cm)       |    € 109,99     |     Staand      |
|       PAP_553        |       Foto op forex ( 80 x 120 cm)       |    € 159,99     |     Staand      |
|       PAP_561        |       Foto op forex ( 20 x 20 cm)        |     € 16,99     |    Vierkant     |
|       PAP_554        |       Foto op forex ( 30 x 30 cm)        |     € 26,99     |    Vierkant     |
|       PAP_555        |       Foto op forex ( 40 x 40 cm)        |     € 34,99     |    Vierkant     |
|       PAP_556        |       Foto op forex ( 50 x 50 cm)        |     € 51,99     |    Vierkant     |
|       PAP_557        |       Foto op forex ( 60 x 60 cm)        |     € 55,49     |    Vierkant     |
|       PAP_558        |       Foto op forex ( 70 x 70 cm)        |     € 92,99     |    Vierkant     |
|       PAP_559        |       Foto op forex ( 80 x 80 cm)        |    € 114,99     |    Vierkant     |
|       PAP_560        |      Foto op forex ( 100 x 100 cm)       |    € 149,99     |    Vierkant     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

WALLART --> PLEXIGLAS
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |            Foto op plexiglas             |      Prijs      |   Oriëntatie    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_454        |     Foto op plexiglas ( 30 x 20 cm)      |     € 35,49     |     Liggend     |
|       PAP_450        |     Foto op plexiglas ( 40 x 30 cm)      |     € 46,99     |     Liggend     |
|       PAP_451        |     Foto op plexiglas ( 60 x 40 cm)      |     € 91,99     |     Liggend     |
|       PAP_452        |     Foto op plexiglas ( 70 x 50 cm)      |    € 114,99     |     Liggend     |
|       PAP_456        |     Foto op plexiglas ( 80 x 60 cm)      |    € 169,99     |     Liggend     |
|       PAP_453        |     Foto op plexiglas ( 100 x 70 cm)     |    € 229,99     |     Liggend     |
|       PAP_455        |     Foto op plexiglas ( 120 x 80 cm)     |    € 289,99     |     Liggend     |
|       PAP_470        |     Foto op plexiglas ( 20 x 30 cm)      |     € 35,49     |     Staand      |
|       PAP_471        |     Foto op plexiglas ( 30 x 40 cm)      |     € 46,99     |     Staand      |
|       PAP_472        |     Foto op plexiglas ( 40 x 60 cm)      |     € 91,99     |     Staand      |
|       PAP_473        |     Foto op plexiglas ( 50 x 70 cm)      |    € 114,99     |     Staand      |
|       PAP_476        |     Foto op plexiglas ( 60 x 80 cm)      |    € 169,99     |     Staand      |
|       PAP_474        |     Foto op plexiglas ( 70 x 100 cm)     |    € 229,99     |     Staand      |
|       PAP_475        |     Foto op plexiglas ( 80 x 120 cm)     |    € 289,99     |     Staand      |
|       PAP_487        |     Foto op plexiglas ( 20 x 20 cm)      |     € 32,49     |    Vierkant     |
|       PAP_480        |     Foto op plexiglas ( 30 x 30 cm)      |     € 35,49     |    Vierkant     |
|       PAP_481        |     Foto op plexiglas ( 40 x 40 cm)      |     € 59,99     |    Vierkant     |
|       PAP_482        |     Foto op plexiglas ( 50 x 50 cm)      |     € 99,99     |    Vierkant     |
|       PAP_483        |     Foto op plexiglas ( 60 x 60 cm)      |    € 149,99     |    Vierkant     |
|       PAP_484        |     Foto op plexiglas ( 70 x 70 cm)      |    € 179,99     |    Vierkant     |
|       PAP_485        |     Foto op plexiglas ( 80 x 80 cm)      |    € 219,99     |    Vierkant     |
|       PAP_486        |    Foto op plexiglas ( 100 x 100 cm)     |    € 239,99     |    Vierkant     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

WALLART --> POSTER
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |                 Posters                  |      Prijs      |   Oriëntatie    |   Mat papier*   |    Glanzend*    |   Extra mat*    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_610        |           Poster ( 30 x 20 cm)           |     € 4,99      |     Liggend     |        -        |     € 0,49      |     € 0,49      |
|       PAP_611        |           Poster ( 40 x 30 cm)           |     € 7,49      |     Liggend     |        -        |     € 0,99      |     € 0,99      |
|       PAP_612        |           Poster ( 60 x 40 cm)           |     € 11,99     |     Liggend     |        -        |     € 1,49      |     € 1,49      |
|       PAP_613        |           Poster ( 70 x 50 cm)           |     € 14,49     |     Liggend     |        -        |     € 1,99      |     € 1,99      |
|       PAP_614        |           Poster ( 80 x 60 cm)           |     € 19,99     |     Liggend     |        -        |     € 2,49      |     € 2,49      |
|       PAP_615        |          Poster ( 100 x 70 cm)           |     € 23,49     |     Liggend     |        -        |     € 3,49      |     € 3,49      |
|       PAP_616        |          Poster ( 120 x 80 cm)           |     € 28,99     |     Liggend     |        -        |     € 3,99      |     € 3,99      |
|       PAP_617        |           Poster ( 20 x 30 cm)           |     € 4,99      |     Staand      |        -        |     € 0,49      |     € 0,49      |
|       PAP_618        |           Poster ( 30 x 40 cm)           |     € 7,49      |     Staand      |        -        |     € 0,99      |     € 0,99      |
|       PAP_619        |           Poster ( 40 x 60 cm)           |     € 11,99     |     Staand      |        -        |     € 1,49      |     € 1,49      |
|       PAP_620        |           Poster ( 50 x 70 cm)           |     € 14,49     |     Staand      |        -        |     € 1,99      |     € 1,99      |
|       PAP_621        |           Poster ( 60 x 80 cm)           |     € 19,99     |     Staand      |        -        |     € 2,49      |     € 2,49      |
|       PAP_622        |          Poster ( 70 x 100 cm)           |     € 23,49     |     Staand      |        -        |     € 3,49      |     € 3,49      |
|       PAP_623        |          Poster ( 80 x 120 cm)           |     € 28,99     |     Staand      |        -        |     € 3,99      |     € 3,99      |
|       PAP_624        |           Poster ( 20 x 20 cm)           |     € 3,11      |    Vierkant     |        -        |     € 0,49      |     € 0,49      |
|       PAP_625        |           Poster ( 30 x 30 cm)           |     € 6,99      |    Vierkant     |        -        |     € 0,99      |     € 0,99      |
|       PAP_626        |           Poster ( 40 x 40 cm)           |     € 8,99      |    Vierkant     |        -        |     € 0,99      |     € 0,99      |
|       PAP_627        |           Poster ( 50 x 50 cm)           |     € 12,49     |    Vierkant     |        -        |     € 1,49      |     € 1,49      |
|       PAP_628        |           Poster ( 60 x 60 cm)           |     € 15,99     |    Vierkant     |        -        |     € 1,99      |     € 1,99      |
|       PAP_629        |           Poster ( 70 x 70 cm)           |     € 16,99     |    Vierkant     |        -        |     € 2,99      |     € 2,99      |
|       PAP_630        |           Poster ( 80 x 80 cm)           |     € 22,99     |    Vierkant     |        -        |     € 3,49      |     € 3,49      |
|       PAP_631        |          Poster ( 100 x 100 cm)          |     € 36,49     |    Vierkant     |        -        |     € 4,49      |     € 4,49      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

CALENDAR --> CALENDAR
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |              Fotokalenders               |      Prijs      |   Mat papier    |    Glanzend     |    Extra mat    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_653        |          Fotokalender A4 Dubbel          |     € 22,49     |    Standaard    |     € 25,09     |     € 24,44     |
|       PAP_658        |                 Vierkant                 |     € 9,49      |    Standaard    |     € 11,44     |     € 10,79     |
|       PAP_659        |             Fotokalender A4              |     € 16,49     |    Standaard    |     € 19,09     |     € 18,44     |
|       PAP_660        |             Fotokalender A3              |     € 26,49     |    Standaard    |     € 29,74     |     € 29,09     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

PRINTS --> PRINTS
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |             Foto’s afdrukken             |      Prijs      | Exacte afmeting |    Glanzend*    |   Witte rand*   |   Mat papier*   |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|  PAP_910_102x102 cm  |         Premium afdrukken 10 cm          |     € 0,12      |  10.2x10.2 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_910_102x136 cm  |         Premium afdrukken 10 cm          |     € 0,18      |  10.2x13.6 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_910_102x153 cm  |         Premium afdrukken 10 cm          |     € 0,20      |  10.2x15.3 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_911_127x127 cm  |         Premium afdrukken 13 cm          |     € 0,20      |  12.7x12.7 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_911_127x169 cm  |         Premium afdrukken 13 cm          |     € 0,21      |  12.7x16.9 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_911_127x180 cm  |         Premium afdrukken 13 cm          |     € 0,24      |  12.7x18.0 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_910_102x120 cm  |               Retro foto's               |     € 0,42      |  10.2x12.0 cm   |        -        |     € 0,02      |     € 0,02      |
|  PAP_911_127x190 cm  |              Foto vergroten              |     € 0,30      |  12.7x19.0 cm   |        -        |     € 0,02      |     € 0,02      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

CARD --> UNFOLDED
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |            Enkele fotokaarten            |     Prijs*      |   Mat papier*   |    Glanzend*    |   Extra mat*    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_940        |                10 x 10 cm                |     € 5,49      |        -        |     € 0,25      |     € 0,15      |
|       PAP_941        |                15 x 15 cm                |     € 11,49     |        -        |     € 1,00      |     € 0,80      |
|       PAP_942        |                10 x 15 cm                |     € 7,99      |        -        |     € 0,90      |     € 0,75      |
|       PAP_943        |                15 x 10 cm                |     € 7,99      |        -        |     € 0,90      |     € 0,75      |
|       PAP_944        |                13 x 19 cm                |     € 12,99     |        -        |     € 1,25      |     € 1,00      |
|       PAP_945        |                19 x 13 cm                |     € 12,99     |        -        |     € 1,25      |     € 1,00      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

CARD --> FOLDED
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       Data-ID        |           Dubbele fotokaarten            |     Prijs*      |   Mat papier*   |    Glanzend*    |   Extra mat*    |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
|       PAP_950        |                10 x 10 cm                |     € 10,99     |        -        |     € 1,00      |     € 0,80      |
|       PAP_951        |                15 x 15 cm                |     € 16,49     |        -        |     € 1,50      |     € 1,25      |
|       PAP_952        |                10 x 15 cm                |     € 12,99     |        -        |     € 1,25      |     € 1,00      |
|       PAP_953        |                15 x 10 cm                |     € 12,99     |        -        |     € 1,25      |     € 1,00      |
|       PAP_954        |                13 x 19 cm                |     € 17,49     |        -        |     € 1,50      |     € 1,25      |
|       PAP_955        |                19 x 13 cm                |     € 17,49     |        -        |     € 1,50      |     € 1,25      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | 

MUG --> MUG
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ |
|       Data-ID        |              Mok bedrukken               |      Prijs      |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ |
|       PAP_720        |                  Mokken                  |     € 9,99      |
|       PAP_721        |         Mokken met panoramafoto          |     € 11,99     |
| ++++++++++++++++++++ | ++++++++++++++++++++++++++++++++++++++++ | +++++++++++++++ | 

```


  [1]: https://i.sstatic.net/pmo6U.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Lautjelief](https://stackoverflow.com/users/20340060)** (2022-11-01): This is perfect! However, I need to export it to an excel sheet (hence the reason for pandas). How can I do that? Ive tried making a DataFrame but it comes back almost empty and not useable :(
- **me** (2022-11-01): @Lautjelief I've added as [another answer](https://stackoverflow.com/a/74279923/12652373). Perhaps that will be more helpful

---
title: "Extract content from a page that renders it with javascript using Beautifulsoup"
site: stackoverflow
question_id: 74497235
answer_id: 74498329
url: https://stackoverflow.com/a/74498329
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-19T07:47:13Z
last_edited: 2022-11-19T08:21:25Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74498329/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 77a0530ed2c8a22a89579c5cff58acc66b40a1d05df3721a16fc344dec8577c6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74498329>, 2022-11-19, last edited 2022-11-19; **accepted**; score 0. Text as retrieved 2026-10-12.

This section not only requires js to load, it actually will not load until you scroll to it. You could try to figure out which request and/or bit of js was made to render that section and then attempt to replicate it with python, but I think it would be easier to use [selenium](https://www.scrapingbee.com/blog/selenium-python/). I even [have this function](https://pastebin.com/kEC9gPC8) for making it more convenient to automate some of the simpler/common interactions before scraping the html:
```python
#### FIRST PASTE [or DOWNLOAD&IMPORT] FUNCTION DEF from https://pastebin.com/kEC9gPC8 ####
soup = linkToSoup_selenium(
    'https://statusinvest.com.br/acoes/petr4', 
    clickFirst='//strong[@data-item="avg_F"]' # it actually just has to scroll, not click [but I haven't added an option for that yet], 
    ecx='//strong[@data-item="avg_F"][text()!="-"]' # waits till this loads
)
if soup is not None:
    print({
        t.find_previous_sibling().get_text(' ').strip(): t.get_text(' ').strip()
        for t in soup.select('div#payout-section span.title + strong.value')
    })
```
prints
```python
{'MÉDIA': '83,32%', 'ATUAL': '124,13% \n ( 48,97% acima da média )', 'MENOR\xa0VALOR': '26,35% \n ( 2019 )', 'MAIOR\xa0VALOR': '144,51% \n \n( 2020 )'}
```

---

**EDIT:** I ended up noticing the API used for fetching the data after all ([https://statusinvest.com.br/acao/payoutresult?code=petr4&companyid=408&type=0](https://statusinvest.com.br/acao/payoutresult?code=petr4&companyid=408&type=0)). You can actually reform it even with html available before the js-loading happens:
```python 
soup.select_one('#payout-section[data-company][data-code]').attrs
```
should return
```python
{'id': 'payout-section', 'data-company': '408', 'data-code': 'petr4', 'data-category': '1'}
```
so then the url can be formed with
```python
payout = soup.select_one('#payout-section[data-company][data-code]')
if payout:
    compId, dCode = payout.get('data-company'), payout.get('data-code')
    apiUrl = f'https://statusinvest.com.br/acao'
    apiUrl = f'{apiUrl}/payoutresult?code={dCode}&companyid={compId}&type=0'
```
[I think the `type` param is for the time window - 0 for 5yrs, 1 for 10yrs, and 2 for max window.] `requests.get(apiUrl, headers=headers).json()` should return something like 
```json
{
    "actual": 124.12623323305537,
    "avg": 83.32096287339556,
    "avgDifference": 48.97359434223362,
    "minValue": 26.353309862919502,
    "minValueRank": 2019,
    "maxValue": 144.51093035368598,
    "maxValueRank": 2020,
    "actual_F": "124,13%",
    "avg_F": "83,32%",
    "avgDifference_F": "48,97% acima da m\u00e9dia",
    "minValue_F": "26,35%",
    "minValueRank_F": "2019",
    "maxValue_F": "144,51%",
    "maxValueRank_F": "2020",
    "chart": {
        "categoryUnique": true,
        "category": [
            "2018",
            "2019",
            "2020",
            "2021",
            "2022"
        ],
        "series": {
            "percentual": [
                {
                    "value": 27.189302754606462,
                    "value_F": "27,19%"
                },
                {
                    "value": 26.353309862919502,
                    "value_F": "26,35%"
                },
                {
                    "value": 144.51093035368598,
                    "value_F": "144,51%"
                },
                {
                    "value": 94.42503816271046,
                    "value_F": "94,43%"
                },
                {
                    "value": 124.12623323305537,
                    "value_F": "124,13%"
                }
            ],
            "proventos": [
                {
                    "value": 7009130357.11,
                    "value_F": "R$ 7.009.130.357,11",
                    "valueSmall_F": "7,01 B"
                },
                {
                    "value": 10577427979.68,
                    "value_F": "R$ 10.577.427.979,68",
                    "valueSmall_F": "10,58 B"
                },
                {
                    "value": 10271836929.54,
                    "value_F": "R$ 10.271.836.929,54",
                    "valueSmall_F": "10,27 B"
                },
                {
                    "value": 100721299707.4,
                    "value_F": "R$ 100.721.299.707,40",
                    "valueSmall_F": "100,72 B"
                },
                {
                    "value": 179966901777.61,
                    "value_F": "R$ 179.966.901.777,61",
                    "valueSmall_F": "179,97 B"
                }
            ],
            "lucroLiquido": [
                {
                    "value": 25779000000.0,
                    "value_F": "R$ 25.779.000.000,00",
                    "valueSmall_F": "25,78 B"
                },
                {
                    "value": 40137000000.0,
                    "value_F": "R$ 40.137.000.000,00",
                    "valueSmall_F": "40,14 B"
                },
                {
                    "value": 7108000000.0,
                    "value_F": "R$ 7.108.000.000,00",
                    "valueSmall_F": "7,11 B"
                },
                {
                    "value": 106668000000.0,
                    "value_F": "R$ 106.668.000.000,00",
                    "valueSmall_F": "106,67 B"
                },
                {
                    "value": 144987000000.0,
                    "value_F": "R$ 144.987.000.000,00",
                    "valueSmall_F": "144,99 B"
                }
            ]
        }
    }
}
```
and then you can get the values you want from there. (I think it includes the chart data as well.)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Álan Gabriel](https://stackoverflow.com/users/19396132)** (2022-11-19): it really worked well, this function that you showed is very useful, as I started studying programming a little while ago, I didn't know how to use selenium, thank you very much

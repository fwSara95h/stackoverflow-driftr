---
title: "How to crawl multiple pages and create a dataframe with parsing?"
site: stackoverflow
question_id: 75280405
answer_id: 75283989
url: https://stackoverflow.com/a/75283989
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2023-01-30T11:49:01Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5b00bbb44e8dfb325ce4fe91e576fa6a03b4b9143fa9a6a08860f159cab63e10
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2023-01-30

Posted on Stack Overflow, <https://stackoverflow.com/a/75283989>, 2023-01-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

There are different ways to get your goal:

- @Driftr95 comes up with a modification of yours using `range()`, that is fine, while iterating a specific number of pages.

- Using a `while-loop` to be flexible in number of pages, without knowing the exact one. You can also use a counter if you like to break the loop at a certain number of iterations.

- ...

I would recommend the second one and also to avoid the bunch of `lists` cause you have to ensure they have the same lenght. Instead use a single `list` with `dicts` that looks more structured.

#### Example

    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    base_url = 'https://www.consilium.europa.eu'
    path ='/en/press/press-releases'
    url = base_url+path
    
    data = []
    
    while True:
        print(url)
        soup = BeautifulSoup(requests.get(url).text)
        for e in soup.select('li.list-item'):
            data.append({
                'date':e.find_previous('h2').text,
                'title':e.h3.text,
                'desc':e.p.text,
                'url':base_url+e.h3.a.get('href')
            })
    
        if soup.select_one('li[aria-label="Go to the next page"] a[href]'):
            url = base_url+path+soup.select_one('li[aria-label="Go to the next page"] a[href]').get('href')
        else:
            break
    
    df = pd.DataFrame(data)

#### Output

|     | date            | title                                                                                                                                                                                                                                   | desc                                                                                                                                                                                                                                                                                                                                                                            | url                                                                                                                                                                                                                                                                                                     |
|----:|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   0 | 30 January 2023 | Statement by the High Representative on behalf of the EU on the alignment of certain third countries concerning restrictive measures in view of the situation in the Democratic Republic of the Congo                                   | Statement by the High Representative on behalf of the European Union on the alignment of certain third countries with Council Implementing Decision (CFSP) 2022/2398 of 8 December 2022 implementing Decision 2010/788/CFSP concerning restrictive measures in view of the situation in the Democratic Republic of the Congo.                                                   | https://www.consilium.europa.eu/en/press/press-releases/2023/01/30/statement-by-the-high-representative-on-behalf-of-the-eu-on-the-alignment-of-certain-third-countries-concerning-restrictive-measures-in-view-of-the-situation-in-the-democratic-republic-of-the-congo/                               |
|   1 | 30 January 2023 | Council adopts recommendation on adequate minimum income                                                                                                                                                                                | The Council adopted a recommendation on adequate minimum income to combat poverty and social exclusion. Income support is considered adequate when it ensures a life in dignity at all stages of life. Member states are recommended to gradually achieve the adequate level of income support by 2030 at the latest, while safeguarding the sustainability of public finances. | https://www.consilium.europa.eu/en/press/press-releases/2023/01/30/council-adopts-recommendation-on-adequate-minimum-income/                                                                                                                                                                            |
|   2 | 27 January 2023 | Forward look: 30 January - 12 February 2023                                                                                                                                                                                             | Overview of the main subjects to be discussed at meetings of the Council of the EU over the next two weeks and upcoming media events.                                                                                                                                                                                                                                           | https://www.consilium.europa.eu/en/press/press-releases/2023/01/27/forward-look/                                                                                                                                                                                                                        |
|   3 | 27 January 2023 | Russia: EU prolongs economic sanctions over Russia’s military aggression against Ukraine                                                                                                                                                | The Council prolonged restrictive measures in view of Russia's actions destabilising the situation in Ukraine by six months.                                                                                                                                                                                                                                                    | https://www.consilium.europa.eu/en/press/press-releases/2023/01/27/russia-eu-prolongs-economic-sanctions-over-russia-s-military-aggression-against-ukraine/                                                                                                                                             |
|   4 | 27 January 2023 | Media advisory – Agriculture and Fisheries Council meeting on 30 January 2023                                                                                                                                                           | Main agenda items, approximate timing, public sessions and press opportunities.                                                                                                                                                                                                                                                                                                 | https://www.consilium.europa.eu/en/press/press-releases/2023/01/27/media-advisory-agriculture-and-fisheries-council-meeting-on-30-january-2023/                                                                                                                                                         |
|...
| 435 | 6 July 2022     | EU support to the African Union Mission in Somalia: Council approves further support under the European Peace Facility                                                                                                                  | The Council approved €120 million in support to the military component of AMISOM/ATMIS for 2022 under the European Peace Facility.                                                                                                                                                                                                                                              | https://www.consilium.europa.eu/en/press/press-releases/2022/07/06/eu-support-to-the-african-union-mission-in-somalia-council-approves-further-support-under-the-european-peace-facility/                                                                                                               |
| 436 | 6 July 2022     | Report by President Charles Michel to the European Parliament plenary session                                                                                                                                                           | Report by European Council President Charles Michel to the European Parliament plenary session on the outcome of the European Council meeting of 23-24 June 2022.                                                                                                                                                                                                               | https://www.consilium.europa.eu/en/press/press-releases/2022/07/06/report-by-president-charles-michel-to-the-european-parliament-plenary-session/                                                                                                                                                       |
| 437 | 5 July 2022     | Declaration by the High Representative on behalf of the EU on the alignment of certain countries concerning restrictive measures against ISIL (Da’esh) and Al-Qaeda and persons, groups, undertakings and entities associated with them | Declaration by the High Representative on behalf of the European Union on the alignment of certain third countries with Council Decision (CFSP) 2022/950 of 20 June 2022 amending Decision (CFSP) 2016/1693 concerning restrictive measures against ISIL (Da’esh) and Al-Qaeda and persons, groups, undertakings and entities associated with them.                             | https://www.consilium.europa.eu/en/press/press-releases/2022/07/05/declaration-by-the-high-representative-on-behalf-of-the-eu-on-the-alignment-of-certain-countries-concerning-restrictive-measures-against-isil-da-esh-and-al-qaeda-and-persons-groups-undertakings-and-entities-associated-with-them/ |
| 438 | 5 July 2022     | Remarks by President Charles Michel after his meeting in Skopje with Prime Minister of North Macedonia Dimitar Kovačevski                                                                                                               | During his visit to North Macedonia, President Michel expressed his support for proposed compromise solution on the country's accession negotiations.                                                                                                                                                                                                                           | https://www.consilium.europa.eu/en/press/press-releases/2022/07/05/remarks-by-president-charles-michel-after-his-meeting-in-skopje-with-prime-minister-of-north-macedonia-dimitar-kovacevski/                                                                                                           |
| 439 | 4 July 2022     | Readout of the telephone conversation between President Charles Michel and Prime Minister of Ethiopia Abiy Ahmed                                                                                                                        | President Charles Michel and Prime Minister of Ethiopia Abiy Ahmed valued their open and frank exchange and agreed to speak in the near future to take stock.                                                                                                                                                                                                                   | https://www.consilium.europa.eu/en/press/press-releases/2022/07/04/readout-of-the-telephone-conversation-between-president-charles-michel-and-prime-minister-of-ethiopia-abiy-ahmed/                                                                                                                    |

...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user21084142 (account no longer exists)** (2023-01-31): Thank you but when I ran the codes it only shows the list of URLs from page 1 to max page like this: [link]https://www.consilium.europa.eu/en/press/press-releases, [link]https://www.consilium.europa.eu/en/press/press-releases?Page=2, etc.
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2023-01-31): There are a lot of pages, so you will know wich one is scraped, `dataframe` will be created after scraping all of them and will be stored in `df`.  so you have to call it in new line with `df` or `print(df)` or what ever you like to do with your `dataframe`. you also can call `data` to check the `list of dicts`

---
title: "How to detect and scrape a specific language version of a multilingual publication, if available?"
site: stackoverflow
question_id: 79578485
answer_id: 79579976
url: https://stackoverflow.com/a/79579976
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2025-04-17T19:44:13Z
last_edited: 2025-04-17T20:09:25Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 65803187cb6d2f5b850e4c496a0357ca4388546bd9b265cb506597d59f32c944
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2025-04-17

Posted on Stack Overflow, <https://stackoverflow.com/a/79579976>, 2025-04-17, last edited 2025-04-17. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

@Driftr95 has already made a clean presentation with the use of the filters. I am also not familiar with the behavior of the filters in detail, but I have seen that the results may break away. 

Therefore, additive a suggestion to approach the topic, should the observation with the filters be confirmed.

Simply iterate over the results and check the language on the detail page and, if necessary, also check for existing language alternatives in English. A good starting point from my point of view are the meta tags, which also show the corresponding content (title, author, PDF link, ...), so that you can actually approach the matter quite generically. 

*Please note, there are also pages that may require a login. you would have to decide how you want to deal with these if necessary, but the direction should be right for you.*

```
data = []

for page_num in range(PAGE_COUNT):
    print(f"\n🔍 Scraping page {page_num + 1}/{PAGE_COUNT}...")
    url = f"https://iris.who.int/discover?filtertype=dateIssued&filter_relational_operator=equals&filter=2025&rpp={RPP}&page={page_num}"
    print(url)
    res = get_with_retries(url)
    if not res:
        print(f"[!] Skipping page {page_num + 1} due to repeated failures.")
        continue
    
    for item in BeautifulSoup(res.text).select('h4.artifact-title a'):
        print(item, BASE_URL + item.get('href'))
        item_res = get_with_retries(BASE_URL + item.get('href'))
        item_soup = BeautifulSoup(item_res.text)

        if item_soup.select_one('#aspect_eperson_LoginChooser_list_login-options'):
            print(BASE_URL + item.get('href')+': needs a login')
            continue
        language = item_soup.select_one('meta[name="citation_language"]').get('content')
        
        if language != 'en':
            for lng in item_soup.select(f'h5 + a[href*="{item.get("href").rsplit("/")[0]}"]'):
                #print(lng.get_text(strip=True))
                if lng.get_text(strip=True) == 'English':
                    lng_res = get_with_retries(lng.get('href'))
                    lng_soup = BeautifulSoup(lng_res.text)
                    d = dict((e.get('name'), e.get('content')) for e in lng_soup.select('meta[name*="citation"]'))
                    break
            if not d:
                print(f'No english version found - fallback to {language}')
                d = dict((e.get('name'), e.get('content')) for e in item_soup.select('meta[name*="citation"]'))
        else:
            d = dict((e.get('name'), e.get('content')) for e in item_soup.select('meta[name*="citation"]'))
        data.append(d)
    

df = pd.DataFrame(data)
relevant_columns = ['citation_keywords', 'citation_language','citation_author', 'citation_pdf_url', 'citation_date','citation_title', 'citation_abstract_html_url', 'citation_publication_date', 'citation_publisher', 'citation_isbn', 'citation_technical_report_number', 'citation_issn']


df[relevant_columns]
```


|    | citation_keywords                                                      | citation_language   | citation_author                                       | citation_pdf_url                                                           | citation_date   | citation_title                                                                                                                     | citation_abstract_html_url               | citation_publication_date   | citation_publisher                                    | citation_isbn                      | citation_technical_report_number   | citation_issn   |
|---:|:-----------------------------------------------------------------------|:--------------------|:------------------------------------------------------|:---------------------------------------------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|:----------------------------|:------------------------------------------------------|:-----------------------------------|:-----------------------------------|:----------------|
|  0 | Technical documents                                                    | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/381041/1/B09337-eng.pdf               | 2025-05-11      | Surveillance for human infections with avian influenza A(H5) viruses: objectives, case definitions, testing and reporting          | https://iris.who.int/handle/10665/381041 | 2025-05-11                  | World Health Organization                             | nan                                | nan                                | nan             |
|  1 | Publications                                                           | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/381088/1/B09329-eng.pdf               | 2025-04-17      | Mental Health Gap Action Programme (mhGAP) guideline for mental, neurological and substance use disorders: executive summary       | https://iris.who.int/handle/10665/381088 | 2025-04-17                  | World Health Organization                             | nan                                | nan                                | nan             |
|  2 | Regional Office for Africa; country cooperation strategy; Publications | en                  | World Health Organization. Regional Office for Africa | https://iris.who.int/bitstream/10665/381092/1/9789290314530-eng.pdf        | 2025-04-17      | Country cooperation strategy 2023–2028, Zimbabwe                                                                                   | https://iris.who.int/handle/10665/381092 | 2025-04-17                  | World Health Organization. Regional Office for Africa | 9789290314530                      | nan                                | nan             |
|  3 | Publications                                                           | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/381095/1/9789240108141-eng.pdf        | 2025-04-17      | WHO consolidated operational handbook on tuberculosis: module 4: treatment and care                                                | https://iris.who.int/handle/10665/381095 | 2025-04-17                  | World Health Organization                             | 9789240108141 (electronic version) | nan                                | nan             |
|...|
| 17 | Publications                                                           | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/381075/1/9789240109100-eng.pdf        | 2025-04-15      | WHO Drug Information 2025, vol. 39, 1 [full issue]                                                                                 | https://iris.who.int/handle/10665/381075 | 2025-04-15                  | World Health Organization                             | 9789240109100 (electronic version) | nan                                | 1010-9609       |
| 18 | Technical documents                                                    | en                  | Flores, Manuel                                        | https://iris.who.int/bitstream/10665/381076/1/B09362-eng.pdf               | 2025-04-15      | Increasing beneficiaries and declining informal caregivers in Spain                                                                | https://iris.who.int/handle/10665/381076 | 2025-04-15                  | World Health Organization                             | nan                                | nan                                | nan             |
| 19 | Publications                                                           | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/381064/1/9789240108363-eng.pdf        | 2025-04-14      | Use of lower-sodium salt substitutes: WHO guideline summary                                                                        | https://iris.who.int/handle/10665/381064 | 2025-04-14                  | World Health Organization                             | 9789240108363 (electronic version) | nan                                | nan             |
| 20 | WHO guideline; Publications                                            | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/380060/1/9789240102965-eng.pdf        | 2024-12-31      | WHO guideline on contact tracing                                                                                                   | https://iris.who.int/handle/10665/380060 | 2024-12-31                  | World Health Organization                             | 9789240102965 (electronic version) | nan                                | nan             |
| 21 | WHO guideline; Publications                                            | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/380060/1/9789240102965-eng.pdf        | 2024-12-31      | WHO guideline on contact tracing                                                                                                   | https://iris.who.int/handle/10665/380060 | 2024-12-31                  | World Health Organization                             | 9789240102965 (electronic version) | nan                                | nan             |
| 22 | Publications                                                           | en                  | Schenck Martínez, Marcela                             | https://iris.who.int/bitstream/10665/381066/1/9789240086296-eng.pdf        | 2025-04-14      | Uruguay: a primary health care case study in the context of the COVID-19 pandemic                                                  | https://iris.who.int/handle/10665/381066 | 2025-04-14                  | World Health Organization                             | 9789240086296 (electronic version) | nan                                | nan             |
| 23 | Technical documents                                                    | en                  | World Health Organization                             | https://iris.who.int/bitstream/10665/380881/1/B09339-eng.pdf               | 2025-03-24      | Interim guidance on social and behavioural research for the mpox public health response, March 2025                                | https://iris.who.int/handle/10665/380881 | 2025-03-24                  | World Health Organization                             | nan                                | nan                                | nan             |

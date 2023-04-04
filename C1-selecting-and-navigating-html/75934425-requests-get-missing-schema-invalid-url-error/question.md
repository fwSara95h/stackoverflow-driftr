---
title: "requests.get Missing Schema Invalid URL error"
site: stackoverflow
question_id: 75934425
url: https://stackoverflow.com/q/75934425
asked: 2023-04-04T22:52:19Z
asked_by: "richard "
asked_by_url: https://stackoverflow.com/users/21568593
last_edited: 2025-10-26T09:20:06Z
last_editor: "jqurious"
last_editor_url: https://stackoverflow.com/users/19355181
tags: [python, web-scraping, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 145
answer_count: 1
accepted_answer_id: 75951865
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2f135006f798880b6c9872cdd5f893347405b7a18dd68aeafd34f786fafe3c6d
---

# requests.get Missing Schema Invalid URL error

Asked by [richard ](https://stackoverflow.com/users/21568593) on Stack Overflow, <https://stackoverflow.com/q/75934425>, 2023-04-04, last edited 2025-10-26 by [jqurious](https://stackoverflow.com/users/19355181). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```py
for year in years:
    data = requests.get(standing_url)
    soup = BeautifulSoup(data.text)
    standing_table = soup.select("table.stats_table")[0]
    
    links = standing_table.find_all("a")
    links = [I.get("href") for I in links]
    links = [I for I in links if "/squads/" in I]
    team_urls = [f"https//fbref.com{I}" for I in links]
    
    for team_url in team_urls:
        team_name = team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
        
        data = requests.get(team_url)
        matches = pd.read_html(data.text, match = "Scores & Fixtures")[0]
        
        soup = BeautifulSoup(data.text)
        links = soup.find_all("a")
        links = [I.get("href") for I in links]
        links = [I for I in links if I and "all_comp/shooting/" in I]
        data = requests.get(f"https://fbref.com{links[0]}")
        shooting = pd.read_html(data.text, match = "Shooting")[0]
        shooting.columns = shooting.columns.droplevel()
```

I wanted to extract the matches data for each team but I keep getting a Missing Schema error at the `data = requests.get(team_url)` line:

```py
# MissingSchema: Invalid URL 'https//fbref.com/en/squads/18bb7c10/Arsenal-Stats': No scheme supplied. Perhaps you meant http://https//fbref.com/en/squads/18bb7c10/Arsenal-Stats?
```

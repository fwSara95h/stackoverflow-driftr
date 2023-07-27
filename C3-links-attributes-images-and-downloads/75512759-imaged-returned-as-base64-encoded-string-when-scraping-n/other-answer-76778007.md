---
title: "Imaged returned as base64 encoded string when scraping news article"
site: stackoverflow
question_id: 75512759
answer_id: 76778007
url: https://stackoverflow.com/a/76778007
author: "chitown88"
author_url: https://stackoverflow.com/users/7752296
posted: 2023-07-27T08:45:24Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c08f57bb2331292afc79c0bd88f905f8f2dac5f89b4cca51e8633fb93d3c2d07
role: another answer on the same question, kept as context; not my work
---

# Answer by [chitown88](https://stackoverflow.com/users/7752296) — 2023-07-27

Posted on Stack Overflow, <https://stackoverflow.com/a/76778007>, 2023-07-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I'd simply use espn's api. You can just pull all the headlines for NBA:

    import requests
    import pandas as pd
    
    url = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/news?team=1'
    jsonData = requests.get(url).json()
    
    articles = jsonData['articles']
    teamIds = pd.json_normalize(articles,
                           record_path=['categories'])
    teamIds = teamIds[(teamIds['teamId'].notnull()) & (teamIds['sportId'] == 46)][['description', 'teamId']].drop_duplicates()
    
    dfs = []
    for idx, row in teamIds.iterrows():
        team = row['description']
        teamId = int(row['teamId'])
        print(team)
        url = f'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/news?team={teamId}'
        jsonData = requests.get(url).json()
    
        articles = jsonData['articles']
        df = pd.json_normalize(articles,
                               record_path=['images'])
        dfs.append(df)
    
    final_df = pd.concat(dfs).drop_duplicates()


**Output:**

    print(final_df.head(10).to_string())
                                                                                           name  width          id                                            credit    type                                                                                                                                                                 url  height dataSourceIdentifier                                  alt                                                                                                                                                       caption
    0                                                                  NBA logo court [600x400]    600  32293398.0                                  Associated Press  header                                                                                                       https://a.espncdn.com/photo/2021/0927/r915150_600x400_3-2.jpg     400                  NaN                                  NaN                                                                                                                                                           NaN
    1                                            NBA post-free agency power rankings [1296x729]   1296  38031584.0                              Illustration by ESPN  header                                                                                                   https://a.espncdn.com/photo/2023/0718/nba_power_rankings_16x9.jpg     729        f5e4098bd673e  NBA post-free agency power rankings                                                                                                                                                              
    2                            Perk on Jaylen Brown's supermax: One championship isn't enough    576         NaN                                               NaN   Media  https://a.espncdn.com/media/motion/2023/0725/dm_230725_dm_230725_NBA_Perk_on_Jaylen_Brown_rev_pub2tag/dm_230725_dm_230725_NBA_Perk_on_Jaylen_Brown_rev_pub2tag.jpg     324                  NaN                                  NaN               Kendrick Perkins and Chiney Ogwumike discuss the expectations on Jaylen Brown following his five-year, $304 million extension with the Celtics.
    3                                                                   Isaiah Mobley [576x324]    576  38022455.0       Photo by Jeff Bottari/NBAE via Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0717/r1198755_576x324_16-9.jpg     324        f834b42626edc                                  NaN                            Isaiah Mobley and the Cleveland Cavaliers will face the Houston Rockets in the NBA 2K24 Summer League championship game on Monday.
    4                                                     Chet Holmgren summer league [576x324]    576  37963701.0  Photo by Melissa Majchrzak/NBAE via Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0705/r1194328_576x324_16-9.jpg     324        b7351111f9cd6                                  NaN  Chet Holmgren scored 15 points and grabbed nine rebounds in the Oklahoma City Thunder's 95-85 win against the Utah Jazz in the Salt Lake City summer league.
    5  Brandon Miller #24 of the Charlotte Hornets defends against Victor Wembanyama  [608x342]    608  37987258.0                         Candice Ward/Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0710/r1196026_608x342_16-9.jpg     342        f53c0bfd44d38                                  NaN                                              Victor Wembanyama and Brandon Miller played against each other on the first night of the NBA 2K24 Summer League.
    6                                                     Chet Holmgren summer league [576x324]    576  37990534.0               Photo by Chris Gardner/Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0710/r1196239_576x324_16-9.jpg     324        e773f8ec23d7c                                  NaN                                      Oklahoma City Thunder forward Chet Holmgren now weighs 208 pounds and appears more physical in his second summer league.
    7                                                                   Chet Holmgren [608x342]    608  37980950.0                Photo by Candice Ward/Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0708/r1195586_608x342_16-9.jpg     342        288a5fc222b16                                  NaN                                                                                                                                                           NaN
    8                                                                  Keyonte George [576x324]    576  38014766.0                Photo by Candice Ward/Getty Images  header                                                                                                     https://a.espncdn.com/photo/2023/0715/r1198090_576x324_16-9.jpg     324        779a8f833ef77                                  NaN                                                                            Keyonte George was one of the best rookies at NBA 2K24 Summer League in Las Vegas.
    9                                                  Cavs win 2023 summer league championship    576         NaN                                               NaN   Media                                                https://a.espncdn.com/media/motion/2023/0717/ss_20230717_225120331_23036861384/ss_20230717_225120331_23036861384.jpg     324                  NaN                                  NaN                                                        The Cavaliers celebrate winning the 2023 summer league championship after defeating the Rockets 99-78.

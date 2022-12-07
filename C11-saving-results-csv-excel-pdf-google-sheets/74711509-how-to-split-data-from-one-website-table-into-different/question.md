---
title: "How to split data from one website table into different outputs using Python"
site: stackoverflow
question_id: 74711509
url: https://stackoverflow.com/q/74711509
asked: 2022-12-07T03:40:47Z
asked_by: "Anthony Madle"
asked_by_url: https://stackoverflow.com/users/19425874
last_edited: 2022-12-07T04:16:33Z
tags: [python, pandas, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 103
answer_count: 1
accepted_answer_id: 74749317
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ceae968d8df845f6dc67c5dbf88c70b0934cca4d4f108ee5d1ef31ee54229c8b
---

# How to split data from one website table into different outputs using Python

Asked by [Anthony Madle](https://stackoverflow.com/users/19425874) on Stack Overflow, <https://stackoverflow.com/q/74711509>, 2022-12-07, last edited 2022-12-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm working on a fun project collecting wave data in New Jersey -- I want to scrape this site every day for the upcoming calendar year and look at trends across the board.

My first step though, is setting up the scrape.  Right now, I'm getting an output that includes what looks like two different tables.  Looking at the site though, it seems they might always be in the same <tbody> tags. 

Is there a way to split this output? I was thinking of doing two different scripts -- one for the "tide data" and the other for the "wave sizes", but it seems I'm not able to split them. (I'm also super new to this)

Ideally, I could have two different scripts that I'll automatically trigger to different tabs of a Google sheet -- I think I can handle that though once I get there.

    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    
    
    id_list = [
        '/Belmar-Surf-Report/3683',
        '/Manasquan-Surf-Report/386/',
        #     '/Ocean-Grove-Surf-Report/7945/',
        #     '/Asbury-Park-Surf-Report/857/',
        #     '/Avon-Surf-Report/4050/',
        #     '/Bay-Head-Surf-Report/4951/',
        #     '/Belmar-Surf-Report/3683/',
        #     '/Boardwalk-Surf-Report/9183/',
        #     '/Bradley-Beach-Surf-Report/7944/',
        #     '/Casino-Surf-Report/9175/',
        #     '/Deal-Surf-Report/822/',
        #     '/Dog-Park-Surf-Report/9174/',
        #     '/Jenkinsons-Surf-Report/4053/',
        #     '/Long-Branch-Surf-Report/7946/',
        #     '/Long-Branch-Surf-Report/7947/',
        #     '/Manasquan-Surf-Report/386/',
        #     '/Monmouth-Beach-Surf-Report/4055/',
        #     '/Ocean-Grove-Surf-Report/7945/',
        #     '/Point-Pleasant-Surf-Report/7942/',
        #     '/Sea-Girt-Surf-Report/7943/',
        #     '/Spring-Lake-Surf-Report/7941/',
        #     '/The-Cove-Surf-Report/385/',
        #     '/Belmar-Surf-Report/3683/',
        #     '/Avon-Surf-Report/4050/',
        #     '/Deal-Surf-Report/822/',
        #     '/North-Street-Surf-Report/4946/',
        #     '/Margate-Pier-Surf-Report/4054/',
        #     '/Ocean-City-NJ-Surf-Report/391/',
        #     '/7th-St-Surf-Report/7918/',
        #     '/Brigantine-Surf-Report/4747/',
        #     '/Brigantine-Seawall-Surf-Report/4942/',
        #     '/Crystals-Surf-Report/4943/',
        #     '/Longport-32nd-St-Surf-Report/1158/',
        #     '/Margate-Pier-Surf-Report/4054/',
        #     '/North-Street-Surf-Report/4946/',
        #     '/Ocean-City-NJ-Surf-Report/391/',
        #     '/South-Carolina-Ave-Surf-Report/4944/',
        #     '/St-James-Surf-Report/7917/',
        #     '/States-Avenue-Surf-Report/390/',
        #     '/Ventnor-Pier-Surf-Report/4945/',
        #     '/14th-Street-Surf-Report/9055/',
        #     '/18th-St-Surf-Report/9056/',
        #     '/30th-St-Surf-Report/9057/',
        #     '/56th-St-Surf-Report/9059/',
        #     '/Diamond-Beach-Surf-Report/9061/',
        #     '/Strathmere-Surf-Report/7919/',
        #     '/The-Cove-Surf-Report/7921/',
        #     '/14th-Street-Surf-Report/9055/',
        #     '/18th-St-Surf-Report/9056/',
        #     '/30th-St-Surf-Report/9057/',
        #     '/56th-St-Surf-Report/9059/',
        #     '/Avalon-Surf-Report/821/',
        #     '/Diamond-Beach-Surf-Report/9061/',
        #     '/Nuns-Beach-Surf-Report/7948/',
        #     '/Poverty-Beach-Surf-Report/4056/',
        #     '/Sea-Isle-City-Surf-Report/1281/',
        #     '/Stockton-Surf-Report/393/',
        #     '/Stone-Harbor-Surf-Report/7920/',
        #     '/Strathmere-Surf-Report/7919/',
        #     '/The-Cove-Surf-Report/7921/',
        #     '/Wildwood-Surf-Report/392/'
    ]
    
    headers = {
    
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
    }
    
    for x in id_list:
    
        url = 'https://magicseaweed.com' + x
    
        r = requests.get(url, headers=headers)
        try:
            soup = BeautifulSoup(r.text, 'html.parser')
            dfs = pd.read_html(str(soup))
            for df in dfs:
                df['City'] = x
                # df.insert(3, "Source", [x], True)
    
                print(df)
                if df.shape[0] > 0:
                    df.to_csv("njwaves3.csv", mode="a", index=False)
                print('____________')
        except Exception as e:
            print(e)

This is an example URL:

<https://magicseaweed.com/Wildwood-Surf-Report/392/>

This is the table data that I want to split -- again, right now I'm receiving both tables in one output; I want one script that pulls all of the wave data, then separately another that pulls the high/low tide data

[![table data][1]][1]


  [1]: https://i.sstatic.net/HGDdP.png


Is this possible? Any insight is much appreciated


UPDATE ---

I was actually able to very easily scrape these tables using simple Google Sheets functions.

Examples are on tabs "Wave Data" and "Tide Data".

Looking at it this way changes things a bit -- it seems all I really want to do is scrape the FIRST and SECOND tables from the URL (I think).

This is the ideal data output:

https://docs.google.com/spreadsheets/d/1mbst-uaRGHWG5ReoFfIsazx0kpY7kXKIBqsRswy1y1Q/edit#gid=1611362673

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[yashtodi94](https://stackoverflow.com/users/3055413)** (2022-12-07): Try out this for scraping html tables. You can then transform it in any way you feel like: https://pypi.org/project/html-table-extractor/

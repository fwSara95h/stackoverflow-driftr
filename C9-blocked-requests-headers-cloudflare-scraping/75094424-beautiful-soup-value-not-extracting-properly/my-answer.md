---
title: "Beautiful Soup Value not extracting properly"
site: stackoverflow
question_id: 75094424
answer_id: 75102700
url: https://stackoverflow.com/a/75102700
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-12T21:54:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75102700/revisions
accepted: true
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a98cf549a2adfe9c7b9307d166f3966735a1d73bb8a215fc9f6f30451dbc2f81
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75102700>, 2023-01-12; **accepted**; score 0. Text as retrieved 2026-10-12.

Probably as a predictive measure, the html fetched by the requests don't seem to consistent in their layouts or even the contents. 

There might be more possible [`selectors`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors), but try

```python
def get_Hotel_Facilities(soup):
    selectors = ['div[data-testid="property-highlights"]', '#facilities', 
                 '.hp-description~div div.important_facility']
    new_list = []
    for sel in selectors:
        for sect in soup.select(sel): 
            new_list += list(sect.stripped_strings)
    return list(set(new_list)) # set <--> unique
```

But even with this, the results are inconsistent. E.g.: I tested on [this page](https://www.booking.com/hotel/in/country-inn-tarika-varca-beach-goa.ja.html?aid=304142&label=gen173rf-1FCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGiAg1wcm9qZWN0cHJvLmlvqAIDuAKwwPadBsACAdICJDU0NThkNDAzLTM1OTMtNDRmOC1iZWQ0LTdhOTNjOTJmOWJlONgCBeACAQ&sid=18ea2a50fe267f571c434ec1d16b784c&all_sr_blocks=902383602_366379939_2_41_0;checkin=2023-01-13;checkout=2023-01-14;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=902383602_366379939_2_41_0;hpos=1;matching_block_id=902383602_366379939_2_41_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=902383602_366379939_2_41_0__800000;srepoch=1673556447;srpvid=5798922f46230054;type=total;ucfs=1&#hotelTmpl) with

```python
for i in range(10):
    soup = BeautifulSoup(cloudscraper.create_scraper().get(url).content)
    fl = get_Hotel_Facilities(soup) if soup else []
    print(f'[{i}] {len(fl)} facilities: {", ".join(fl)}')
```

[![test][1]][1]

(But the inconsistencies might be due to using cloudscraper - maybe you'll get better results with your headers?)

  [1]: https://i.sstatic.net/G3LCv.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[BODDAPALLI KOUSHIK](https://stackoverflow.com/users/18705324)** (2023-01-14): So using the above selectors may solve my problem?
- **me** (2023-01-14): @BODDAPALLIKOUSHIK somewhat. Like I said, the site seems to be rotating through various html structures. My `selectors` list accounts for 3 of them but if there are more, those might still yield empty lists

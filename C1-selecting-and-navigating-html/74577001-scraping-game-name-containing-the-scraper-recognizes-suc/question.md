---
title: "Scraping game name containing the \"@\": scraper recognizes such name as email address"
site: stackoverflow
question_id: 74577001
url: https://stackoverflow.com/q/74577001
asked: 2022-11-25T19:02:09Z
asked_by: "Xiaowei Zhang"
asked_by_url: https://stackoverflow.com/users/18455304
last_edited: never
tags: [python, web-scraping]
score: 0
views_at_snapshot: 118
answer_count: 1
accepted_answer_id: 74587510
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2ab257c724ba9d07bfbdd3136dc4aa8fbafe0f3a8a89c8ad7e06adbbd3a6bd69
---

# Scraping game name containing the "@": scraper recognizes such name as email address

Asked by [Xiaowei Zhang](https://stackoverflow.com/users/18455304) on Stack Overflow, <https://stackoverflow.com/q/74577001>, 2022-11-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape games' information. However, some games' name contains "@", such as the game "[Ampers@t](https://www.mobygames.com/game/amperst)".

When I try to scrape such games' title, the code will return me "[email protected]". Apparently, my code does not recognize that this is game's name, and is not an email.

Here are my codes used.
```
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

def grab_soup(url):
    """Takes a url and returns a BeautifulSoup object"""
    response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})
    assert response.status_code == 200, "Problem with url request! %s throws %s" % (
        url,
        response.status_code,
    )  # checking that it worked
    page = response.text
    soup = BeautifulSoup(page, "lxml")
    return soup

soup = grab_soup("https://www.mobygames.com/game/amperst")

header = soup.find(class_="niceHeaderTitle")("a")
```

What I expect the output of the header is 
```
<a href="https://www.mobygames.com/game/amperst">Ampers@t</a>,
...
```

However, the output is:
```
<a href="https://www.mobygames.com/game/amperst"><span class="__cf_email__" data-cfemail="ce8fa3beabbcbd8eba">[email protected]</span></a>,
...
```

And I try to check the page source of [the game](https://www.mobygames.com/game/amperst). Indeed, the page source is recorded like this:
```
<div class="rightPanelHeader">
<h1 class="niceHeaderTitle">
<a href="https://www.mobygames.com/game/amperst">
<span class="__cf_email__" data-cfemail="cd8ca0bda8bfbe8db9">[email&#160;protected]
</span>
</a>"
```

Therefore, the reason my code gives me the content probably because it is what being recorded in the page source. But IS there a way that I can get rid of this issue?

I found [this solution](https://stackoverflow.com/questions/58103525/how-to-decode-email-xa0protected-while-web-scraping-using-python). But it is undesire for me as I have lots of games to scrape and cannot run the code for each of game.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-11-26): *"Apparently, my code does not recognize that this is game's name, and is not an email"* - that's not the case, you said it's like that in the page source, so it has nothing to do with with your code since it's not receiving the decoded email in the first place....but why *can't* you include that decode function in your scraper code? Is there a speed requirement?
- **[Xiaowei Zhang](https://stackoverflow.com/users/18455304)** (2022-11-26): @Driftr95 I have lots of games (about 10,000) to scrape. Only a few of them contains @ in their names. So, I think it may be ineffective to run the decode function for each of them. Therefore, it is kind of a speed requirement.
- **me** (2022-11-26): why not do it conditionally? something like `for i, h in enumerate(header): if h.get_text() == '[email protected]' and h.get('data-cfemail'): header[i].string = deCFEmail(h.get('data-cfemail'))` shouldn't add *that* much time

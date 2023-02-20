---
title: "Imaged returned as base64 encoded string when scraping news article"
site: stackoverflow
question_id: 75512759
answer_id: 75515179
url: https://stackoverflow.com/a/75515179
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-20T23:42:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75515179/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: [valGetter]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6036911be0736ac13467c3e7724785847d0d5b70c3b43f1920563b0730a958d7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75515179>, 2023-02-20; score 0. Text as retrieved 2026-10-12.

As mentioned in the comments, those are placeholders that are to be updated by JavaScript. Fortunately, the data you want seems to be available [inside a `script` tag][1] in the source HTML. You can slice out the `window['__espnfitt__']` object from the script and then parse it as [`json`](https://docs.python.org/3/library/json.html) before extracting the details you want.

```python
import requests, json
from bs4 import BeautifulSoup

#################################################
# for printing and returning in one statement ###
def vRet(toPrint, toRet=[]):                   ##
    print(toPrint)                             ##
    return toRet                               ##
                                               ##
## extract a nested value with a list of keys ###
def valgetter(obj, *keys, defaultVal=None):    ##
    try:                                       ##
        for k in keys: obj = obj[k]            ##
    except: return defaultVal                  ##
    return obj                                ###
#################################################


def get_team_stories(team_endpt):
    teamUrl = f'https://www.espn.com/nba/team/_/name/{team_endpt}'
    resp = requests.get(teamUrl)
    rMsg = f'[Received <{resp.status_code} {resp.reason}> from {resp.url}]\n'
    if not resp.ok: return vRet(f'{rMsg}! Failed to scrape {teamUrl}')

    soup = BeautifulSoup(resp.content, 'html.parser')
    try:
        pgData = json.loads(soup.find(
            'script', string=lambda s: s and ''.join(
                s.split()).startswith("window['__espnfitt__']=")
        ).text.split('=', 1)[-1].strip().strip(';'))['page']

        team_heading = pgData['meta']['title'].split('-')[0].strip()
        clubhouseCols = pgData['content']['clubhouse']['columns']
        articles = clubhouseCols['middleColumn']['clubhouse']['feed']
    except Exception as e: return vRet(repr(e))

    if not isinstance(articles, list): 
        return vRet(f'{rMsg}Expected list of articles, not {type(articles)}')
    if not articles: return vRet(f'{rMsg}No articles for {team_endpt}')

    def formLink(l):
        if not isinstance(l, str): return l 
        if l.startswith('/espn/'): 
            return l.replace('/espn/', 'https://www.espn.com/', 1)
        if l.startswith('/'): return f'https://www.espn.com{l}'
        return l

    rData = [{
        'team_heading': team_heading, 'headline': a['headline'], 
        'link': formLink(a['link']), 'img_url': valgetter(a,'image','url')
    } for a in articles if isinstance(a, dict) and 'headline' in a]
    if len(rData) != len(articles): 
        print(f'! Could only extract {len(rData)} of {len(articles)} articles')
    return rData 
```

---

I tested the function above with

```python
team_endpoints = ['bos/boston-celtics', 'phi/philadelphia-76ers', 
                  'bkn/brooklyn-nets', 'ny/new-york-knicks']
team_stories = []
for te in team_endpoints: team_stories += get_team_stories(te)

print(len(team_stories), 'articles collected\n')
```

[![opdf][2]][2]


  [1]: https://i.sstatic.net/mxblz.png
  [2]: https://i.sstatic.net/y0n3O.png

---
title: "Can someone help me properly scrape YouTube titles in Python using BS4?"
site: stackoverflow
question_id: 76361069
answer_id: 76366675
url: https://stackoverflow.com/a/76366675
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-05-30T16:05:44Z
last_edited: 2023-05-30T16:12:29Z
revisions: 2
revision_history: https://stackoverflow.com/posts/76366675/revisions
accepted: true
score: 1
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 52df6d996e58e9db47626eb7891a9e33896a52c0b99553d83708fb10fef2ba7c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-05-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76366675>, 2023-05-30, last edited 2023-05-30; **accepted**; score 1. Text as retrieved 2026-10-12.

Your code is using `requests.get` so you'll only get the [source html](https://www.lifewire.com/view-html-source-in-chrome-3466725), which is [**not** the same as](https://egghead.io/lessons/misc-chrome-devtools-elements-inspect-elements-vs-view-source) the fully rendered HTML you might inspect on your browser. For that, you might want to use something that supports JavaScript (like [selenium](https://medium.com/ymedialabs-innovation/2f8ad15efe25) - and don't forget to add in some wait time to allow the page to load....).

However, if all you want are some titles, you can try extracting from the `script` tags that contain the JavaScript with the following functions:

```py
# import json

## a general function for extracting a JavaScript variable from a bs4 object
def get_jsScriptVal(jSoup, valDecl, isJson=True):
    script_finder = lambda s: s and valDecl in s
    for sc in jSoup.find('script', string=script_finder):
        for st in  sc.string.split(';'):
            ls, rs, *_ = [s.strip() for s in (st.split('=', 1) + [''])]
            if ls == valDecl and rs: return json.loads(rs) if isJson else rs


## specifically for your case
def get_ytInitialTitles(ySoup):
    contents = get_jsScriptVal(ySoup, 'var ytInitialData')['contents']
    tab1 = contents['twoColumnBrowseResultsRenderer']['tabs'][0]
    contents = tab1['tabRenderer']['content']['richGridRenderer']['contents']
    contents = [c['richItemRenderer']['content']['videoRenderer'] 
                for c in contents if 'richItemRenderer' in c and 
                'videoRenderer' in c['richItemRenderer']['content']]
    titles = [c['title']['runs'][0]['text'] for c in contents]
    return titles
```

---

Now, if you edit your code to use the functions above:

```py
import requests
from bs4 import BeautifulSoup
import json

#### DON'T FORGET TO PASTE THE FUNCTION DEFINITIONS INTO YOUR CODE TOO ####
## def get_jsScriptVal....
## def get_ytInitialTitles....
##########################################################################

def get_youtube_titles():
    url = 'https://www.youtube.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # titles = get_ytInitialTitles(soup) # Find YouTube title elements
        # for title in titles: print(title) # Extract and print the titles

        # OR [in one line]
        for title in get_ytInitialTitles(soup): print(title)
    
    except Exception as e:
        print('Failed to scrape due to', type(e), ':', e)

get_youtube_titles()
```

then it should print something like

> ```lang-none
> Survive 100 Days In Circle, Win $500,000
> lofi hip hop radio 📚 - beats to relax/study to
> Spectaculair ingekleurde film over het begin van de Duitse bezetting van Nederland tijdens WOII
> Omtzigt is WOEST & SLOOPT liegende Rutte! 'Kijk die ouders in hun ogen!'
> Ineens vielen er bommen op zonnepanelen... Algemene beschouwingen Venlo 2023
> Trump Opens Up on Secret White House Documents, Biden Family & Republican Opponents | Trump LIVE
> An einem Tag nach Mallorca und zurück: Was verdient ein Flugbegleiter? | Lohnt sich das | BR
> I BUILT A SHELTER IN THE FOREST!! AND LIVED THERE FOR 2 MONTHS!
> De halvering van China
> Ibiza Summer Mix 2023 🍓 Best Of Tropical Deep House Music Chill Out Mix 2023🍓 Chillout Lounge #153
> Tibetaanse Genezende Fluit • Afgifte van melatonine en gifstoffen • Elimineer stress en kalmeer ...
> Alle 200 POTLODEN GEBRUIKEN in 1 TEKENING - Tekenen Challenge
> Top 10 BEST Auditions on BGT 2023!
> Ontspannende muziek tot opluchting stress, angst en depressie 🐬 Verzachtende muziek voor zenuwen
> 6 juni 1944, D-Day, Operatie Overlord | Ingekleurd
> Ed Sheeran, Martin Garrix, Kygo, Dua Lipa, Avicii, Robin Schulz, The Chainsmokers Style - Feeling Me
> DIY with Mr Bean | Full Episodes | Classic Mr Bean
> EEN WEDSTRIJD VOL AFSCHEID! 😭🫡 | Barcelona vs Mallorca | La Liga 2022/23 | Samenvatting
> Deep Focus Music To Improve Concentration - 12 Hours of Ambient Study Music to Concentrate #506
> The Inside Guys React To The Miami Heat's Blowout Game 7 Win In Boston | NBA on TNT
> Muziek genezen om stress, vermoeidheid, depressie, negativiteit, detoxemoties te verlichten
> How Rain Caused Havoc And Changed The Race | 2023 Monaco Grand Prix
> ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Peter](https://stackoverflow.com/users/15442983)** (2023-05-31): thanks for your kindness.  i really appreciate you. i hope you have a good day. : )

---
title: "Flask-based youtube playlist calculator giving null/incorrect output"
site: stackoverflow
question_id: 75918949
answer_id: 75940405
url: https://stackoverflow.com/a/75940405
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-05T14:03:18Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75940405/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: [script-JSON extractor]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0238d86f1279db69a2f213c232e3d373089341c26031efbd1269c309f340e171
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75940405>, 2023-04-05; score 0. Text as retrieved 2026-10-12.

YouTube playlist pages are [dynamic](https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_dynamic_websites.htm), and if you preview the [source HTML](https://egghead.io/lessons/misc-chrome-devtools-elements-inspect-elements-vs-view-source) (which is all you get with *`requests.get(playlist_url).text`*) in the [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) (it should be the first request if you refresh the page)<sup>([view example][1])</sup>, then you'll see that pretty much everything is rendered with JavaScript. 

Because of this, you can expect *`soup.select('span.ytd-thumbnail-overlay-time-status-renderer')`* to return an empty ResultSet.<sup>([view example][2])</sup>

The good news is that the data you want *is* there in the source HTML, inside a `script` tag, from which various information can be extracted<sup>([view example][3] with [this function](https://pastebin.com/UYJUqtXF))</sup>; so, if you alter `calculate_playlist_length` to something like

```py
def calculate_playlist_length(playlist_url):
    pSoup = BeautifulSoup((r:=requests.get(playlist_url)).content, 'html.parser') 
    rStatus = f'<Response [{r.status_code} {r.reason}]> from {r.url}'

    jScript = pSoup.select_one('script:-soup-contains("var ytInitialData")')
    try: 
        jData = json.loads(jScript.string.split('=',1)[-1].strip().rstrip(';'))
        
        keysList = [
            'contents', 'twoColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer',
            'content', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer',
            'contents', 0, 'playlistVideoListRenderer', 'contents'
        ]
        for k in keysList: jData = jData[k]
        vidLength = lambda v: int(v['playlistVideoRenderer'].get('lengthSeconds',0))

        total_seconds = sum([vidLength(vid) for vid in jData])
    except Exception as e: total_seconds, _ = 0, print(f'{rStatus}\n{e!r}') 
    return (total_seconds//3600), ((total_seconds%3600)//60), (total_seconds%60)
```

then `calculate_playlist_length(url)` should return <kbd>**`(0, 35, 46)`**</kbd> if `url` has been set to link [this playlist](https://www.youtube.com/playlist?list=PL5A4nPQbUF8CHsZzDMBFFOwHlMOun8vEU).


  [1]: https://i.sstatic.net/MtQEa.png
  [2]: https://i.sstatic.net/F6E25.png
  [3]: https://i.sstatic.net/k12b9.png

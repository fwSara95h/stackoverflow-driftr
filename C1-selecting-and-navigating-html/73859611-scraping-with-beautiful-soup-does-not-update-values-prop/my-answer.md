---
title: "Scraping with Beautiful Soup does not update values properly"
site: stackoverflow
question_id: 73859611
answer_id: 73862506
url: https://stackoverflow.com/a/73862506
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-27T04:46:24Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73862506/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [getReqUrl]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ba01caf53608d879d7d8d8e49fe3ec5d76f3ee8c3c9bd1fe859598e37e3c433
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73862506>, 2022-09-27; **accepted**; score 1. Text as retrieved 2026-10-12.

You could try this alternate method: since the site actually retrieves the data from another url, you could just directly make the request and scrape the site only every hour or so to update the request url.

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import json
    from datetime import datetime, timedelta
    #def getReqUrl...

    reqUrl = getReqUrl()
    prevTime, prevAt = '', datetime.now()
    while True:
      ures = json.loads(urlopen(reqUrl).read())
      if 'observations' not in asd:
        reqUrl = getReqUrl()
        ures = json.loads(urlopen(reqUrl).read())

      #to see time since last update
      obvTime = ures['observations'][0]['obsTimeUtc']
      td = (datetime.now() - prevAt).seconds 

      wSpeed = ures['observations'][0]['imperial']['windSpeed']
      wGust = ures['observations'][0]['imperial']['windGust']
      print('',end=f'\r[+{td}s -> {obvTime}]:   {wGust} ° / {wSpeed} °mph')

      if prevTime < obvTime:
        prevTime = obvTime
        prevAt = datetime.now()
        print('')

Even when making the request directly, the "observation time" in the retrieved data jumps around sometimes, which is why I'm only printing on a fresh line [when `obvTime` increases][1] - without that, [it looks like this][2]. (If that's preferred you can just print normally without the `'',end='\r...` format, and the second `if` block is no longer necessary either).

The first `if` block is for refreshing the `reqUrl` (because it expires after a while), which is when I actually scrape the wunderground site, because the url is inside one of their `script` tags:

    def getReqUrl():
      url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'    
      soup = BeautifulSoup(urlopen(url), 'html.parser')
      appText = soup.select_one('#app-root-state').text

      nxtSt = json.loads(appText.replace('&q;','"'))['wu-next-state-key'] 
      return [
          ns for ns in nxtSt.values() 
          if 'observations' in ns['value'] and 
          len(ns['value']['observations']) == 1
      ][0]['url'].replace('&a;','&')

or, since I know how the url starts, more simply like:

    def getReqUrl():
      url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'    
      soup = BeautifulSoup(urlopen(url), 'html.parser')
      appText = soup.select_one('#app-root-state').text
      
      rUrl = 'https://api.weather.com/v2/pws/observations/current'
      rUrl = rUrl + appText.split(rUrl)[1].split('&q;')[0]
      return rUrl.replace('&a;','&')

  [1]: https://i.sstatic.net/qbsKP.png
  [2]: https://i.sstatic.net/j6wwd.png

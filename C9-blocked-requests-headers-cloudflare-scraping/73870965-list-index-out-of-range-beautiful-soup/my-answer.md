---
title: "list index out of range - beautiful soup"
site: stackoverflow
question_id: 73870965
answer_id: 73874251
url: https://stackoverflow.com/a/73874251
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-27T22:09:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73874251/revisions
accepted: true
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [getReqUrl]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e58ebe4067dea4dfc52988ac1a1c2738d8b798ce478d9bd938c7b3ecba84dc4b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73874251>, 2022-09-27; **accepted**; score 0. Text as retrieved 2026-10-12.

You can't expect code tailored to scrape one website to work for a different link! You should always [inspect][1] and explore your target site, especially the parts you need to scrape, so you know the tag names [like `td` and `a` here] and identifying attributes [like `name`, `id`, `class`, etc.] of the elements you need to extract data from.

With this site, if you want the info from the `reportTable`, it gets generated after the page gets loaded with javascript, so it wouldn't show up in the `request` response. You could either try something like [Selenium][2], or you could try retrieving the data from the source itself.

If you [inspect the site and look at the network tab][3], you'll find a request (which is what actually retrieves the data for the table) that looks [like this][4], and when you [inspect the table's html][5], you'll find above it the scripts to generate the data.

In the suggested solution below, the `getReqUrl` scrapes your link to get the url for requesting the reports (and also the template of the url for downloading the documents).
    
    def getReqUrl(scrapeUrl):
      res = requests.get(scrapeUrl)
      ercot_soup = BeautifulSoup(res.text, "html.parser")
    
      script = [l.split('"') for l in [
          s for s in ercot_soup.select('script')
          if 'reportListUrl' in  s.text 
          and 'reportTypeID' in s.text
      ][0].text.split('\n') if l.count('"') == 2]
    
      rtID = [l[1] for l in script if 'reportTypeID' in l[0]][0]
      rlUrl = [l[1] for l in script if 'reportListUrl' in l[0]][0]
      rdUrl = [l[1] for l in script if 'reportDownloadUrl' in l[0]][0]
    
      return f'{rlUrl}{rtID}&_={int(time.time())}', rdUrl

(I couldn't figure out how to scrape the last query parameter [the `&_=...` part] from the site exactly, but `{int(time.time())}}` seems to get close enough - the results are the same even then and even when that last bit is omitted entirely; so it's totally optional.)

The url returned can be used to request the documents:

    #import json

    url = 'https://www.ercot.com/mp/data-products/data-product-details?id=NP3-233-CD'
    reqUrl, ddUrl = getReqUrl(url)
    reqRes = requests.get(reqUrl[0]).text
    rsJson = json.loads(reqRes)
    
    for doc in rsJson['ListDocsByRptTypeRes']['DocumentList']:
      d = doc['Document'] 
      downloadLink = ddUrl+d['DocID']
      #print(f"{d['FriendlyName']} {d['PublishDate']} {downloadLink}")
      print(f"Download '{d['ConstructedName']}' at\n\t {downloadLink}")
    print(len(rsJson['ListDocsByRptTypeRes']['DocumentList']))

The `print` results will look like [![enter image description here][6]][6]


  [1]: https://www.thedataschool.co.uk/conrad-wilson/scraping-a-web-page-part-1-inspecting-the-html
  [2]: https://www.scrapingbee.com/blog/selenium-python/
  [3]: https://help.fullstory.com/hc/en-us/articles/360020623654-How-do-I-use-the-Network-view-in-Dev-Tools-
  [4]: https://i.sstatic.net/HsYpv.png
  [5]: https://i.sstatic.net/RnBL4.png
  [6]: https://i.sstatic.net/4MMO7.png

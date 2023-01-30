---
title: "Isolating a link with beautifulsoup"
site: stackoverflow
question_id: 75250425
answer_id: 75280477
url: https://stackoverflow.com/a/75280477
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-30T05:14:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75280477/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [queue crawler]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80a2a15daf0c7d30ea425ffbd9592d6ee5d7518607021061a8b0caebefbc3ef9
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75280477>, 2023-01-30; score 0. Text as retrieved 2026-10-12.

> Is there any way I can instead just isolate the "next" link that is on each page and go through that recursively till I reach the end?

If you mean buttons like 

|[![next_1][1]][1]|
|:-:|
||
|**OR**| 
||
|[![next_2][2]][2]|

then you can look for `a` tags with `data-rnwi-handle="BaseCard"` and [because "Previous" button has the same attribute] containing "Next" as as the first [[stripped] string](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings) (see `aNxt` below). You don't need to utilize recursion necessarily - since each page has just one "Next" [at most], a `while` loop should suffice:

```python
# from urllib.parse import urljoin # [ if you use it ]

rootUrl = 'https://crmhelpcenter.gitbook.io'
nxtUrl = f'{rootUrl}/wahi-digital/getting-started/readme'
nextUrls = [nxtUrl]
# allUrls = [nxtUrl] # [ if you want to collect ]
while nxtUrl:
    resp = requests.get(nxtUrl)
    print([len(nextUrls)], resp.status_code, resp.reason, 'from', resp.url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    ### EXTRACT ANY PAGE DATA YOU WANT TO COLLECT ###
    # pgUrl = {urljoin(nxtUrl, a["href"]) for a in soup.select('a[href]')}
    # allUrls += [l for l in pgUrl if l not in allUrls]

    aNxt = [a for a in soup.find_all(
        'a', {'href': True, 'data-rnwi-handle': 'BaseCard'}
    ) if list(a.stripped_strings)[:1]==['Next']]
    
    # nxtUrl = urljoin(nxtUrl, aNxt[0]["href"]) if aNxt else None
    nxtUrl = f'{rootUrl}{aNxt[0]["href"]}' if aNxt else None
    nextUrls.append(nxtUrl) # the last item will [most likely] be None
# if nxtUrl is None: nextUrls = nextUrls[:-1] # remove last item if None
```

On colab this took about 3min to run and collect 344[+1 for `None`] items in `nextUrls` and 2879 in `allUrls`; omitting or keeping `allUrls` does not seem to make any significant difference in this duration, since the most of the delay is due to the request (and some due to parsing).

You can also try to scrape *all* ~3k links with [this queue-based crawler](https://pastebin.com/t4scGj7C). [It took about 15min in my colab notebook.] The results of that, as well as `nextUrls` and `allUrls` have been uploaded to **[this spreadsheet](https://docs.google.com/spreadsheets/d/1rMgkO9S1s_HKXBzJps5qfvrjVf-YtmqJ9Hp6_UFqGls/edit?usp=sharing)**.


  [1]: https://i.sstatic.net/eqHYX.png
  [2]: https://i.sstatic.net/wVVmI.png

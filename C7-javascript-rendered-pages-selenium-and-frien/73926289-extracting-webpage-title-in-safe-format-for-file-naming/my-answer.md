---
title: "Extracting Webpage Title in Safe Format for File Naming"
site: stackoverflow
question_id: 73926289
answer_id: 73928355
url: https://stackoverflow.com/a/73928355
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-02T18:29:16Z
last_edited: 2022-10-02T21:56:52Z
revisions: 3
revision_history: https://stackoverflow.com/posts/73928355/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 73f95be17dc337dd9ca0f5b5f2b116c5a3c28240257e41be5c9e36c042e6f9f7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73928355>, 2022-10-02, last edited 2022-10-02; score 1. Text as retrieved 2026-10-12.

I'm afraid I don't know of any *"all-purpose page-title retrieval in browser save format"*, but what you're doing so far is not too bad (though I particularly prefer the method suggested in [this answer](https://stackoverflow.com/a/295152/12652373) and its comments from [@](https://stackoverflow.com/users/1498405/hardmooth)hardmooth and [@](https://stackoverflow.com/users/627278/alex-krycek)AlexKrycek). 

You can always save it as a little function if you'll be needing it often and use something like [urlparse](https://stackoverflow.com/a/56476496/12652373) or [tldextract](https://pypi.org/project/tldextract/) to get the domain if you'll be using sites other than YouTube as well.

So something like:

    # import tldextract

    def cleanPageTitle(origTitle, pageUrl):
        domain = tldextract.extract(pageUrl).domain
        cleaned = "".join([
                x for x in origTitle if (x.isalnum() or x in "._- ")
            ]).replace(domain, "")
        return cleaned

so that you can just call as 

    title = cleanPageTitle(br.title(), "https://www.youtube.com/watch?v=RvCBzhhydNk")

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[pglove](https://stackoverflow.com/users/1485503)** (2022-10-03): I like the look of 'isalnum', never seen that before, very nice!
- **me** (2022-10-03): @pglove That's exactly what the first thought I had when I came across that answer =)

---
title: "BeautifulSoup: How to add script src attribute with querystring without encoding the url?"
site: stackoverflow
question_id: 74192079
url: https://stackoverflow.com/q/74192079
asked: 2022-10-25T09:44:53Z
asked_by: "Daniel Vygolov"
asked_by_url: https://stackoverflow.com/users/1194200
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 185
answer_count: 1
accepted_answer_id: 74196605
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c06f2ebe875e78f9a741ec84f5d52aa69d47f95b5a7132347c0051f67fd5269b
---

# BeautifulSoup: How to add script src attribute with querystring without encoding the url?

Asked by [Daniel Vygolov](https://stackoverflow.com/users/1194200) on Stack Overflow, <https://stackoverflow.com/q/74192079>, 2022-10-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need to add a new script tag that has query parameters to my html document so I tried this:

    jsmanager = self.soup.new_tag("script", src="https://example.com/myscript.js?data=test&alarm=1")
    self.soup.select_one("head").append(jsmanager)

The problem is that after the script element is added the url in the src attribute looks like this:

    https://example.com/myscript.js?data=test&amp;alarm=1

Is there any way to add src attribute without html-encoding it's value? (The &amp; thing).

Thanks in advance!

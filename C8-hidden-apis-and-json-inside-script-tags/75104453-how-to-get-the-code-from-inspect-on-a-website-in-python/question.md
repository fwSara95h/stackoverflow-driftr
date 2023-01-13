---
title: "How to get the code from Inspect on a website in Python (dynamic content different from source code)"
site: stackoverflow
question_id: 75104453
url: https://stackoverflow.com/q/75104453
asked: 2023-01-13T03:02:54Z
asked_by: "CELLSecret"
asked_by_url: https://stackoverflow.com/users/13888956
last_edited: never
tags: [python, html, web-scraping, dynamic]
score: 0
views_at_snapshot: 102
answer_count: 1
accepted_answer_id: 75115221
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dbb90b54d1d99690dbc778d399b2231626a3d22422c5e361bb2d7b947e85530b
---

# How to get the code from Inspect on a website in Python (dynamic content different from source code)

Asked by [CELLSecret](https://stackoverflow.com/users/13888956) on Stack Overflow, <https://stackoverflow.com/q/75104453>, 2023-01-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When I try to get the source code for a website, I would usually use `urllib.request.urlopen(url)`. However, when I try to do it for a website with a table (that I believe generated after javascript code is run), it does not return the same as what I see when I press `inspect` on a website. 

How can I get what I see in `inspect` *after* the page is loaded?

I have tried using `json` backage and load the page using `json.load(urllib.request.urlopen(url))`, I would get an error:

[![enter image description here][1]][1]

I also tried to use selenium Webdriver, but when I call `webdrive.Chrome()` an error is generated:

```
WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127
```

How can I fix either of these solutions? Or is there a better solution? Any help would be appeciated.

I'm using replit if that matters.

  [1]: https://i.sstatic.net/fwr4n.jpg

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-01-13): https://stackoverflow.com/q/49323099 for the 127 error. can you share the site and include which table you're trying to get? there might be an API alternative or some data buried in `script` tags in the source code
- **[CELLSecret](https://stackoverflow.com/users/13888956)** (2023-01-13): @Driftr95 I saw this post. I don't think I can run those terminal commands since I'm using replit though.   This is the [site](https://data.eastmoney.com/stock/tradedetail/2023-01-13.html) I'm using (It's in Chinese, but there is only one table so it should be clear which one I'm referring to).

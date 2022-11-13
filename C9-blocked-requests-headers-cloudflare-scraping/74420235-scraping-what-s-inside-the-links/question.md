---
title: "Scraping what's inside the links"
site: stackoverflow
question_id: 74420235
url: https://stackoverflow.com/q/74420235
asked: 2022-11-13T10:46:56Z
asked_by: "ninj"
asked_by_url: https://stackoverflow.com/users/20491929
last_edited: 2022-11-13T11:19:07Z
last_editor: "baduker"
last_editor_url: https://stackoverflow.com/users/6106791
tags: [python, web-scraping]
score: -2
views_at_snapshot: 199
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ea454d2f2469f68552922472809084622144688b61257706ad47d2bdccd2df5c
---

# Scraping what's inside the links

Asked by [ninj](https://stackoverflow.com/users/20491929) on Stack Overflow, <https://stackoverflow.com/q/74420235>, 2022-11-13, last edited 2022-11-13 by [baduker](https://stackoverflow.com/users/6106791). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I don't really have code for this problem. But I will try my best to actually explain everything.

[![Example](https://i.sstatic.net/nQVBp.png)](https://i.sstatic.net/nQVBp.png)
alright, say you are scraping a website, and in the website there are 3 different links and you want to scrape what is inside each and everyone one of them without having to manually do it. Is this possible for just BeautifulSoup and the Requests library? Or would you have to use another library, for e.g scrapy.


If you want you can try it on this website: https://www.bleepingcomputer.com/
What I am trying to achieve is scrape the website, and what is inside the links at the same time.

If it's not possible to do it with only requests & Beautifulsoup feel free to use scrapy as well.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[hopperelec](https://stackoverflow.com/users/17168710)** (2022-11-13): Assuming the links are hyperlinks (a tags) and not buttons, you can access where they are redirecting to through the href property
- **[Community](https://stackoverflow.com/users/-1)** (2022-11-13): Please edit the question to limit it to a specific problem with enough detail to identify an adequate answer.
- **[hopperelec](https://stackoverflow.com/users/17168710)** (2022-11-13): Does this answer your question? [retrieve links from web page using python and BeautifulSoup](https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup)
- **[ninj](https://stackoverflow.com/users/20491929)** (2022-11-13): @hopperelec no, because I'm trying to scrape the content inside the links, not the links itself.
- **[hopperelec](https://stackoverflow.com/users/17168710)** (2022-11-13): @ninj Then why don't you just scrape it the same way you would with any other HTML element? Links are just HTML elements and the content of the link is the content of the HTML element
- **[ninj](https://stackoverflow.com/users/20491929)** (2022-11-13): @hopperelec the aim is to scrape what is INSIDE the link. So a new page for e.g
- **[hopperelec](https://stackoverflow.com/users/17168710)** (2022-11-13): That's not 'inside the link'. That is a completely different page the link happened to be linking to. You would need to make a new request to the linked page. You should edit your question to make it more clear because the way it is currently worded, it would usually mean two completely different things.
- **[ninj](https://stackoverflow.com/users/20491929)** (2022-11-13): @hopperelec but would it be possible to automatically just go to the link and scrape everything in there?
- **[hopperelec](https://stackoverflow.com/users/17168710)** (2022-11-13): You would need to make a new request to the linked page

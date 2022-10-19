---
title: "Python Web scraper for Stackoverflow"
site: stackoverflow
question_id: 74129800
url: https://stackoverflow.com/q/74129800
asked: 2022-10-19T17:48:03Z
asked_by: "Ultra Instinct Shaggy"
asked_by_url: https://stackoverflow.com/users/11850237
last_edited: 2022-10-19T17:48:44Z
last_editor: "Rahul K P"
last_editor_url: https://stackoverflow.com/users/4407666
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 188
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9f9b79bc57022f991084db520ce53958eef80c250e511e4a59b30693107655b4
---

# Python Web scraper for Stackoverflow

Asked by [Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237) on Stack Overflow, <https://stackoverflow.com/q/74129800>, 2022-10-19, last edited 2022-10-19 by [Rahul K P](https://stackoverflow.com/users/4407666). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm a newbie Python programmer learning how to design web scrapers. The tutorial I'm following used the code I've posted below and I'm trying to follow it. However, the code runs without displaying any info, plus I get two problem messages in VSCode telling me that:
1) Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely *pylint (missing-timeout) [Ln 4, Col 12]*

2)Missing module docstring *pylint(missing-module-docstring)[Ln 1,Col 1]*

    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get("https://stackoverflow.com/questions")
    soup = BeautifulSoup(response.text, "html.parser")
    
    questions = soup.select(".s-post-summary    js-post-summary")
    for question in questions:
        print(question.select_one(".s-link").getText())

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[esqew](https://stackoverflow.com/users/269970)** (2022-10-19): `soup.select(".s-post-summary    js-post-summary")` Is there truly a `js-post-summary` element type in `response`? I would doubt as much - have you verified this?
- **[Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237)** (2022-10-19): I inspected the site and saw the div class as such
- **[esqew](https://stackoverflow.com/users/269970)** (2022-10-19): Firstly - if that’s a *class name*, you’re missing the `.` in front of it. Secondly - it’s possible the returned content in `response` doesn’t match what you inspected in your browser.
- **[Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237)** (2022-10-19): I have a screenshot to confirm that indeed, that was the class name. Also, I placed the . in front of the entire _class name_
- **[Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237)** (2022-10-19): I dunno if it helps that the tutorial I'm following is a python tutorial from 4 years ago The current tutorials I have don't include creating web crawlers
- **[esqew](https://stackoverflow.com/users/269970)** (2022-10-19): Right, but in CSS style selectors, *each* class name must be prepended with a full stop.  Additionally, white space between tokens indicates to the parsing engine that it should look for decendants in order of the tokens provided. How about `.s-post-summary.js-post-summary`?
- **[Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237)** (2022-10-19): So if you can kindly help me out with some experimental code, I'd be grateful
- **[Ultra Instinct Shaggy](https://stackoverflow.com/users/11850237)** (2022-10-19): How do I solve the missing timeout arguments problem
- **me** (2022-10-20): @UltraInstinctShaggy just pass `timeout=5` to your request - make it a really big number if you don't care how long it'll take

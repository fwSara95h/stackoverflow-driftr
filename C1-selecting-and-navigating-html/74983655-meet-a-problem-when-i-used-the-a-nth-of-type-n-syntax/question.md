---
title: "meet a problem when I used the a:nth-of-type(n) syntax"
site: stackoverflow
question_id: 74983655
url: https://stackoverflow.com/q/74983655
asked: 2023-01-02T14:34:21Z
asked_by: "TryingToLearnSomething"
asked_by_url: https://stackoverflow.com/users/19511524
last_edited: 2023-01-02T14:35:07Z
tags: [python, beautifulsoup]
score: -1
views_at_snapshot: 30
answer_count: 1
accepted_answer_id: 74987691
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 76d1398371d38f504a9b8f06a0e8543d8c0dd928db36586b04633da35df14c9a
---

# meet a problem when I used the a:nth-of-type(n) syntax

Asked by [TryingToLearnSomething](https://stackoverflow.com/users/19511524) on Stack Overflow, <https://stackoverflow.com/q/74983655>, 2023-01-02, last edited 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am new to using beautiful soup, and I encounter an interesting problem
The code is following:

    html_doc = """
    <html><head><title>"happy new year"</title></head>
    <body>
    <p class="title"><b>c.biancheng.net</b></p>
    <p class="website">2022 is last year</p>
    <a href="http://c.biancheng.net/python/" id="link1">2023 is the new year</a>
    <a href="http://c.biancheng.net/c/" id="link2">hope you will be better</a>
    <a href="http://c.biancheng.net/django/" id="link3">achieve more</a>
    <p class="VIP">YEAH</p>
    <a href="http://vip.biancheng.net/?from=index" id="link4">and realize your dream</a>
    <p class="introduce">introduction:
    <a href="http://c.biancheng.net/view/8066.html" id="link5">best</a>
    <a href="http://c.biancheng.net/view/8092.html" id="link6">wishes</a>
    </p>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.select('p ~ a:nth-of-type(4)'))
The above code will print 

`[<a href="http://vip.biancheng.net/?from=index" id="link4">and realize your dream</a>]`

However, if I change 4 into 5, which looks like this:

    print(soup.select('p ~ a:nth-of-type(5)'))

The return value will be [], which means None. But I have no idea how it comes. Could you tell me what happened?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[9769953](https://stackoverflow.com/users/9769953)** (2023-01-02): The last two anchors are inside a paragraph element, and thus there is no fifth anchor directly at the same level as the first paragraph element. (Note how the line `<p class="introduce">introduction:` is only closed by `</p>` three lines below it.)

---
title: "Remove unicode HTML tags in Python"
site: stackoverflow
question_id: 74244208
answer_id: 74244584
url: https://stackoverflow.com/a/74244584
author: "Vishnukk"
author_url: https://stackoverflow.com/users/3152686
posted: 2022-10-29T10:39:21Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: efce6b7dc6de4143a59a17bd5c1752c96c552ea519fbc6439ec3c7de00d2f7ba
role: another answer on the same question, kept as context; not my work
---

# Answer by [Vishnukk](https://stackoverflow.com/users/3152686) — 2022-10-29

Posted on Stack Overflow, <https://stackoverflow.com/a/74244584>, 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This should do!

    content = "overview":"\u003cp style=\"margin: 0px 0px 20px; padding: 0px; line-height: 20px; outline: none !important; min-height: 1em; color: #333333; font-family: Arial, Helvetica, sans-serif, emoji; font-size: 14px; font-style: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: auto; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; text-align: center;\"\u003e\u003cspan style=\"font-family: arial, helvetica, sans-serif;\"\u003e\u003cstrong\u003e\u003cspan style=\"font-size: 18pt; outline: none !important;\"\u003eWTS/VDI macOS\u003c/span\u003e\u003c/strong\u003e\u003c/span\u003e\u003c/p\u003e\n\u003chr\u003e\n\u003cp\u003e\u003cspan ......
    
    soup = BeautifulSoup(content.encode('utf-8').decode('unicode-escape'))
    for tag in soup():
     for attribute in ["class", "id", "name", "style"]:
       del tag[attribute]
        
    new_s = os.linesep.join([s for s in soup.text.splitlines() if s])
    print(new_s)

This will give me

> "overview":"WTS/VDI (Citrix) - macOS WTS (Windows Terminal Services)
> and VDI (Virtual Desktop Instance) provide you....

without the HTML Tags!

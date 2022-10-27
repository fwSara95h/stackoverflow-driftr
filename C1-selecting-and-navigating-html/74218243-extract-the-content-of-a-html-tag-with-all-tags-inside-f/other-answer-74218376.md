---
title: "extract the content of a html tag with all tags inside from beautifulsoup"
site: stackoverflow
question_id: 74218243
answer_id: 74218376
url: https://stackoverflow.com/a/74218376
author: "Daweo"
author_url: https://stackoverflow.com/users/10785975
posted: 2022-10-27T07:36:25Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cca2c8fb3fee4c4ba51c9b62b245f20745e085a008e5c826cf51878be7a92249
role: another answer on the same question, kept as context; not my work
---

# Answer by [Daweo](https://stackoverflow.com/users/10785975) — 2022-10-27

Posted on Stack Overflow, <https://stackoverflow.com/a/74218376>, 2022-10-27; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You might use `decode_contents` as follows

    from bs4 import BeautifulSoup
    html_text = "<TD WIDTH=60%>Portsmouth - Cherbourg<BR/>Portsmouth - Santander<BR/></TD>"
    soup = BeautifulSoup(html_text, 'html.parser')
    soup_list = soup.find_all("td")
    soup_object = soup_list[0]
    inner_html = soup_object.decode_contents()
    print(inner_html)

output

    Portsmouth - Cherbourg<br/>Portsmouth - Santander<br/>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-28): I didn't know about `.decode_contents()` before - that's pretty cool!

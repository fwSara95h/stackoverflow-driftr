---
title: "Remove tag containing a certain text"
site: stackoverflow
question_id: 76545651
answer_id: 76545710
url: https://stackoverflow.com/a/76545710
author: "HedgeHog"
author_url: https://stackoverflow.com/users/14460824
posted: 2023-06-24T10:53:46Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d4f009cf3b90835cebfd2899bd712ad92f63efca6f8e4d3e5686728f1d7005b8
role: another answer on the same question, kept as context; not my work
---

# Answer by [HedgeHog](https://stackoverflow.com/users/14460824) — 2023-06-24

Posted on Stack Overflow, <https://stackoverflow.com/a/76545710>, 2023-06-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could use pseudo class `:-soup-contains("Read our full")`

##### Example

    from bs4 import BeautifulSoup
    html = '''
    <p>
        <strong>
            Read our full
            <a href="">
                review
            </a>
        </strong>
    </p>
    '''
    soup = BeautifulSoup(html)
    
    for e in soup.select('p:-soup-contains("Read our full")'):
        e.decompose()
    
    soup

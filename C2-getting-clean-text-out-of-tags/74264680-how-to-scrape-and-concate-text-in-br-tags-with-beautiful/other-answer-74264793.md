---
title: "How to scrape and concate text in <br> tags with Beautiful Soup"
site: stackoverflow
question_id: 74264680
answer_id: 74264793
url: https://stackoverflow.com/a/74264793
author: "Joel Ambu"
author_url: https://stackoverflow.com/users/12907353
posted: 2022-10-31T14:25:44Z
last_edited: 2022-10-31T22:23:54Z
last_editor: "Maciej Gol"
last_editor_url: https://stackoverflow.com/users/1338158
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 395fb35a9b6c84e92e37ebd405c47515409b5221b7814b84a28bd93b19a16aed
role: another answer on the same question, kept as context; not my work
---

# Answer by [Joel Ambu](https://stackoverflow.com/users/12907353) — 2022-10-31

Posted on Stack Overflow, <https://stackoverflow.com/a/74264793>, 2022-10-31, last edited 2022-10-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Your code doesn't return any results, because the `<br>` does not contain any tags. In fact, the tag does not support ending tags and can only be closed at opening: `<br/>`. See https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br

You might want to use the `get_text` method: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text

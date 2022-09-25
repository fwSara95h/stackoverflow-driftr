---
title: "How can I change the style of all <mark>snippets</mark> within html using javascript?"
site: stackoverflow
question_id: 73848065
url: https://stackoverflow.com/q/73848065
asked: 2022-09-25T21:52:02Z
asked_by: "Sir Hackalot"
asked_by_url: https://stackoverflow.com/users/2380687
last_edited: never
tags: [javascript, html, css]
score: 0
views_at_snapshot: 613
answer_count: 4
accepted_answer_id: 73848324
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 06a1e4ef0ba55ac8775e336e1282bfd32eb31fcad7015c6bfc8b3af42836aba5
---

# How can I change the style of all <mark>snippets</mark> within html using javascript?

Asked by [Sir Hackalot](https://stackoverflow.com/users/2380687) on Stack Overflow, <https://stackoverflow.com/q/73848065>, 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a static html file containing mostly text. Lots of text snippets are highlighted using the `<mark>` tag. I would like to add a button that toggles the text weight of the marked text snippets between bold and normal. The intended effect is to switch on / off the highlighting.

Is there any magic way to do it by directly changing the style of the `mark` css class?

Example:

 - HTML: `... This is an <mark>important text snippet</mark> ...`
 - CSS class BEFORE I hit the button: `mark { text-weight: bold; }`
 - CSS class AFTER I hit the button: `mark { text-weight: normal; }`
 
The reason why I want to do this is to allow the user to decide, if he wants to see highlighted text or not. I know I can change the style of each marked text snippet, but I am wondering, if there is a more direct way.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sir Hackalot](https://stackoverflow.com/users/2380687)** (2022-09-26): Thanks for your answers below! Unfortunately I can only accept one, though all were very helpful in understanding the available options. Thanks!

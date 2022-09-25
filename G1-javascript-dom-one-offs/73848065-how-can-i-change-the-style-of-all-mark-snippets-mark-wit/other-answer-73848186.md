---
title: "How can I change the style of all <mark>snippets</mark> within html using javascript?"
site: stackoverflow
question_id: 73848065
answer_id: 73848186
url: https://stackoverflow.com/a/73848186
author: "ORGPEV"
author_url: https://stackoverflow.com/users/20085325
posted: 2022-09-25T22:19:05Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca04a6e9a0e0664d5b1eb299ce644d60874ed239074b4b2f847d8a1c3e92b056
role: another answer on the same question, kept as context; not my work
---

# Answer by [ORGPEV](https://stackoverflow.com/users/20085325) — 2022-09-25

Posted on Stack Overflow, <https://stackoverflow.com/a/73848186>, 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

What about something like this?

    <html>
        <head>
            <style>
                mark {
                    font-weight: bold;
                    background: none;
                }
            </style>
        </head>
    <body>
    
    This is an <mark>important text snippet</mark> and so <mark>is this</mark>.
    
    <button onclick = "changeMark()">Change Mark Style</button>
    
    <script>
        function changeMark() {
            document.querySelectorAll("mark").forEach(e => e.style.fontWeight = "normal");
        }
    </script>
    
    </body>
    </html>

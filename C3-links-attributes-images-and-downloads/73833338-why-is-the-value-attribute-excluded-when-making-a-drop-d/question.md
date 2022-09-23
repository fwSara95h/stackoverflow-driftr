---
title: "Why is the value attribute excluded when making a drop-down menu's answer tag?"
site: stackoverflow
question_id: 73833338
url: https://stackoverflow.com/q/73833338
asked: 2022-09-23T21:56:30Z
asked_by: "ConfusedinNorway"
asked_by_url: https://stackoverflow.com/users/20073510
last_edited: never
tags: [html, forms]
score: 0
views_at_snapshot: 22
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 42144632392a36f770f43969ceddcb28a62eda37d8c3070204d5d3a3ea79f7af
---

# Why is the value attribute excluded when making a drop-down menu's answer tag?

Asked by [ConfusedinNorway](https://stackoverflow.com/users/20073510) on Stack Overflow, <https://stackoverflow.com/q/73833338>, 2022-09-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm learning web development for fun.

Now I am making a drop-down menu that asks security questions. I learned how to create one from a tutorial online. What I'm still confused about is why the value attribute is excluded for the answer's input tag. I thought it would be needed to send the answer to the server? Does the name attribute allow the answer to be sent?

My code is below.

Thanks in advance!

        <label for="question">Security question</label>
        <select name="question" id="question">
            <option value="q1">What is your favorite Pokemon?</option>
            <option value="q2">What is your favorite book?</option>
            <option value="q3">What is your city of birth?</option>

        </select>

        <br><br>
        <label for="answer">Security question answer:</label>
        <input type="text" id="answer" name="answer">

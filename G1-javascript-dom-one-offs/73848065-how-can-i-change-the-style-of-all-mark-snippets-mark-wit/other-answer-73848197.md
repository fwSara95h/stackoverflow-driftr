---
title: "How can I change the style of all <mark>snippets</mark> within html using javascript?"
site: stackoverflow
question_id: 73848065
answer_id: 73848197
url: https://stackoverflow.com/a/73848197
author: "ivy"
author_url: https://stackoverflow.com/users/9627251
posted: 2022-09-25T22:22:08Z
last_edited: never
accepted: false
score: 3
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 397e0f21cfcfb8eac73100851d8c09e92da9005d8af6169dd83888c5d4a4da90
role: another answer on the same question, kept as context; not my work
---

# Answer by [ivy](https://stackoverflow.com/users/9627251) — 2022-09-25

Posted on Stack Overflow, <https://stackoverflow.com/a/73848197>, 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.


## Method 1 - Toggling a Class on a Parent Element
A more direct way would be to add a class to a *parent* element. Then, in CSS, you can select all of the child `mark` elements. This method saves you from iterating over every mark element on your page in JS. You could add this class on a containing `div` or even on the root `html` element if you desire.

`classList.toggle` is supported on all major browsers: https://caniuse.com/?search=classlist.toggle

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->


    function toggleMarkup() {
      document.querySelector("#content").classList.toggle("markup-shown");
    }

<!-- language: lang-css -->


    p.markup-shown mark {
      font-weight: bold;
    }

<!-- language: lang-html -->


    <p id="content">
    Hello! This is some <mark>marked up</mark> text! And this is some more <mark>marked</mark> text.
    </p>

    <button onclick="toggleMarkup()">
    Click me to toggle markup.
    </button>

<!-- end snippet -->

## Method 2 - Using CSSOM

https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model
https://stackoverflow.com/a/55468693/9627251

You can also obtain and modify existing CSS classes directly from JS:

    const rules = document.styleSheets.map(sheet => sheet.cssRules);
    const rule = rules.find(r => r.selectorText == 'mark');
    rule.style.fontWeight = 'bold'; // or normal, in your toggle function logic

Note that you would already have to have a CSS rule like:

    mark { font-weight: normal; }

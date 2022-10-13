---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74051973
url: https://stackoverflow.com/a/74051973
author: "uingtea"
author_url: https://stackoverflow.com/users/4082344
posted: 2022-10-13T07:29:23Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 16f210e65a590892bf2e5b2972889db0dcdea5fa5a99579695551b61e256a1a4
role: another answer on the same question, kept as context; not my work
---

# Answer by [uingtea](https://stackoverflow.com/users/4082344) — 2022-10-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74051973>, 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

to not submit the form, replace the `<button>` with `<input type="button" value="+">` and to create list you want `<li>` element with the parent `<ul>`



<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let addToButton = document.getElementById('addButton');
    let inputFieldset = document.getElementById('toDoInput');
    let toDoContainer = document.getElementById('toDoList');

    addToButton.addEventListener('click', function() {
      // show warning if input empty
      if (!inputFieldset.reportValidity()) // or use: if (!inputFieldset.value)
        return
      let toDoStuff = document.createElement('li')
      toDoStuff.innerHTML = inputFieldset.value
      toDoContainer.append(toDoStuff);
      // reset input
      inputFieldset.value = '';
    })

<!-- language: lang-html -->

    <h3>Input your activities</h3>
    <form>
    Input something <input type="text" required id="toDoInput" placeholder="Input your stuff" />
    <button id="addButton">+</button>
    </form>

    <ul id="toDoList">
    </ul>

<!-- end snippet -->

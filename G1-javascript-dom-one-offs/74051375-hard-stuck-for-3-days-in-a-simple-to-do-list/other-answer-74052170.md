---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74052170
url: https://stackoverflow.com/a/74052170
author: "Adam Carlsson"
author_url: https://stackoverflow.com/users/20169829
posted: 2022-10-13T07:48:07Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 36ffdaffdff65d772f9fa928e39bbb5377a013a6d85cc0f9ba2915c5511cdd3d
role: another answer on the same question, kept as context; not my work
---

# Answer by [Adam Carlsson](https://stackoverflow.com/users/20169829) — 2022-10-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74052170>, 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I changed your code. The problems are 3 in number.
 1. you have button type submit, this submits the form and the form then requires an action to handle the submit, this is typically used to send data to other pages.(dont quote me on that, i never use it)
 2. you made toDoStuff get the value of the input thus overriding the create element.
 3. you had a div as a container for a created ul when you want to have a ul as container for a created li.

Here is the changed html:
```
 <body>
      <main>
          <h1>Ysmael's To-Do List</h1>
          <h3>Input your activities</h3>
          <form>
              Input something<input type="text" required id="toDoInput" placeholder="Input your stuff"/><button id="addButton" type="button">+</button>
          </form>
          <ul id="toDoList">
          </ul>
      </main>
  </body>
```
And here is the changed Javascript:
```
let addToButton = document.getElementById('addButton')
let inputFieldset = document.getElementById('toDoInput')
let toDoContainer = document.getElementById('toDoList')


addToButton.addEventListener('click', () => {
  let toDoStuff = document.createElement('li')
  toDoStuff.innerHTML = inputFieldset.value
  toDoContainer.append(toDoStuff)
})
```

Good luck and happy coding, dont let a setback make you give up!

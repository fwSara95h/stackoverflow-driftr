---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74052058
url: https://stackoverflow.com/a/74052058
author: "Karolis"
author_url: https://stackoverflow.com/users/18782190
posted: 2022-10-13T07:37:11Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bbfacf5e3e0b1225bc948b72d7d999c15badf66e07a72b6f7f2f8be15e438c70
role: another answer on the same question, kept as context; not my work
---

# Answer by [Karolis](https://stackoverflow.com/users/18782190) — 2022-10-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74052058>, 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

1. One of the solutions to prevent reloading the page after submitting the form is to use `even.preventDefault()` on `submit` event. In this way you prevent default browser's behavior. Anyway, to do so, you should add `submit` event listener. You can also add submitted task to the list from there, therefore I replaced your 'click' event handler with `submit`.
2. `<script>` tag shouldn't have `href` attribute. It should be `src` instead.
3. You are creating `<ul>` element which is a container for the list of unordered elements. You should create `<li>` element and append it to `<ul>` or `<ol>` container. I have replaced tasks container from `<div>` to `<ul>`.

`index.html`:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <title>la lista</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="list-style.css" />
</head>

<body>
    <main>
        <h1>Ysmael's To-Do List</h1>
        <h3>Input your activities</h3>
        <form id="toDoForm">
            Input something
            <input type="text" required id="toDoInput" placeholder="Input your stuff" />
            <button id="addButton" type="submit">+</button>
        </form>
        <ul id="toDoList">
        </ul>
    </main>
    <script src="todolist.js"></script>
</body>

</html>
```

`tasklist.js`:

    let inputFieldset = document.getElementById('toDoInput');
    let toDoContainer = document.getElementById('toDoList');
    let toDoForm = document.getElementById('toDoForm');
    
    toDoForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const task = document.createElement('li');
        task.innerText = inputFieldset.value;
        toDoContainer.appendChild(task);
        inputFieldset.value = '';
    })

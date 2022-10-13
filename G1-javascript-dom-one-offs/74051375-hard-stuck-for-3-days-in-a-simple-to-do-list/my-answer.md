---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74052093
url: https://stackoverflow.com/a/74052093
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-13T07:40:29Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74052093/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 19489511391dd5b1dcf145c18ca989ed2ec3f848089e5f50262ef49aee30c411
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74052093>, 2022-10-13; score 0. Text as retrieved 2026-10-12.

Change button type to `button` instead of `submit` to keep everything from disappearing when it's clicked, and change `toDoList` element from `div` to `ul` and then add tasks as `li` [list items] rather than `ul` [a whole unordered list in itself]. Also, you need to change the innerHTML (or innerText) of `toDoStuff` instead of setting the element itself (so that it remains a `li`).

<!-- begin snippet: js hide: false console: true babel: null -->

<!-- language: lang-js -->

    let addToButton = document.getElementById('addButton');
    let inputFieldset = document.getElementById('toDoInput');
    let toDoContainer =  document.getElementById('toDoList');

    addToButton.addEventListener('click', function(){
        let toDoStuff = document.createElement('li');
        toDoStuff.innerHTML = inputFieldset.value;
        toDoContainer.append(toDoStuff);
        inputFieldset.value = "";//clear field
    })

    //so that "enter" does the same as addToButton instead of submit
    inputFieldset.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            addToButton.click();
        }
    });

<!-- language: lang-html -->

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>la lista</title>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            <link rel="stylesheet" href="list-style.css"/>
            
        </head>
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
            <script href="todolist.js"></script>
        </body>
    </html>

<!-- end snippet -->




I've also added a line to clear the field [for the next task] after a task has been added, and another event listener to the text input because "enter" key can also register as submit - but now, instead of everything disappearing on enter, it simulates clicking the add button.

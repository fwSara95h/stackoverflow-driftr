---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
url: https://stackoverflow.com/q/74051375
asked: 2022-10-13T06:35:06Z
asked_by: "Ysmael"
asked_by_url: https://stackoverflow.com/users/20228511
last_edited: 2022-10-13T06:38:25Z
last_editor: "DarkBee"
last_editor_url: https://stackoverflow.com/users/446594
tags: [javascript, dom, project]
score: 0
views_at_snapshot: 1092
answer_count: 6
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cc5dd3d8dca6fb2c77988e16d66b52759ae44fca43f7b237e6d91893492edf90
---

# Hard stuck for 3 days in a simple to do list

Asked by [Ysmael](https://stackoverflow.com/users/20228511) on Stack Overflow, <https://stackoverflow.com/q/74051375>, 2022-10-13, last edited 2022-10-13 by [DarkBee](https://stackoverflow.com/users/446594). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

after months of doing courses, I finally ventured into coding my first project, but the most basic functionality of it isn't working.

I'm doing a simple to do list, and im working on it actually displaying the elements added by the user through the button but they don't appear on the screen after clicking, even if i'm using DOM manipulation commands to create an 'ul' element. Also, the page refreshes after every click on the button.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let addToButton = document.getElementById('addButton');
    let inputFieldset = document.getElementById('toDoInput');
    let toDoContainer =  document.getElementById('toDoList');

    addToButton.addEventListener('click', function(){
        let toDoStuff = document.createElement('ul')
        toDoStuff = inputFieldset.value
        toDoContainer.append(toDoStuff);
    })

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
                    Input something<input type="text" required id="toDoInput" placeholder="Input your stuff"/><button id="addButton" type="submit">+</button>
                </form>
                <div id="toDoList">
                </div>
            </main>
            <script href="todolist.js"></script>
        </body>
    </html>



<!-- end snippet -->

Acording to my logic, it should work, but I'm clearly doing one or more things wrong.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Teemu](https://stackoverflow.com/users/1169519)** (2022-10-13): Plain text is not permitted content in [`ul`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul) element, you've to create `li` element and append the text to that element and then append `li` to `ul`.
- **[DarkBee](https://stackoverflow.com/users/446594)** (2022-10-13): Use the `type="button"` if you don't want to submit the form

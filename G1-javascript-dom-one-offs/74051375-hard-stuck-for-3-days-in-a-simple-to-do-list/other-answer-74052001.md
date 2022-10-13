---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74052001
url: https://stackoverflow.com/a/74052001
author: "Davi"
author_url: https://stackoverflow.com/users/9870107
posted: 2022-10-13T07:31:44Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 62dd76f6f4497c868d6663f71d3cdfbe90829d41e23c7614173577da6d8ef65d
role: another answer on the same question, kept as context; not my work
---

# Answer by [Davi](https://stackoverflow.com/users/9870107) — 2022-10-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74052001>, 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

For problem #1:

In line 6 you are creating the let binding `toDoStuff` which holds a `<ul>`-element, just to override `toDoStuff` in line 7 with the current value of the `<input>`-element. Even if it worked (somehow), I suspect it wouldn't work as you expect, because it would create a completely new list for each todo instead of creating a single list of todos. If I'm right, move the `let toDoStuff = document.createElement('ul')` line out of your event handler function, create the `<ul>` right away and `.append()` it to your `toDoContainer` (hold a reference to it so that you can append elements to it later).

     let toDoContainer =  document.getElementById('toDoList');
     let toDoStuff = document.createElement('ul');
     toDoContainer.append(toDoStuff);

Then, inside the click handler function, create an `<li>` element that you can append to the `<ul>`:

     addToButton.addEventListener('click', function () {
       let toDoListItem = document.createElement('li');
       // ... elided
     });

The `.append()` method of an `HTMLElement` expects to receive another `HTMLElement` or `Node`, but you are passing it a `String`. This means you need to transform that `String` into a `Node` before passing it to `.append()`, and the usual way to do that transformation is via `document.createTextNode()`. 

    let toDoText = document.createTextNode(inputFieldset.value)

However, you want to insert that `Node` into a `<ul>` element and the only child elements of an unordered list should be `<li>`-elements. This is why we generated the `<li>` in the previous sections, so all you have to do now is adding the `Node` to the `<li>`, then adding the `<li>` to the `<ul>`. In code:

    addToButton.addEventListener('click', function () {
      let toDoListItem = document.createElement('li');
      let toDoText = document.createTextNode(inputFieldset.value);
      toDoListItem.append(toDoText);
      toDoStuff.append(toDoListItem);
    });

In regards to the #2 submission problem:

Your button is nested inside a `<form>` element, so pressing it "naturally" submits the form. What you want to do is to suppress the submission, either via:

- calling `.preventDefault()` on the generated `SubmitEvent` object of the _form_
- returning `false` in your event handler function

In favor of a standards way, use `.preventDefault()`, so we need a reference to the `<form>` element instead of the `<button>` as well as changing the event type from `'click'` to `'submit'`:

    // ... elided
    let addToButton = document.querySelector('form');
    // ... elided
    addToButton.addEventListener('submit', function (event) { // <-- changed click to submit, added generated event object
      event.preventDefault(); // <-- suppress form submission
      let toDoListItem = document.createElement('li');
      // ... elided, see above
    });

Changing the variable names to appropriate ones is left as an excercise ;-)

Example:

<!-- begin snippet: js hide: false console: true babel: null -->

<!-- language: lang-js -->

    let addToButton = document.querySelector('form');
    let inputFieldset = document.getElementById('toDoInput');
    let toDoContainer =  document.getElementById('toDoList');
    let toDoStuff = document.createElement('ul');
    toDoContainer.append(toDoStuff);

    addToButton.addEventListener('submit', function (event) {
        event.preventDefault();
        let toDoListItem = document.createElement('li');
        let toDoText = document.createTextNode(inputFieldset.value);
        toDoListItem.append(toDoText);
        toDoStuff.append(toDoListItem);
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

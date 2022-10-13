---
title: "Hard stuck for 3 days in a simple to do list"
site: stackoverflow
question_id: 74051375
answer_id: 74052565
url: https://stackoverflow.com/a/74052565
author: "zer00ne"
author_url: https://stackoverflow.com/users/2813224
posted: 2022-10-13T08:20:31Z
last_edited: 2022-10-13T08:26:23Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 07aef6ae488d4fa5789cc12b82935835b50a3dd39d78001ba2741562293b2f29
role: another answer on the same question, kept as context; not my work
---

# Answer by [zer00ne](https://stackoverflow.com/users/2813224) — 2022-10-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74052565>, 2022-10-13, last edited 2022-10-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.



Bind the `<form>` to the "submit" event. Details are commented in example.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    // Reference <form>
    const todo = document.forms.todo;
    // Reference <input>
    const add = todo.elements.add;
    // Reference <ul>
    const list = document.querySelector(".list");

    /**
     * Bind <form> to "submit" event
     * Stop <form> from sending data and blanking out the page
     * Create <li> which is required in a <ul>
     * Add the value of <input> as the text of <li>
     * Add <li> to <ul>
     * Clear the <form> to prevent accidental clicking
     */
    todo.addEventListener('submit', function(event) {
      event.preventDefault();
      const item = document.createElement('li')
      item.textContent = add.value
      list.append(item);
      this.reset();
    });

<!-- language: lang-html -->

    <main>
      <!-- Add #id or [name] to <form> -->
      <form id="todo">
        <fieldset>
          <legend>Ysmael's To-Do List</legend>
          <!-- Add <label> and [for="{<input> #id}"] -->
          <label for="add">Enter Task: </label>
          <input id="add" type="text" required>
          <!-- A plain <button> inside a <form> will trigger "submit" -->
          <button>+</button>
        </fieldset>
      </form>
      <ul class="list"></ul>
    </main>

<!-- end snippet -->

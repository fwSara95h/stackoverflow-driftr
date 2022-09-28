---
title: "select element that is created by insertAdjacentHTML for adding or remove class"
site: stackoverflow
question_id: 73873818
answer_id: 73875442
url: https://stackoverflow.com/a/73875442
author: "zer00ne"
author_url: https://stackoverflow.com/users/2813224
posted: 2022-09-28T01:59:49Z
last_edited: 2022-09-28T02:05:49Z
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 68a902a472064d3e82104717790f2a06573bb8b880a7c01f6358fa28138d3e5a
role: another answer on the same question, kept as context; not my work
---

# Answer by [zer00ne](https://stackoverflow.com/users/2813224) — 2022-09-28

Posted on Stack Overflow, <https://stackoverflow.com/a/73875442>, 2022-09-28, last edited 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

First off, do not use inline event handlers (see https://stackoverflow.com/q/11737873/2813224). Secondly, if you are dynamically adding buttons that trigger an event handler (a function that runs when an event is triggered like a "click" event), use [event delegation][1] by registering events to a common ancestor element. 

In the example below, only the elements are generated and added to the DOM -- there is no event binding. A `<form>` is wrapped around the `<ol>` so that the succinct syntax of the [HTMLFormElement][2] interface can be used should it be needed (in this example it's used once ie `const main = document.forms[0]`, but it can do a lot more with less code). See [event handling][3] for details as well.

**Details are commented in example**
<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const todo = [{
      title: "First task",
      status: "pending"
    }, {
      title: "Second task",
      status: "pending"
    }, {
      title: "Third task",
      status: "complete"
    }, {
      title: "Fourth task",
      status: "pending"
    }, {
      title: "Fifth task",
      status: "complete"
    }];

    /**
     * Generates a list from a given array of objects
     *  1. Adds a <ol> within a <form>
     *  2. Adds an <li> to <ol> for each object in >list<
     *  3. Within each <li> is an <output> and 2 <button>s
     *  4. Each object's "title" is the text of <output>
     *  5. Each object's "status" is the className of <li>
     * @param {array<object>} list - Each object is the following by default:
     *        {title: "TBA", status: "pending"}
     * @param {string||object} node - If it's a string then it's a selector of an element. Otherwise it's a
     *        DOM object. If undefined it is a @defualt of a selector called "body"
     */
    function genList(list, node = "body") {
      let root = typeof node === "string" ? document.querySelector(node) : node;
      const form = document.createElement('form');
      const ol = document.createElement('ol');
      root.append(form);
      form.append(ol);

      list.forEach((item, index) => {
        ol.insertAdjacentHTML('beforeend', `<li class="${item.status}"><output name="title">${item.title}</output> <button name="complete" class="btn btn-success" type="button"></button><button name="delete" class="btn btn-danger" type="button">Delete</button></li>`);
      });
    }

    // Call genList pass the >todo< array and do not define second @param so it'll just add to <body>
    genList(todo);
    // Reference the <form>
    const main = document.forms[0];
    // Register the click event to <form> -- call action(event) when click event is triggered on <form>
    main.onclick = action;

    // Event handler passes Event object by default
    function action(event) {
      // Reference the element the user clicked
      const clk = event.target;
      /*
      If the user clicked an element with [name="complete"]...
      ...toggle the classNames "complete" and "pending" on it's parent element
      In other words: if <button name="complete"...> was clicked...
      ...reverse the className of the containing <li> from/to "complete"/"pending"
      */
      if (clk.name === "complete") {
        clk.parentElement.classList.toggle("complete");
        clk.parentElement.classList.toggle("pending");
        return;
      }
      /*
      If the user clicked an element with [name="delete"]...
      ...find it's parent element and remove it
      */
      if (clk.name === "delete") {
        return clk.parentElement.remove();
      }
    }

<!-- language: lang-css -->

    output {
      display: inline-block;
      width: 25ch;
    }

    button {
      display: inline-block;
      width: 12ch;
    }

    .complete output {
      text-decoration: line-through red;
    }

    .complete .btn-success::before {
      content: "Completed";
    }

    .pending .btn-success::before {
      content: "Complete";
    }

<!-- end snippet -->


  [1]: https://javascript.info/event-delegation
  [2]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement
  [3]: https://developer.mozilla.org/en-US/docs/Web/Events/Event_handlers

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[joyi61](https://stackoverflow.com/users/19601673)** (2022-09-28): Omg i realy liked your answer it is perfect , and i think it's upper than my level but i will try it to learn more , thank you sooo much dear ** zer00ne**

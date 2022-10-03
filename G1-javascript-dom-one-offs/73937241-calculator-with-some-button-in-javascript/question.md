---
title: "Calculator with some Button in JavaScript"
site: stackoverflow
question_id: 73937241
url: https://stackoverflow.com/q/73937241
asked: 2022-10-03T14:54:38Z
asked_by: "BeniGR"
asked_by_url: https://stackoverflow.com/users/20150768
last_edited: 2022-10-03T15:10:04Z
last_editor: "Mister Jojo"
last_editor_url: https://stackoverflow.com/users/10669010
tags: [javascript]
score: 0
views_at_snapshot: 1301
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6cb09e4ddf5a8fd4f72854e770f3f70ab2a193f1565818afd3f238caeb784a2e
---

# Calculator with some Button in JavaScript

Asked by [BeniGR](https://stackoverflow.com/users/20150768) on Stack Overflow, <https://stackoverflow.com/q/73937241>, 2022-10-03, last edited 2022-10-03 by [Mister Jojo](https://stackoverflow.com/users/10669010). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to make a Calculator in JS. I'm new to JS and I don't get it why it isn't working. In the Browser Console I get undefined if I call add().  
getInputAsNumber(...) should retrieves the input value from the field with the ID passed as Parameter
writeResult() writes the calculated result to the output field and is used in all operations



<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    "use strict";

    function add() {
      let operator1;
      let operator2;
      getInputAsNumber(operator1, operator2);
      let summe = operator1 + operator2;
      writeResult(summe);
    }

    function getInputAsNumber(op1, op2) {

      op1 = document.getElementById("op1").value;
      op2 = document.getElementById("op2").value;
    }

    function writeResult(result) {
      let outputElement = document.getElementById("output1");
      outputElement.innerHTML = Number.result;
    }

<!-- language: lang-html -->

    <form>
      <h1>Calculator with Buttons</h1>
      <label>Operand 1:</label>
      <input id="op1" type="number">
      <br>
      <br>
      <label>Operand 2:</label>
      <input id="op2" type="number">
      <br>
      <br>
      <label>Operators: </label>
      <button>+</button>
      <button>-</button>
      <button>*</button>
      <button>/</button>
      <br>
      <br>
      <div id="result">
        <label>Result: </label>
        <output id="output1"></output>
      </div>

    </form>

<!-- end snippet -->

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jay Buckman](https://stackoverflow.com/users/2292368)** (2022-10-03): Look at https://stackoverflow.com/questions/518000/is-javascript-a-pass-by-reference-or-pass-by-value-language - your code is assuming that op1 and op2 are passed by reference...
- **[Mister Jojo](https://stackoverflow.com/users/10669010)** (2022-10-03): fist you are using a `<form>` and `<button>` elements. any click or enter key on form element will submit the form, as your form doesn't use any action value, this will cause a page reload.

---
title: "Calculator with some Button in JavaScript"
site: stackoverflow
question_id: 73937241
answer_id: 73937510
url: https://stackoverflow.com/a/73937510
author: "Fatorice"
author_url: https://stackoverflow.com/users/4613465
posted: 2022-10-03T15:19:10Z
last_edited: 2022-10-03T15:25:24Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0bec61140158c0706dac26b102bbdbd2239206cb96428b4e33294c687db5bd43
role: another answer on the same question, kept as context; not my work
---

# Answer by [Fatorice](https://stackoverflow.com/users/4613465) — 2022-10-03

Posted on Stack Overflow, <https://stackoverflow.com/a/73937510>, 2022-10-03, last edited 2022-10-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You are passing op1 and op2 as a referenced parameter, but they are actually called by value (which means, that they aren't changed when changing inside of the function). You get undefined because operator1 and operator2 are only **declared** (not initialized!).

You can modify your function so that it returns both operators (instead of passing them):

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function add() {
      let {operator1, operator2} = getInputAsNumber();
      let summe = operator1 + operator2;
      writeResult(summe);
    }

    function getInputAsNumber() {
      const op1 = document.getElementById("op1").value;
      const op2 = document.getElementById("op2").value;
      return {operator1: parseFloat(op1), operator2: parseFloat(op2)};
    }

    function writeResult(result) {
      let outputElement = document.getElementById("output1");
      outputElement.innerHTML = result;
    }

<!-- language: lang-html -->


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
    <button onClick="add()">+</button>
    <button>-</button>
    <button>*</button>
    <button>/</button>
    <br>
    <br>
    <div id="result">
      <label>Result: </label>
      <output id="output1"></output>
    </div>


<!-- end snippet -->

This function returns an object consisting of operator1 and 2 and using the object unwrapping (left side of the getInputAsNumber call) you can easily fetch the two values.
Additionally: just reading the values of the input field (.value) retrieves a string (!), adding two strings in JavaScript means concatination ("2" + "2" = "22"), so you need to parse them first.

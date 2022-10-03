---
title: "Calculator with some Button in JavaScript"
site: stackoverflow
question_id: 73937241
answer_id: 73938066
url: https://stackoverflow.com/a/73938066
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-03T16:09:40Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73938066/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: db1e6919411cf9864f822f18ed34088ffeee43dd99e8bf45e19e61c5025f53ea
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73938066>, 2022-10-03; score 0. Text as retrieved 2026-10-12.

The main issues I can see with your code is that:

 - you need to either pass `op1` and `op2` more directly, or [as below] set them globally so that they don't need to be passed at all
 - you can just use `result`, not `Number.result` [why the `Number.` in the first place?] 
 - you might need to parse the inputs from string to number using `parseInt`
Then, if you add `onclick` attributes to your buttons or use enventListener, you can make the calculator work fully

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    "use strict";

    var operator1;
    var operator2;

    function calcOp(operator) {
      getInputAsNumber();
      var op;
      if (operator == 'add') {
        writeResult(operator1 + operator2);
      } else if (operator == 'sub') {
        writeResult(operator1 - operator2);
      } else if (operator == 'mul') {
        writeResult(operator1 * operator2);
      } else if (operator == 'div') {
        writeResult(operator1 / operator2);
      }
    }

    function getInputAsNumber() {
      operator1 = parseInt(document.getElementById("op1").value);
      operator2 = parseInt(document.getElementById("op2").value);
    }

    function writeResult(result) {
      let outputElement = document.getElementById("output1x");
      outputElement.value = result;
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
    <button onclick="calcOp('add');">+</button>
    <button onclick="calcOp('sub');">-</button>
    <button onclick="calcOp('mul');">*</button>
    <button onclick="calcOp('div');">/</button>
    <br>
    <br>
    <div id="result"><label>Result: </label><output id="output1x"></output></div>

<!-- end snippet -->

I changed your `add` function to `calcOp` because all the operations would have very similar, but if you just wanted to have `add` :
    

    function add() {
        getInputAsNumber();
        let summe = operator1 + operator2;
        writeResult(summe);
    }
[Also, as one of the comments mentioned, if you wrap it as a `form` the way you did, it will likely disappear after any operation. Just `div` will look the same and not disappear]

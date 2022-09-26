---
title: "My Function will not inject text into my HTML"
site: stackoverflow
question_id: 73856960
url: https://stackoverflow.com/q/73856960
asked: 2022-09-26T16:10:50Z
asked_by: "Tyler Ernesto"
asked_by_url: https://stackoverflow.com/users/20092065
last_edited: 2022-09-26T16:16:36Z
last_editor: "ScandinavianAvian"
last_editor_url: https://stackoverflow.com/users/295783
tags: [javascript, html]
score: 1
views_at_snapshot: 72
answer_count: 4
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 36060aae0e438137b364f4f46f6336f3e308a2f3aa8267bc30d4988bd9463f0b
---

# My Function will not inject text into my HTML

Asked by [Tyler Ernesto](https://stackoverflow.com/users/20092065) on Stack Overflow, <https://stackoverflow.com/q/73856960>, 2022-09-26, last edited 2022-09-26 by [ScandinavianAvian](https://stackoverflow.com/users/295783). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am creating a quiz for my web site and I would like for my function to be able to inject text into my HTML. It has worked for every other function but this one does not work. I have tried to change my injection method. I have also tried to use a JQuery method to inject my text but it still wont let me.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function quiz() {
      var f = 0;
      alert(f);
      if (document.getElementById("answer1").checked == true) {
        f++;
      };
      if (document.getElementById("answer2").checked == true) {
        f++;
      };
      if (document.getElementById("answer3").checked == true) {
        f++;
      };
      if (document.getElementById("answer4").checked == true) {
        f++;
      };

      function checkpass() {
        var a = ""
        if (f == 4) {
          a = "Y"
          alert(a)
        } else {
          a = "N"
          alert(a)
        };
      };
      checkpass();
      alert(document.getElementById("score"))
      document.getElementById("score").innerHTML = `Score:${f}/4 ${a}`;
    };

<!-- language: lang-html -->

    <div id="WebBody">
      <P>Answer True or False on qustions</P>
      <p>Is ___</p>
      <form>
        <input class="Radio-Button" id="answer1" name="T/F" type="radio">   <label>True</label><br>   <input class="Radio-Button" name="T/F" type="radio">   <label>False</label>
      </form>
      <hr>
      <p>Is ___</p>
      <form>
        <input class="Radio-Button" id="answer2" name="T/F" type="radio">   <label>True</label><br>   <input class="Radio-Button" name="T/F" type="radio">   <label>False</label>
      </form>
      <hr>
      <p>Is ___</p>
      <form>
        <input class="Radio-Button" id="answer3" name="T/F" type="radio">   <label>True</label><br>   <input class="Radio-Button" name="T/F" type="radio">   <label>False</label>
      </form>
      <hr>
      <p>Is ___</p>
      <form>
        <input class="Radio-Button" id="answer4" name="T/F" type="radio">   <label>True</label><br>   <input class="Radio-Button" name="T/F" type="radio">   <label>False</label>
      </form>
      <hr>
      <button onclick="quiz()">Submit</button>
      <p id="score">Score:Not Submitted</p>
    </div>

<!-- end snippet -->

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Felix Kling](https://stackoverflow.com/users/218196)** (2022-09-26): Have you looked for errors in your browser's console? Does any of the `alert`s show up?
- **[GrafiCode](https://stackoverflow.com/users/5334486)** (2022-09-26): variable `a` is not accessible from outside the `checkpass` function.
- **[Kinglish](https://stackoverflow.com/users/1772933)** (2022-09-26): Use your inspector - its telling you exactly the error: `"message": "Uncaught ReferenceError: a is not defined"`
- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-09-26): `f` is not in scope in the second function and neither `a` nor `f` are available to your last statement. Move them outside your functions

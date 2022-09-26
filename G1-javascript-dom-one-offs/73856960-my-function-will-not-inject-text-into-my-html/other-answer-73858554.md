---
title: "My Function will not inject text into my HTML"
site: stackoverflow
question_id: 73856960
answer_id: 73858554
url: https://stackoverflow.com/a/73858554
author: "ScandinavianAvian"
author_url: https://stackoverflow.com/users/295783
posted: 2022-09-26T18:39:47Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ce19ea7a7ec64588cd488fc47849527bd3c0a24ecc00c57cf5736d8031e377ce
role: another answer on the same question, kept as context; not my work
---

# Answer by [ScandinavianAvian](https://stackoverflow.com/users/295783) — 2022-09-26

Posted on Stack Overflow, <https://stackoverflow.com/a/73858554>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

So the other answers explained what was wrong

Here is a version using recommended eventListener and a more elegant way of counting.
Also the HTML is simpler and if you want to submit the form, you will get the correct names

Note this quiz does not know or care how many questions there are


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const correct = ["answer1", "answer2", "answer3", "answer4"];
    document.getElementById("quizForm").addEventListener("submit", e => {
      e.preventDefault(); // stop submit
      const f = [...document.querySelectorAll(".Radio-Button:checked")]
        .filter(rad => correct.includes(rad.id)).length; // count correct answers
      const a = f === correct.length ? "Y" : "N";
      document.getElementById("score").innerHTML = `Score:${f}/${correct.length} ${a}`;
    });

<!-- language: lang-html -->

    <form id="quizForm">
      <div id="WebBody">
        <P>Answer True or False on questions</P>
        <p>Is ___</p>
        <label><input class="Radio-Button" id="answer1" name="T/F1" type="radio">True</label><br>
        <label><input class="Radio-Button" name="T/F1" type="radio">False</label>
        <hr>
        <p>Is ___</p>
        <label><input class="Radio-Button" id="answer2" name="T/F2" type="radio">True</label><br>
        <label><input class="Radio-Button" name="T/F2" type="radio">False</label>
        <hr>
        <p>Is ___</p>
        <label><input class="Radio-Button" id="answer3" name="T/F3" type="radio">True</label><br>
        <label><input class="Radio-Button" name="T/F3" type="radio">False</label>
        <hr>
        <p>Is ___</p>
        <label><input class="Radio-Button" id="answer4" name="T/F4" type="radio">True</label><br>
        <label><input class="Radio-Button" name="T/F4" type="radio">False</label>
        <hr>
        <button>Submit</button>
        <p id="score">Score:Not Submitted</p>
      </div>
    </form>

<!-- end snippet -->

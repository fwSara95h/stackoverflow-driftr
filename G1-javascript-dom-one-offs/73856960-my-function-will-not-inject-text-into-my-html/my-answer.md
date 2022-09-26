---
title: "My Function will not inject text into my HTML"
site: stackoverflow
question_id: 73856960
answer_id: 73857154
url: https://stackoverflow.com/a/73857154
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-26T16:28:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73857154/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1bf78ac5e4b39b921d8305e01311e543ac8bfc542065b7a7b2e83da525652ef3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73857154>, 2022-09-26; score 0. Text as retrieved 2026-10-12.


You just have to move the definition of `a` to outside `checkpass` or return it because it's needed in the last line (which is outside `checkpass`). (I'm showing the latter because another answer already shows the first). You might want to look into [the js debugger in devtools][1], because this kind of slips are not unusual, but easy to catch with debugger.

(Also I changed your "score" element alert because alerts are not like console.log - full, expandable objects will not be displayed, just string.)


<!-- begin snippet: js hide: false console: true babel: null -->

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
        var a = "";
        if (f == 4) {
          a = "Y"
          alert(a)
        } else {
          a = "N"
          alert(a)
        };
        return a;
      };
      var a = checkpass();
      alert(document.getElementById("score").outerHTML)
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


  [1]: https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools#the_javascript_debugger

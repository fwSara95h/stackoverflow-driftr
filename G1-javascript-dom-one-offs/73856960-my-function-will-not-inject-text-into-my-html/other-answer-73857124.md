---
title: "My Function will not inject text into my HTML"
site: stackoverflow
question_id: 73856960
answer_id: 73857124
url: https://stackoverflow.com/a/73857124
author: "Zimon Huh"
author_url: https://stackoverflow.com/users/1833021
posted: 2022-09-26T16:25:28Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d21225db9f5a5784aebfed61d7ebc4e59df8004ea3bf55f70144c21bcf7706cb
role: another answer on the same question, kept as context; not my work
---

# Answer by [Zimon Huh](https://stackoverflow.com/users/1833021) — 2022-09-26

Posted on Stack Overflow, <https://stackoverflow.com/a/73857124>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

        
    <!DOctyPE html>
    <html lang="en">
    <body>
    
    
    <div id="WebBody">
      <P>Answer True or False on qustions</P>
      <p>Is ___</p>
                  <form>
                        <input class="Radio-Button" id="answer1" name="T/F" type="radio">
                        <label>True</label><br>
                        <input class="Radio-Button" name="T/F" type="radio">
                        <label>False</label>
                  </form> 
                  <hr>
      <p>Is ___</p>
                  <form>
                        <input class="Radio-Button" id="answer2" name="T/F" type="radio">
                        <label>True</label><br>
                        <input class="Radio-Button" name="T/F" type="radio">
                        <label>False</label>
                  </form> 
                  <hr>
      <p>Is ___</p>
                  <form>
                        <input class="Radio-Button" id="answer3" name="T/F" type="radio">
                        <label>True</label><br>
                        <input class="Radio-Button" name="T/F" type="radio">
                        <label>False</label>
                  </form> 
                  <hr>
      <p>Is ___</p>
                  <form>
                        <input class="Radio-Button" id="answer4" name="T/F" type="radio">
                        <label>True</label><br>
                        <input class="Radio-Button" name="T/F" type="radio">
                        <label>False</label>
                  </form> 
                  <hr>
          <button onclick="quiz()">Submit</button>
      <p id="score">Score:Not Submitted</p>
    </div>
    
    
    
    
    <script>
    function quiz() {
      var f = 0;
      var a = ""
      alert(f);
      if (document.querySelector("#answer1").checked == true){
        f++ ;
      };
      if (document.querySelector("#answer2").checked == true){
        f++ ;
      };
      if (document.querySelector("#answer3").checked == true){
        f++ ;
      };
      if (document.querySelector("#answer4").checked == true){
        f++ ;
      };
      function checkpass(){
        if (f == 4) {
          a = "Y"
          alert(a)
        } else { 
          a = "N"
          alert(a)
        };
      };
      checkpass();
      alert(document.querySelector("#score").textContent);
      document.querySelector("#score").innerHTML = `Score:${f}/4 ${a}`;
    };
    
    quiz();
    </script>
    </body>
    </html>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Community](https://stackoverflow.com/users/-1)** (2022-09-29): Your answer could be improved with additional supporting information. Please [edit] to add further details, such as citations or documentation, so that others can confirm that your answer is correct. You can find more information on how to write good answers [in the help center](/help/how-to-answer).

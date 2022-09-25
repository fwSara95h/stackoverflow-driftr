---
title: "Displaying the sum of two Javascript Functions"
site: stackoverflow
question_id: 73848254
url: https://stackoverflow.com/q/73848254
asked: 2022-09-25T22:39:46Z
asked_by: "Awojab"
asked_by_url: https://stackoverflow.com/users/7897429
last_edited: 2022-09-26T07:43:09Z
last_editor: "Miu"
last_editor_url: https://stackoverflow.com/users/11451181
tags: [javascript, html]
score: -1
views_at_snapshot: 55
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 328ae33072c2b92eae8ac3acdf3a387a0b625ae4e160b7e17d569ba35f65b8e3
---

# Displaying the sum of two Javascript Functions

Asked by [Awojab](https://stackoverflow.com/users/7897429) on Stack Overflow, <https://stackoverflow.com/q/73848254>, 2022-09-25, last edited 2022-09-26 by [Miu](https://stackoverflow.com/users/11451181). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

The output in the result field is showing NaN for the grandTotal function in the following JavaScript and HTML codes. Please assist to identify the error.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function firstSum(){ 
      subPay=()=>{
       let comPay = document.getElementById('totPay').value;
       if (comPay > 215000){return (comPay - 215000)*0.25;}
        else {return comPay*0.15;}
       }
      document.getElementById('result1').value = subPay();
      }

     groPay=()=>{
      groEstimate=()=>{
       let comPay = document.getElementById('totPay').value;
       if (comPay > 220000){return (comPay - 220000)*0.33;} 
       else {return comPay*0.16;}
      }
     document.getElementById('result2').value = groEstimate();
     }

    function grandTotal(){
      var allPay;
      allPay = firstSum() + groPay();
      document.getElementById('result').value = allPay;
    }

<!-- language: lang-html -->

    <form>
      <input id="totPay" type="number" placeholder = "groPymt">
      <input type = "button" onclick = "grandTotal()" value = "Submit">

      <div><input type="text" class="totsum" id="result1"></div>
      <div><input type="text" class="totsum" id="result2"></div>
      <div>Result: <input type="text" id="result"></div><br><br>
    </form>

<!-- end snippet -->

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[kikon](https://stackoverflow.com/users/16466946)** (2022-09-25): Your functions `firstSum` and `groPay` don't return any value; either capture the retuned values of the internal functions `subPay` and `groEstimate` and return them, or drop the internal functions altogether (keeping their code, of course), as they don't seem to have any intrinsic value.

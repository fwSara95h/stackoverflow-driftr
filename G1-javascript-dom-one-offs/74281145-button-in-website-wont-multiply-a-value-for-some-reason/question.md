---
title: "Button in website wont multiply a value for some reason like the other 2 buttons that should do similar things"
site: stackoverflow
question_id: 74281145
url: https://stackoverflow.com/q/74281145
asked: 2022-11-01T19:53:41Z
asked_by: "ImBadAtMath"
asked_by_url: https://stackoverflow.com/users/16807441
last_edited: 2023-02-16T17:46:49Z
tags: [javascript, html, css]
score: -2
views_at_snapshot: 65
answer_count: 2
accepted_answer_id: 74281602
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 524a4a2fd5e6450b4c6f78ed7fce5e33ed3209ae8f510446f90e4816197cd83f
---

# Button in website wont multiply a value for some reason like the other 2 buttons that should do similar things

Asked by [ImBadAtMath](https://stackoverflow.com/users/16807441) on Stack Overflow, <https://stackoverflow.com/q/74281145>, 2022-11-01, last edited 2023-02-16. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am making a website that has buttons that should multiply vales, but I am having trouble.

The first button adds one to the number at the bottom, the second button multiplies the amount that's added by 2, and the third one should multiply the multiplier, but for some reason it doesn't work. It wont update the numbers or anything, so  I dont know if its a typo or wrong syntax or somthing.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    let numy = 0
    increment = 1
    multy = 2
    multym = 2

    function changeColor() {
      window.alert("downloading virus");
    }

    function adNum() {
      numy += increment
      document.getElementById("num").innerHTML = numy;
    }

    function multiply() {
      increment *= multy
      document.getElementById("earn").innerHTML = "press for earn " + increment;
    }

    function multy() {
      multy *= multym
      document.getElementById("multiplym").innerHTML = "multiply asmdfmasdfams by " + multym;
    }

<!-- language: lang-css -->

    body {
      background-color: powderblue;
    }

    body {
      background-image: url("bigboiwater.jpg");
    }

    h1,
    h2,
    h3,
    h4,
    h5 {
      color: red;
    }

    img {
      max-width: 100%;
      max-height: 100%;
    }

    .water {
      height: 20px;
      cursor: pointer;
      margin: 0 auto;
    }

    #earn {}

    #mulity {}

    #multym
    }
    {}
    .ih {
      left: 1px;
      width: 100px
    }
    .button {
      margin: 0 auto;
    }
    #num {
      font-size: 50;
      color: pink;
    }

<!-- language: lang-html -->

    
    
      <div class="water" ;><button onclick="changeColor()" ;><img src="Click-Here-PNG-Images.png"></button> </div>
    </div>

    <div>
      <button onclick="adNum()" class="button">
          <p id="earn">press for earn 1</p>
        </button>
      <button onclick="multiply()" class="button">
          <p id="multiply">multiply earn by 2</p>
        </button>
      <button onclick="multy()" class="button">
          <p id="multiplym">multiply multiply by 2</p>
        </button>
    </div>
    <p id="num">hi</p>
    <div style="background-color:pink"><label for="Name">Whats your problem:</label><input type="text" id="Name" name="Name" placeholder="I am kinda stupid"></div>

<!-- end snippet -->

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[David](https://stackoverflow.com/users/328193)** (2022-11-01): This is a good opportunity for you to start familiarizing yourself with [using a debugger](https://stackoverflow.com/q/25385173/328193).  When you step through the code in a debugger, which operation first produces an unexpected result?  What were the values used in that operation?  What was the result?  What result was expected?  Why?  To learn more about this community and how we can help you, please start with the [tour] and read [ask] and its linked resources.
- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-11-01): @code No need. There are no parts of the script that needs to run at load time
- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-11-01): One of your problems is you have variable named the same as a function. Rename multy or function multy
- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-11-01): Also use let for all the top vars or add commas between them to reuse the let: `let numy = 0, increment = 1, multy = 2, multym = 2;`

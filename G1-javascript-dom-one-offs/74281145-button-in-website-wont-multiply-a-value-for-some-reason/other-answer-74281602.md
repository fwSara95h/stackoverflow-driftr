---
title: "Button in website wont multiply a value for some reason like the other 2 buttons that should do similar things"
site: stackoverflow
question_id: 74281145
answer_id: 74281602
url: https://stackoverflow.com/a/74281602
author: "DCR"
author_url: https://stackoverflow.com/users/4398966
posted: 2022-11-01T20:46:54Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7d025d44716f2d9d402ccdfd90a3e360369a7a5150929641cce13cb95ac55e58
role: another answer on the same question, kept as context; not my work
---

# Answer by [DCR](https://stackoverflow.com/users/4398966) — 2022-11-01

Posted on Stack Overflow, <https://stackoverflow.com/a/74281602>, 2022-11-01; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

you make multy a global variable.  change the name of your function to multy1



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

    function multy1() {
    console.log("hello")
      
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

    <title>you should drink water</title>
    <link rel="icon" href="troll.png" />
    <div class="ih" style="cursor:progress" ;>
      <h1 style="cursor:wait;">Water!</h1>
      <h2 style="cursor:crosshair" ;>Water!</h2>
      <h3 style="cursor:alias" ;>Water</h3>
      <h4 style="cursor:not-allowed" ;>Water</h4>
      <h5 style="cursor:zoom-in" ;>Water</h5>
      <img src="troll.png">
      <div class="water" ;><button onclick="changeColor()" ;><img src="Click-Here-PNG-Images.png"></button> </div>
    </div>

    <div>
      <button onclick="adNum()" class="button">
          <p id="earn">press for earn 1</p>
        </button>
      <button onclick="multiply()" class="button">
          <p id="multiply">multiply earn by 2</p>
        </button>
      <button onclick="multy1()" class="button">
          <p id="multiplym">multiply multiply by 2</p>
        </button>
    </div>
    <p id="num">hi</p>
    <div style="background-color:pink"><label for="Name">Whats your problem:</label><input type="text" id="Name" name="Name" placeholder="I am kinda stupid"></div>

<!-- end snippet -->

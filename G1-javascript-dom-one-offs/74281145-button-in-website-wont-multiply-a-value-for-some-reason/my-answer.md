---
title: "Button in website wont multiply a value for some reason like the other 2 buttons that should do similar things"
site: stackoverflow
question_id: 74281145
answer_id: 74281810
url: https://stackoverflow.com/a/74281810
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T21:08:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74281810/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dd9b8f133a051c09105feb6d1378ccd13e11970fc850ed2aedadc66cdad8d1a3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74281810>, 2022-11-01; score 0. Text as retrieved 2026-10-12.

You have a function and a variable - both called `multy`. The issues should be resolved if you rename either of them. Below, the variable has been renamed to `multiplier`.


<!-- begin snippet: js hide: false console: true babel: null -->

<!-- language: lang-js -->

    let numy = 0;
    increment = 1;
    multiplier = 2;
    multym = 2;

    function changeColor() {
      window.alert("downloading virus");
    }

    function adNum() {
      numy += increment;
      document.getElementById("num").innerHTML = numy;
    }

    function multiply() {
      increment *= multiplier;
      document.getElementById("earn").innerHTML = "press for earn " + increment;
    }

    function multy() {
      multiplier *= multym;
      document.getElementById("multiply").innerHTML = "multiply earn by " + multiplier;
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
      <button onclick="multy()" class="button">
          <p id="multiplym">multiply multiply by 2</p>
        </button>
    </div>
    <p id="num">hi</p>
    <div style="background-color:pink"><label for="Name">Whats your problem:</label><input type="text" id="Name" name="Name" placeholder="I am kinda stupid"></div>

<!-- end snippet -->

(I also added one more line within the function so that the change is reflected in the middle button text.)

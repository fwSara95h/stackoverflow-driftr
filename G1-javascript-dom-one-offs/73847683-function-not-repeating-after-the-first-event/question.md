---
title: "Function not repeating after the first event"
site: stackoverflow
question_id: 73847683
url: https://stackoverflow.com/q/73847683
asked: 2022-09-25T20:33:13Z
asked_by: "alex_mateko"
asked_by_url: https://stackoverflow.com/users/20084885
last_edited: 2022-09-25T20:40:16Z
last_editor: "j08691"
last_editor_url: https://stackoverflow.com/users/616443
tags: [javascript, html, css]
score: 0
views_at_snapshot: 65
answer_count: 2
accepted_answer_id: 73848105
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d122bb3b8de4b9b690e2bb43ed152223795b8efd7878fab23dc42360568f8d59
---

# Function not repeating after the first event

Asked by [alex_mateko](https://stackoverflow.com/users/20084885) on Stack Overflow, <https://stackoverflow.com/q/73847683>, 2022-09-25, last edited 2022-09-25 by [j08691](https://stackoverflow.com/users/616443). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

 I've been trying to learn how to work with HTML, CSS and JavaScript  with no prior experience with a any sort of programming, and I'm trying some things out as I learn.




I'm trying to get a click event where multiple divs on a list (two in this case) to either lose a specific class if they have it, and gain said class if they don't, all on the same click.

The first time it's clicked, it runs properly, but how do I get it to do this on every click?
I know there's easier ways to do this, but I really just want to experiment with this setup for now.
If anybody has an idea on why it won't switch classes again, or any tips(or insults) whatsoever, please feel free.

Here's the code:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const SignList = document.querySelectorAll('.sign')

    console.log(SignList)

    SignList.forEach((div) => {
      div.addEventListener('click', () => {
        if (div.classList.contains('active')) {
          SignList.forEach((div) => {
            div.classList.remove('active');
            SignList.forEach((div) => {
              if (!div.classList.contains('active')) {
                div.classList.add('active')
              }
            })
          })
        }
      })
    })

<!-- language: lang-css -->

    html {
      margin: 0px;
      padding: 0px;
      box-sizing: border-box;
      height: 100%;
    }

    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100%;
    }

    .sign {
      position: absolute;
      height: 100px;
      width: 100px;
      border: 5px solid black;
      border-radius: 20px;
    }

    .red {
      background-color: red;
      display: none;
    }

    .blue {
      background-color: blue;
      display: none;
    }

    .active {
      display: block;
    }

<!-- language: lang-html -->

    <div class="sign red active"></div>
    <div class="sign blue"></div>

<!-- end snippet -->

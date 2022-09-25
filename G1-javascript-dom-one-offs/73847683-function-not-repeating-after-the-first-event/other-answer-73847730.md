---
title: "Function not repeating after the first event"
site: stackoverflow
question_id: 73847683
answer_id: 73847730
url: https://stackoverflow.com/a/73847730
author: "IT goldman"
author_url: https://stackoverflow.com/users/3807365
posted: 2022-09-25T20:43:13Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8a82ff86423b1505a83cade180bdc2a88297ef006b56fce8f9d57bae875f1c8e
role: another answer on the same question, kept as context; not my work
---

# Answer by [IT goldman](https://stackoverflow.com/users/3807365) — 2022-09-25

Posted on Stack Overflow, <https://stackoverflow.com/a/73847730>, 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You should iterate each of the `.sign` and toggle it. That's how the code now reflects that.


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const SignList = document.querySelectorAll('.sign')

    // console.log(SignList)

    SignList.forEach((div) => {
      div.addEventListener('click', () => {

        SignList.forEach((div) => {
          if (div.classList.contains('active')) {
            div.classList.remove('active');
          } else {
            div.classList.add('active')
          }
        })
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

    <body>

      <div class="sign red active"></div>
      <div class="sign blue"></div>


    </body>

<!-- end snippet -->

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[alex_mateko](https://stackoverflow.com/users/20084885)** (2022-09-26): Thank you! This fits perfectly with what I was initially going for. I probably botched it then just kept complicating it when it didn't work, rather than double check.

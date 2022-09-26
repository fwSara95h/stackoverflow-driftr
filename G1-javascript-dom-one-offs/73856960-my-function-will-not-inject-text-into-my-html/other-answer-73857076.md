---
title: "My Function will not inject text into my HTML"
site: stackoverflow
question_id: 73856960
answer_id: 73857076
url: https://stackoverflow.com/a/73857076
author: "hz-rd"
author_url: https://stackoverflow.com/users/16000542
posted: 2022-09-26T16:20:59Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0b7616062182964f54dced7b67da5f8e1b599fc0b291d211f3e6090b90fcf406
role: another answer on the same question, kept as context; not my work
---

# Answer by [hz-rd](https://stackoverflow.com/users/16000542) — 2022-09-26

Posted on Stack Overflow, <https://stackoverflow.com/a/73857076>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Your problem is here:
```javascript
document.getElementById("score").innerHTML = `Score:${f}/4 ${a}`;
```

You are trying to access the variable "`a`" that's inside checkpass function, You need to put the variable outside from the checkpass functions.

This is your code
```javascript
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
```

It should be something like this:
```javascript
var a = "";
function checkpass() {
    if (f == 4) {
      a = "Y"
      alert(a)
    } else {
      a = "N"
      alert(a)
    };
  };
```

And by the way, variable "`f`" is declared correctly it's not the problem because the error says `"message": "Uncaught ReferenceError: a is not defined"` and variable "`a`" is after variable "`f`" So it's more like it can't access variable "`a`" not var "`f`"

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2022-09-26): Better would be for the function to `return a`
- **[hz-rd](https://stackoverflow.com/users/16000542)** (2022-09-26): It's better but the easiest way for now is to just move the variable itself.

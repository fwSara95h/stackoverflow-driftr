---
title: "How do I use an HTML text box value as a JavaScript parameter or variable and call the JavaScript Function with the text box value?"
site: stackoverflow
question_id: 73832355
answer_id: 73832379
url: https://stackoverflow.com/a/73832379
author: "Sean"
author_url: https://stackoverflow.com/users/11726149
posted: 2022-09-23T19:51:38Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1518ab70243f7be454177fe68d7f2995988833d9f966d0df005f8d957928f58a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Sean](https://stackoverflow.com/users/11726149) — 2022-09-23

Posted on Stack Overflow, <https://stackoverflow.com/a/73832379>, 2022-09-23; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You aren't passing the parameter to the decodeurl function. Try it like this:
```
function decodeUrlDefensev3(link) {
    var matches = link.match(new RegExp('v3/__(.+?)__;(.*?)!'))

    // love me a mutable array
    var decode_pile = Array.from(matches[1]);
    var chars_pile = Array.from(atob(matches[2])).reverse();
    
    for (var match of link.matchAll(/\*/g)) {
        decode_pile[match.index] = match.pop()
    }

    return decode_pile.join('')
}

function handleClick() {
   var link = document.getElementById('textbox1').value;
   decodeUrlDefensev3(link);
}

```

Then in your html:

```

<input type="button" value="button1" onclick="handleClick()"/>
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Gregory Carlton](https://stackoverflow.com/users/20072974)** (2022-09-23): Thank you for the explanation and the help on this, it makes sense to me. I'm still learning, and this has helped a lot. Have a good weekend.

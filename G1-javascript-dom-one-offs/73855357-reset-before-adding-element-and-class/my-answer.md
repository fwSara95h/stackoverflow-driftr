---
title: "Reset before adding element and class"
site: stackoverflow
question_id: 73855357
answer_id: 73858510
url: https://stackoverflow.com/a/73858510
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-26T18:35:59Z
last_edited: 2022-09-26T19:29:39Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73858510/revisions
accepted: true
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2b4d177f0bd252a454b42a4c7c0df117772724bb7beaa5503c36172835add760
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73858510>, 2022-09-26, last edited 2022-09-26; **accepted**; score 1. Text as retrieved 2026-10-12.

It's hard to tell without seeing more of your code - without understanding just how/what you are trying to reset. 

> tried also innerHTML=""

For which element? If it was something like `img_1.innerHTML=""`, then your `small` gets left behind because you added it outside `img_1` . (If that's intentional/necessary then you could try something like `el.parentElement.removeChild(el)` to remove the left-over elements separately.)



> used insertAdjacentHTML because innerHTML was not showing the text

Does the debugger show any errors? When you inspect the outer element, has it not been added to html at all, or is the text just not rendering?


**EDIT**: now that I can see the fiddle, I realize the field you're trying to reset is an input type, so [you *can't* change `innerHTML`][1] - you have to work with `value` and `placeholder` and maybe even `defaultValue` when setting/resetting. 

I would suggest just resetting value and showing the message by adding a class with `[::after][1]` css, but you could also show it by setting a new placeholder or even value [I don't thing setting the error message as value is a good idea at *all* though]. You can define the placeholder style in css as [::placeholder][2]; but personally, I much prefer the `::after` approach.


  [1]: https://stackoverflow.com/questions/20604299/what-is-innerhtml-on-input-elements
  [2]: https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Santi R](https://stackoverflow.com/users/12629043)** (2022-09-26): Thanks, but seems the text is not rendering. In my opinion a img_1.innerHTML = "" before starting , and the img_1.innerHTML ="<small class="danger-color">error</small>", would have been ideal. But is not rendering and no errors in the console.
- **me** (2022-09-26): @SantiRiveira Please see my edit - I hadn't realized you were trying to set innerHTML of an input (though I suppose I should have, from the `name` attribute. My bad... partially =P)

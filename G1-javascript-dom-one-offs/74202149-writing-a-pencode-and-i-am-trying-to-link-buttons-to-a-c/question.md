---
title: "Writing a pencode and I am trying to link buttons to a countdown timer for start and reset"
site: stackoverflow
question_id: 74202149
url: https://stackoverflow.com/q/74202149
asked: 2022-10-26T02:43:10Z
asked_by: "Jon Beckner"
asked_by_url: https://stackoverflow.com/users/20226524
last_edited: 2022-10-26T13:28:16Z
tags: [javascript]
score: 0
views_at_snapshot: 103
answer_count: 1
accepted_answer_id: 74211417
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c47db7f2a38d75452dbc88bcef46697cee94ec3edbeb982de6537e11e82e75ab
---

# Writing a pencode and I am trying to link buttons to a countdown timer for start and reset

Asked by [Jon Beckner](https://stackoverflow.com/users/20226524) on Stack Overflow, <https://stackoverflow.com/q/74202149>, 2022-10-26, last edited 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am in the process of writing a pencode https://codepen.io/Jonbeckner/pen/XWqOvrp
I copied a codepen countdown timer to my existing work. I got it to run when you click the start button. I now need it to reset the time when the reset button is clicked. My code to start the timer is as follows

    document.querySelector('.button-start').addEventListener('click', function() 
    { 
         startTimer();
    }); 

I also set a variable to check if the timer is running so it won't execute multiple times.

My ask is as follows: How would I get it to reset using the reset button? Thanks for putting up with my questions as I learn JS.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Archigan](https://stackoverflow.com/users/14333778)** (2022-10-26): Add an `eventListener` that listens for when the reset button is clicked, then stop the timer by clearing the `setInterval` function for it, then resetting `timeLeft` and `timePassed` back to `TIME_LIMIT` and `null`, as well as resetting the animated timer itself.
- **[Jon Beckner](https://stackoverflow.com/users/20226524)** (2022-10-26): I added the eventListener but am unsure as to how to clear setInterval
- **[Archigan](https://stackoverflow.com/users/14333778)** (2022-10-26): The `id` of a `setTimeout()` or `setInterval()` function is assigned to whatever variable the function is, so in this case `timerInterval`, if in the global scope, would have its value set at the `id` of the function. You can use `clearInterval(timeInterval)` or however you access it to clear the interval in that function.
- **[Jon Beckner](https://stackoverflow.com/users/20226524)** (2022-10-26): document 	.querySelector(".button-start-reset") 	.addEventListener("click", function () { 		clearInterval(timerInterval); 		timeLeft = TIME_LIMIT; 		timerInterval = null; 		isRunning = false; 	});  This code will stop the timer but I'm lost as to what to do to reset. I'm an extremely new js programmer and need lots of help.
- **[Archigan](https://stackoverflow.com/users/14333778)** (2022-10-26): Whatever you did should have worked, as the time is 100% reset, and perhaps if you try to start it again it will work?
- **[Jon Beckner](https://stackoverflow.com/users/20226524)** (2022-10-26): Nothing but stop the timer. I just tried it.
- **[Archigan](https://stackoverflow.com/users/14333778)** (2022-10-26): Look at the answer to this question and try that out instead.

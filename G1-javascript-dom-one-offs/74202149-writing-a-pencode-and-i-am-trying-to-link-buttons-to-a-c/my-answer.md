---
title: "Writing a pencode and I am trying to link buttons to a countdown timer for start and reset"
site: stackoverflow
question_id: 74202149
answer_id: 74211417
url: https://stackoverflow.com/a/74211417
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T16:46:35Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74211417/revisions
accepted: true
score: 2
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fc8d7a7bde800f051592eb96d9c51ae68a8e50cd1cfdf9e8633587c37fba88d7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74211417>, 2022-10-26; **accepted**; score 2. Text as retrieved 2026-10-12.

It speeds up because another countdown gets layered on every time the button is clicked, so it decrements that many times faster. You could disable the button at the start of `startTimer` :

```javascript
function startTimer() {
	//disable start-timer button 
	document.querySelector(".button-start").disabled = true;

	// rest of the function [below] is copied from the fiddle
	timerInterval = setInterval(() => {
		timePassed = timePassed += 1;
		timeLeft = TIME_LIMIT - timePassed;
		document.getElementById("base-timer-label").innerHTML = formatTime(timeLeft);
		setCircleDasharray();
		setRemainingPathColor(timeLeft);

		if (timeLeft === 0) { onTimesUp(); }
	}, 1000);
}
```

To make the reset button work, you just need to define a reset function and then add an event listener [to the reset button] to call the function from:
```javascript
//adding click event listener
document.querySelector(".button-start-reset").addEventListener("click", function(){resetTimer();});

//function definition
function resetTimer() {
	onTimesUp(); 
	const { alert, warning, info } = COLOR_CODES;
	timePassed = 0;
	timeLeft = TIME_LIMIT;
	document.getElementById("base-timer-label").innerHTML = formatTime(timeLeft);
	setCircleDasharray();
	document.getElementById("base-timer-path-remaining").classList.remove(warning.color);
	document.getElementById("base-timer-path-remaining").classList.remove(alert.color);
	document.getElementById("base-timer-path-remaining").classList.add(info.color);

	//enable start-timer button again
	document.querySelector(".button-start").disabled = false;
}
```

<hr><hr>

Also, [if you wanted] you could **remove the disable/enable lines** from the functions above and instead set the start-timer button's click event handler to toggle it between start and pause:
```javascript
var timerRunning = false; // flag variable

document.querySelector(".button-start").addEventListener("click", function () {
	if (timerRunning) {
		timerRunning = false;
		this.innerText = 'Start Timer';
		onTimesUp(); 
	} else {
		timerRunning = true;
		this.innerText = 'Pause Timer';
		startTimer();
	}
});
```
and then the `onTimesUp` function would need to be edited to
```javascript
function onTimesUp() {
	clearInterval(timerInterval); 
	document.querySelector(".button-start").innerText = 'Start Timer';
	timerRunning = false;
}
```

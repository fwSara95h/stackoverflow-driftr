// Code from my Stack Overflow answer https://stackoverflow.com/a/74211417 (posted 2022-10-26), extracted verbatim; may need the question's context to run.

// --- block 1 ---
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

// --- block 2 ---
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

// --- block 3 ---
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

// --- block 4 ---
function onTimesUp() {
	clearInterval(timerInterval); 
	document.querySelector(".button-start").innerText = 'Start Timer';
	timerRunning = false;
}

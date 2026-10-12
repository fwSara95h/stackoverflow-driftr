// Code from my Stack Overflow answer https://stackoverflow.com/a/74281810 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

// --- block 1 ---
let numy = 0;
increment = 1;
multiplier = 2;
multym = 2;

// --- block 2 ---
function adNum() {
  numy += increment;
  document.getElementById("num").innerHTML = numy;
}

// --- block 3 ---
function multiply() {
  increment *= multiplier;
  document.getElementById("earn").innerHTML = "press for earn " + increment;
}

// --- block 4 ---
function multy() {
  multiplier *= multym;
  document.getElementById("multiply").innerHTML = "multiply earn by " + multiplier;
  document.getElementById("multiplym").innerHTML = "multiply asmdfmasdfams by " + multym;
}

// Code from my Stack Overflow answer https://stackoverflow.com/a/73938066 (posted 2022-10-03), extracted verbatim; may need the question's context to run.

// --- block 1 ---
function getInputAsNumber() {
  operator1 = parseInt(document.getElementById("op1").value);
  operator2 = parseInt(document.getElementById("op2").value);
}

// --- block 2 ---
function writeResult(result) {
  let outputElement = document.getElementById("output1x");
  outputElement.value = result;
}

// --- block 3 ---
function add() {
    getInputAsNumber();
    let summe = operator1 + operator2;
    writeResult(summe);
}

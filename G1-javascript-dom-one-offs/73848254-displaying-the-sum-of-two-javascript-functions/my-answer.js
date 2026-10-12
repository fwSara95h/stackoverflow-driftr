// Code from my Stack Overflow answer https://stackoverflow.com/a/73848436 (posted 2022-09-25), extracted verbatim; may need the question's context to run.
function grandTotal(){
  firstSum(); groPay();
  const fs = document.getElementById('result1').value;
  const gp = document.getElementById('result2').value;
  document.getElementById('result').value = fs + gp;
}

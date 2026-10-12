// Code from my Stack Overflow answer https://stackoverflow.com/a/73857154 (posted 2022-09-26), extracted verbatim; may need the question's context to run.
function quiz() {
  var f = 0;
  alert(f);
  if (document.getElementById("answer1").checked == true) {
    f++;
  };
  if (document.getElementById("answer2").checked == true) {
    f++;
  };
  if (document.getElementById("answer3").checked == true) {
    f++;
  };
  if (document.getElementById("answer4").checked == true) {
    f++;
  };

  function checkpass() {
    var a = "";
    if (f == 4) {
      a = "Y"
      alert(a)
    } else {
      a = "N"
      alert(a)
    };
    return a;
  };
  var a = checkpass();
  alert(document.getElementById("score").outerHTML)
  document.getElementById("score").innerHTML = `Score:${f}/4 ${a}`;
};

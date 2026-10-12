// Code from my Stack Overflow answer https://stackoverflow.com/a/74203457 (posted 2022-10-26), extracted verbatim; may need the question's context to run.

// --- block 1 ---
let commonAnc;
let hasTxt = [document.getElementById('mainContainer')]; // or whatever outermost element you want

// --- block 2 ---
while(hasTxt.length == 1) {
  commonAnc = hasTxt[0]; hasTxt = []; 
  let caChilds = commonAnc.children;

// --- block 3 ---
  for(let i=0; i<caChilds.length; i++) {
    if (caChilds[i].textContent.includes("SOMETHING")){
      hasTxt.push(caChilds[i]); 
    } 
  }
}

// --- block 4 ---
console.log(commonAnc);

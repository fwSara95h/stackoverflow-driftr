// Code from my Stack Overflow answer https://stackoverflow.com/a/74052093 (posted 2022-10-13), extracted verbatim; may need the question's context to run.

// --- block 1 ---
let addToButton = document.getElementById('addButton');
let inputFieldset = document.getElementById('toDoInput');
let toDoContainer =  document.getElementById('toDoList');

// --- block 2 ---
addToButton.addEventListener('click', function(){
    let toDoStuff = document.createElement('li');
    toDoStuff.innerHTML = inputFieldset.value;
    toDoContainer.append(toDoStuff);
    inputFieldset.value = "";//clear field
})

// --- block 3 ---
//so that "enter" does the same as addToButton instead of submit
inputFieldset.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        addToButton.click();
    }
});

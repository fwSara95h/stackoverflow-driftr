// Code from my Stack Overflow answer https://stackoverflow.com/a/73835433 (posted 2022-09-24), extracted verbatim; may need the question's context to run.

// --- block 1 ---
function displayOneTable() {
    const cartTable = document.querySelector('table#sepettablo');
    const emptyTable = document.querySelector('table.sepetbos');
    //hopefully you only have 1 table with class='sepetbos' 
    //[would be better to set a unique id]

// --- block 2 ---
var cartRows = cartTable.querySelectorAll('tr').length;
if (cartRows > 0) {//use (cartRows>2) if header/total doesn't count
    emptyTable.setAttribute('hidden', true);

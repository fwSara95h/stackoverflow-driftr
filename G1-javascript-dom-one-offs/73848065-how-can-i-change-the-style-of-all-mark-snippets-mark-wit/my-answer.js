// Code from my Stack Overflow answer https://stackoverflow.com/a/73848324 (posted 2022-09-25), extracted verbatim; may need the question's context to run.
function changeStyleProperty(ssIndex, selTxt, pName, pVal) {
    const cssRules = document.styleSheets[ssIndex].cssRules;
    for (let i = 0; i < cssRules.length; i++) {
        if (cssRules[i].selectorText === selTxt) {
            cssRules[i].style.setProperty(pName, pVal);
        }
    }
}

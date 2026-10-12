// Code from my Stack Overflow answer https://stackoverflow.com/a/73848105 (posted 2022-09-25), extracted verbatim; may need the question's context to run.

// --- block 1 ---
const SignList = document.querySelectorAll('.sign')
console.log(SignList)

function toggleClass(tClass) {
    //incase more div.sign might be added dynamically:
    const sList = document.querySelectorAll('.sign')

    sList.forEach((div) => {
        if (div.classList.contains(tClass)) {
            div.classList.remove(tClass);
        } else {
            div.classList.add(tClass);
        }
    })
}

SignList.forEach((div) => {
    div.addEventListener('click', () => { toggleClass('active') })
})

// --- block 2 ---
function toggleClass(clickTarget, tClass) {
    if (clickTarget.classList.contains(tClass)) {
        const sList = document.querySelectorAll('.sign');
        sList.forEach((div) => {
            if (div.classList.contains(tClass)) {
                div.classList.remove(tClass);
            } else {
                div.classList.add(tClass);
            }
        })
    }
}
SignList.forEach((div) => {
    div.addEventListener('click', (evt) => { toggleClass(evt.target, 'active') })
})

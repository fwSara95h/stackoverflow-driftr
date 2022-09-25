---
title: "Function not repeating after the first event"
site: stackoverflow
question_id: 73847683
answer_id: 73848105
url: https://stackoverflow.com/a/73848105
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-25T21:59:34Z
last_edited: 2022-09-25T22:00:36Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73848105/revisions
accepted: true
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ae4a05fc299af8e12288008419aec6894ebd0852556caaeb494171d091d7d5da
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73848105>, 2022-09-25, last edited 2022-09-25; **accepted**; score 0. Text as retrieved 2026-10-12.

I feel like your question and code are a little confusing in terms of exactly what behavior you want from the click. Also, you probably shouldn't nest so much and reuse the same variable name [like div here] - instead, it might be better to break it down by defining a function.

If you want to toggle a certain class in each div when *any* div is clicked, you might change your js to something like this:

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

On the other hand, if you want to toggle that class *only* if the clicked div contain the class, you can change the above code to :

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

Then, it will only toggle if an "active" element  is clicked on. It won't make a difference here, because the non-"active" elements are not visible, and there are only 2 elements affected, but if the class (for example) changed border color to green, only clicking on divs with green border would do anything....

(`evt.target` passes the object [that the event happened to] to the function in the listener and is more reliable than passing it as `div` like in your code. You could pass on the `evt` object itself to give the function [more information about the event][1], but it's not necessary in this case.)

Hope this helps, and best of luck with your coding journey!


  [1]: https://developer.mozilla.org/en-US/docs/Web/API/Event#properties

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[alex_mateko](https://stackoverflow.com/users/20084885)** (2022-09-26): Thank you! And whoa... thanks for all the tips too. I

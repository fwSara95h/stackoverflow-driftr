---
title: "How can I change the style of all <mark>snippets</mark> within html using javascript?"
site: stackoverflow
question_id: 73848065
answer_id: 73848250
url: https://stackoverflow.com/a/73848250
author: "dale landry"
author_url: https://stackoverflow.com/users/1533592
posted: 2022-09-25T22:37:37Z
last_edited: 2022-09-25T23:40:13Z
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fccef82277ff3518dc69303a90556ffe526c46aedbc93a1ce34ed83934b0b5cf
role: another answer on the same question, kept as context; not my work
---

# Answer by [dale landry](https://stackoverflow.com/users/1533592) — 2022-09-25

Posted on Stack Overflow, <https://stackoverflow.com/a/73848250>, 2022-09-25, last edited 2022-09-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Query all your `mark` elements, then toggle a highlight class to affect their font-weight styling. Get the parents of the mark elements using '.closest()', and add a button to each parent element.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    const marks = document.querySelectorAll('mark')

    // use event target to get the parent element and subsequent 
    // mark element and toggle a class of normal font weight
    function toggleHighlight(e) {
      e.target.closest('li').querySelectorAll('mark').forEach( el => {
        el.classList.toggle('normal')
      })
    }

    marks.forEach(mark => {
      // create the button
      const button = document.createElement('button')
      // add text for the button
      button.textContent = 'Toggle Highlight'
      // get the parent element your mark is living within and append the button to it
      // make sure it only gets one button in case there are more than one mark element
      !mark.parentNode.innerHTML.includes('button') ? mark.parentNode.appendChild(button) : null  
      // event listener for when the button is pressed 
      button.addEventListener('click', toggleHighlight)
    })

<!-- language: lang-css -->

    mark {
      font-weight: bold;
    }

    .normal {
      font-weight: normal;
    }

    li {
      clear: left;
    }

    button {
      float: right;
    }

<!-- language: lang-html -->

    <ul>
      <li>This is not important text</li><hr>
      <li><mark>This text here important text.</mark> But this is not. <mark>We have more important text here as well.</mark> Arcu cursus euismod quis viverra nibh cras pulvinar mattis. Tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Ac turpis egestas integer eget. </li><hr>
      <li>This is text not important text. <mark>But this is</mark></li><hr>
      <li><mark>This text here important text.</mark> But this is not</li><hr>
    </ul>

<!-- end snippet -->

---
title: "Reset before adding element and class"
site: stackoverflow
question_id: 73855357
url: https://stackoverflow.com/q/73855357
asked: 2022-09-26T14:06:40Z
asked_by: "Santi R"
asked_by_url: https://stackoverflow.com/users/12629043
last_edited: 2022-09-26T19:04:00Z
tags: [javascript, validation, dom, frontend]
score: 0
views_at_snapshot: 112
answer_count: 1
accepted_answer_id: 73858510
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7d5d7577945fe9a9d4511c67abf419a97fbe7825d23e67fd9448eb2665d015d7
---

# Reset before adding element and class

Asked by [Santi R](https://stackoverflow.com/users/12629043) on Stack Overflow, <https://stackoverflow.com/q/73855357>, 2022-09-26, last edited 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've been trying to reset after inserting an element with a class with no success. Tried also innerHTML="" but it is not working.
Maybe because I'm using insertAdjacentHTML(). - ?  I couldn't find a remove method before inserting.

    let small = document.querySelector("small")
    let img_1 = document.querySelector('[name="img_1"]')

    //Image fields validation
 
    if (img_1.value =="") {
        
        img_1.classList.add('is-invalid_create')
        small = '<small class="text-danger__Create">Campo imagen 1 no puede estar vacío</small>'
        img_1.insertAdjacentHTML("afterend", small);
    } else {
        img_1.classList.add('is-valid_create')
        img_1.classList.remove('is-invalid_create')
    }


I'm trying to build a validation with an error message if fields are . I used insertAdjacentHTML because innerHTML was not showing the text. 


fiddle : https://jsfiddle.net/gzsudqvm/


I tried to do a simpler approach like:

        function setErrorFor(input, message) {
        input.innerHTML = ""
        input.classList.add('is-invalid_create')
        input.innerHTML = "<small class='danger'>"+message+"</small>" 
    }

But the message is not rendering, and there are no errors.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[bloodyKnuckles](https://stackoverflow.com/users/2743458)** (2022-09-26): Your jsfiddle example is missing a bunch of necessary elements to even be able to test. After either adding or eliminating all the missing stuff, it works fine.

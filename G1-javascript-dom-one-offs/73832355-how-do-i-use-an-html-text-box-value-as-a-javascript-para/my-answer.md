---
title: "How do I use an HTML text box value as a JavaScript parameter or variable and call the JavaScript Function with the text box value?"
site: stackoverflow
question_id: 73832355
answer_id: 73832607
url: https://stackoverflow.com/a/73832607
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-23T20:17:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73832607/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 751ecc663a23249ae712654f220f3e5c3e7ac02f15f59d801a8679d16d0f049b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73832607>, 2022-09-23; score 0. Text as retrieved 2026-10-12.

The error is probably because there are no results from the `link.match` function (for "https://www.google.com"), let alone 3 [2nd and 3rd items of the result are used for `decode_pile` and `chars_pile` respectively]. You should either change the `RegExp` for the match or provide and error message like the commented `if` block in the edited code below. 

Also, your function is not taking updated input from *textbox1* - only the initial value of "https://www.google.com" set in html. You should retrieve it within the function like:

    function decodeUrlDefensev3() {
        var link = document.getElementById('textbox1').value;
        var matches = link.match(new RegExp('v3/__(.+?)__;(.*?)!'))
        
        /*if (!matches || matches.length < 3) {
            alert("Invalid input, could not decode");
            return null;
        }*/
    
        // love me a mutable array
        var decode_pile = Array.from(matches[1]);
        var chars_pile = Array.from(atob(matches[2])).reverse();
        
        for (var match of link.matchAll(/\*/g)) {
            decode_pile[match.index] = match.pop()
        }
    
        return decode_pile.join('')
    }


And then your HTML for the button can simply be:

    <input type="button" value="button1" onclick="decodeUrlDefensev3()"/>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Gregory Carlton](https://stackoverflow.com/users/20072974)** (2022-09-23): Thank you for bringing up the error handling, this was not making any sense to me.  Now that you included the error handling, it makes more sense. Now I just wish I could figure out how to return the URL even if it is an error. Have a good weekend!
- **me** (2022-09-23): @GregoryCarlton just `return link` instead of `return null` inside the error-handling if block, but it will return the un-decoded url from the input.

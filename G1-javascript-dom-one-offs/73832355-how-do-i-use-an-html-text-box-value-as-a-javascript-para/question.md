---
title: "How do I use an HTML text box value as a JavaScript parameter or variable and call the JavaScript Function with the text box value?"
site: stackoverflow
question_id: 73832355
url: https://stackoverflow.com/q/73832355
asked: 2022-09-23T19:47:50Z
asked_by: "Gregory Carlton"
asked_by_url: https://stackoverflow.com/users/20072974
last_edited: 2022-09-24T04:54:53Z
last_editor: "ScandinavianAvian"
last_editor_url: https://stackoverflow.com/users/295783
tags: [javascript, html]
score: 0
views_at_snapshot: 73
answer_count: 2
accepted_answer_id: 73832379
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2a4d2865fe48f35014f794a14cd89c10a57e69b961b197c0939c90af4b7f0570
---

# How do I use an HTML text box value as a JavaScript parameter or variable and call the JavaScript Function with the text box value?

Asked by [Gregory Carlton](https://stackoverflow.com/users/20072974) on Stack Overflow, <https://stackoverflow.com/q/73832355>, 2022-09-23, last edited 2022-09-24 by [ScandinavianAvian](https://stackoverflow.com/users/295783). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a JavaScript function that works on its own, however, I am having difficulty getting it to function correctly inside of an HTML web page (no server backend). The function that works correctly by itself is:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function decodeUrlDefensev3(link) {
      var matches = link.match(new RegExp('v3/__(.+?)__;(.*?)!'))

      // love me a mutable array
      var decode_pile = Array.from(matches[1]);
      var chars_pile = Array.from(atob(matches[2])).reverse();

      for (var match of link.matchAll(/\*/g)) {
        decode_pile[match.index] = match.pop()
      }

      return decode_pile.join('')
    }

    var link = "https://urldefense.com/v3/__https://files.bitsight.com/e3t/Ctc/LR*113/c1NcF04/VWyThK1lvg49W724nRX2d04lQW1xTZ7Q4QfX7gN6fpSV75nCTJV3Zsc37CgZP4N95fbTLz6L-gW48j6gR3bC3zwW6L_GnH7kDhzMW9418Rb3hJ605W2HjF587SWBXyW8RmYtF6fgdWYW5XQmQn1bFttzW5qPlhD5h_TCqW4-gDCr8x7fD0N4M_DVGdxFD9W2T0jhF4j9YsWW7603Qw8dF3j7W36QBsz4RM6hNW6Hpcdy8Qtmw4W8y5VBz2TLWGhVTNFr45gN7FDW7m9S0M1tvjXNW7vLHnj2945hZW437Z0x5Vd_ZcW7MjgJC89gYB6W2Y3sH14zDDZvW39S6bT1pFgM2W8gn9pV4HdltbW3MTVMS59VlW-VBQkF74S69PWW5yn7jz6PhmVLW4sYpYl4yDVH4W3dkf3v6S141VW3Sqpcn7xkSPcW33N24p3R1FxPW3y04W03TWHN4N2wvRyC4j7X83p5G1__;Kw!!HhY5bxTJhQ!vdj_DUrp0JIWgTw61Vg8M1chEvhp0k7XlLFiomq0Wu1rCrze9dzn2inIIVKchdRRP6HqJshCEuIHCbwCa1ha0FPyFA$"

    console.log(decodeUrlDefensev3(link))

<!-- end snippet -->

Expected output: 

```
https://files.bitsight.com/e3t/Ctc/LR*113/c1NcF04/VWyThK1lvg49W72*nRX2d04lQW1xTZ7Q4QfX7gN6fpSV75nCTJV3Zsc37CgZP4N95fbTLz6L-gW48j6gR3bC3zwW6L_GnH7kDhzMW9418Rb3hJ605W2HjF587SWBXyW8RmYtF6fgdWYW5XQmQn1bFttzW5qPlhD5h_TCqW4-gDCr8x7fD0N4M_DVGdxFD9W2T0jhF4j9YsWW7603Qw8dF3j7W36QBsz4RM6hNW6Hpcdy8Qtmw4W8y5VBz2TLWGhVTNFr45gN7FDW7m9S0M1tvjXNW7vLHnj2945hZW437Z0x5Vd_ZcW7MjgJC89gYB6W2Y3sH14zDDZvW39S6bT1pFgM2W8gn9pV4HdltbW3MTVMS59VlW-VBQkF74S69PWW5yn7jz6PhmVLW4sYpYl4yDVH4W3dkf3v6S141VW3Sqpcn7xkSPcW33N24p3R1FxPW3y04W03TWHN4N2wvRyC4j7X83p5G1
```

The above code will return a correctly decoded website URL in the console. This works for technical people however, I am trying to create a basic HTML with a text box for users to enter the encoded URL, click a button, then return the decoded URL on their screen.

Using the below code:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function decodeUrlDefensev3(link) {
      var matches = link.match(new RegExp('v3/__(.+?)__;(.*?)!'))

      // love me a mutable array
      var decode_pile = Array.from(matches[1]);
      var chars_pile = Array.from(atob(matches[2])).reverse();

      for (var match of link.matchAll(/\*/g)) {
        decode_pile[match.index] = match.pop()
      }

      return decode_pile.join('')
    }

    var link = document.getElementById('textbox1').value;

    console.log(link)

<!-- language: lang-html -->

    <input type="text" id="textbox1" value="https://www.google.com" />
    <input type="button" value="button1" onclick="decodeUrlDefensev3(link)" />
    <input type="button" value="button2" onclick="function2()" />

<!-- end snippet -->

The console.log(link) returns the true variable saved above. However, when I click the button, I get an error "Uncaught TypeError: Cannot read properties of null (reading '1')".

How do I pass the textbox input and properly call my function so that whatever is entered inside of textbox1 is parsed using my JavaScript function?

An example of what I am trying to do can be found here:https://jsfiddle.net/37phxda8/1/

I need to use my function above, not the function on that JS Fiddle.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-09-23): Please click [edit], then `[<>]` snippet editor and add a [mcve] with relevant input and expected output. Your `<enter some URL here to be parsed>` is not useful
- **[Gregory Carlton](https://stackoverflow.com/users/20072974)** (2022-09-23): Thank you @mplungjan. I'm new to Stack Overflow and I'll remember that for future questions.
- **[ScandinavianAvian](https://stackoverflow.com/users/295783)** (2022-09-24): I clicked the button looking like this `[<>]` and pasted the code into the relevant panels.

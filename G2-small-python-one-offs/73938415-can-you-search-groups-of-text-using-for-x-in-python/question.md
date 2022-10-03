---
title: "Can you search groups of text using for x in python?"
site: stackoverflow
question_id: 73938415
url: https://stackoverflow.com/q/73938415
asked: 2022-10-03T16:42:15Z
asked_by: "Rambo"
asked_by_url: https://stackoverflow.com/users/20151512
last_edited: 2022-10-03T16:51:27Z
tags: [python, loops, text]
score: -1
views_at_snapshot: 104
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 047d713382aaa1f5fab039863b4552e91ddd16615c7d4b51db4743e127c9016f
---

# Can you search groups of text using for x in python?

Asked by [Rambo](https://stackoverflow.com/users/20151512) on Stack Overflow, <https://stackoverflow.com/q/73938415>, 2022-10-03, last edited 2022-10-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So I am working on a small program that would scan a line of compressed text (Think Variable 1 would be shortened to V1, Variable 2 would be shortened to V2, and things like Start would be shortened to S). I am attempting to have my program scan through this text using for x... loops. My apologies for all the comments in advance, feel free to modify them! Anyways, this is my code:

    Text = "S V1XV2E" # The code is incomplete to search all the text, but that's a me problem

    I = 0 # Create index for later

    for x in Text: # Look through all text
        I = I + 1 # Increase index for every letter searched
        if x == Text[:I]: # Text starts at 0, Text[:I] = 0th char always = S 
            if x == "S": # Therefore this is always correct unless the sample changes
                print("Start")
                I = 1 # Set "I" to 1 to skip over the space
        if x == Text[I:I+2]: # Here the idea is since "I" is set to 1, it will search the text from the 1st to 3rd char, so "V1"
            if x == "V1": # "x" is only 1 character, so this always fails
                print("Var 1")

The only problem is that "x" can only see one character at a time in this case. I can't seem to find any other way of making it represent more than one character. Is there a better way to go about doing this? 

Any and all help in this problem is greatly appreciated!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-03): do you want to loop through [all substrings](https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/) of `x` instead?
- **[Rambo](https://stackoverflow.com/users/20151512)** (2022-10-03): Maybe, can substrings be used to get specific bits of a string instead of all of them at once?
- **me** (2022-10-03): probably; which specific bits do you need? [please give me an example string and the set of substring you would want from it]
- **[Rambo](https://stackoverflow.com/users/20151512)** (2022-10-03): Simply put: I'd need to have x at different points to be equal to "S", "V1", "X", "V2" and "E", essentially chopping up the first string into usable code that can be converted via my program.
- **[ti7](https://stackoverflow.com/users/4541045)** (2022-10-03): if you have an exact list of search possibilities, this might be a rare case for [`re.finditer()`](https://docs.python.org/3/library/re.html#re.finditer) .. however, if you want to simply make a program smaller, you may find very tangentially that using a complete compression algorithm like GZIP will handle ugly corner cases (for example, how would you handle two functions named `Vector1` and `Verify1`?) as it can handle arbitrary text without relying on a complex rules engine
- **[Rambo](https://stackoverflow.com/users/20151512)** (2022-10-03): In the full version I would make, I'd use dictionaries to hold all possibilities of the compressed text, with the full text being the key and the compressed text the value. Would it be possible to do this in conjunction with re.finditer()?  I'm trying to avoid using outside algorithms as it's against the rules of my project, though re.finditer() seems promising if I can use it with dictionaries! If it does work as I hope, how might I go about implementing it?
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2022-10-03): Welcome to Stack Overflow. "Is there a better way to go about doing this?" I would like to be able to answer that, but for all that you wrote here, I still have *absolutely no idea what "this" is*. **What should happen** when you run the code? What does happen instead, and how is that different? Please read [ask] and note well that this is **not a discussion forum**.

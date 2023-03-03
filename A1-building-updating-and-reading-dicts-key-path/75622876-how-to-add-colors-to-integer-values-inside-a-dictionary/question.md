---
title: "How to add colors to integer values inside a dictionary in python?"
site: stackoverflow
question_id: 75622876
url: https://stackoverflow.com/q/75622876
asked: 2023-03-03T03:20:36Z
asked_by: "KrishnaSaran draksharapu"
asked_by_url: https://stackoverflow.com/users/10587646
last_edited: 2023-03-03T03:48:19Z
tags: [python, list, dictionary, integer, colorama]
score: -2
views_at_snapshot: 845
answer_count: 1
accepted_answer_id: 75623892
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9c994d53603f5faba5a256b399894b45480ac5893494b922571aa7ccd8ff318b
---

# How to add colors to integer values inside a dictionary in python?

Asked by [KrishnaSaran draksharapu](https://stackoverflow.com/users/10587646) on Stack Overflow, <https://stackoverflow.com/q/75622876>, 2023-03-03, last edited 2023-03-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to add green color to an integer value which is <= 5 and red color to an integer value >5 , inside a dictionary in python.

    from colorama import Fore, Back, Style
    input_dict = {'key1': 217, 'key2': 2, 'key3': 9, 'key4': 4, 'key5':6}
    for key in input_dict:
        if input_dict[key] < 5:
            <# print input_dict with integer values in red color #>
        if output[key]>5:
            <# print input_dict with integer values in red color #>
    
    expected output = {'key1': 217 (217 value printed in red color), 'key2': 2 (2 value printed in green color), 'key3': 9 (9 value printed in red color), 'key4': 4 (4 value printed in green color), 'key5': 6 (6 value printed in red color)}

expected output_dictionary = {'key1': 217 (value printed in red color), 'key2': 2 (value printed in green color), 'key3': 9 (value printed in red), 'key4': 4 (value printed in green color), 'key5': 6 (value printed in red color)}

I request your help sincere help here.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Unmitigated](https://stackoverflow.com/users/9513184)** (2023-03-03): Integers don't have colors... What are you expecting the dict to look like?
- **[Tom Karzes](https://stackoverflow.com/users/5460719)** (2023-03-03): It sounds like you want to either associate some color value with your integers, in a separate field of some aggregate type, or convert them to a string format that supports color codes (e.g. ansi color), in which case they are no longer integers.  You need to decide what you want your representation to look like, giving a concrete example of it.  The example given is nonsensical, since standard integers don't have color properties.
- **[KrishnaSaran draksharapu](https://stackoverflow.com/users/10587646)** (2023-03-03): I have re-edited the question for better understanding
- **[Tom Karzes](https://stackoverflow.com/users/5460719)** (2023-03-03): It doesn't help.  Give a concrete example of what you want.  Saying something like "217 (value printed in red color)" is meaningless.  It's not valid Python syntax.  What value do you want in place of 217?  Show it.  You have not asked a meaningful question.  You have been told why it's not meaningful.  How do you want to encode the color information?  Do you want to use a tuple, e.g. `(217, "red")`?  Or do you want to encode is as ansi string escapes?  *Be concrete.*  If you can't say what you want, then no one can help you.
- **[Blckknght](https://stackoverflow.com/users/1405065)** (2023-03-03): Even if you do store ANSI colored strings in your dictionary, you probably won't see the colors if you print the whole thing, since printing a dictionary prints the `repr` of its contents. The `repr` of a string will escape non-printable characters, like the Escape character that leads off each ANSI sequence.

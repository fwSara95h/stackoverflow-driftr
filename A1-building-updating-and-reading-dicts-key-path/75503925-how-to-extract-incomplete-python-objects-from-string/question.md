---
title: "How to extract incomplete Python objects from string"
site: stackoverflow
question_id: 75503925
url: https://stackoverflow.com/q/75503925
asked: 2023-02-19T22:47:25Z
asked_by: "Aaditya Ura"
asked_by_url: https://stackoverflow.com/users/5904928
last_edited: 2023-02-20T00:07:29Z
tags: [python, regex, list, dictionary, parsing]
score: -1
views_at_snapshot: 137
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 15cc9098edff7e6e9fb47a63c3f1db66f8990e3d07d564d32399ceedd2c80c47
---

# How to extract incomplete Python objects from string

Asked by [Aaditya Ura](https://stackoverflow.com/users/5904928) on Stack Overflow, <https://stackoverflow.com/q/75503925>, 2023-02-19, last edited 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am attempting to extract valid Python-parsable objects, such as dictionaries and lists, from strings. For example, from the string `"[{'a' : 1, 'b' : 2}]"`, the script will extract `[{'a' : 1, 'b' : 2}]` since the `{}` and `[]` denote completed Python objects.

However, when the string output is incomplete, such as `"[{'a' : 1, 'b' : 2}, {'a' : 1'}]"`, I only attempt to extract `{'a' : 1, 'b' : 2}` and place it into a list `[{'a' : 1, 'b' : 2}]`, as the second Python object is not yet complete and therefore must be left out.


I tried to write a regex pattern to match completed `{}` or `[]`, it works for simple output but failing on nested list or dict.

Code:

    import re 
    
    def match_dict_list(string): 
        pattern = r"\[?\{[^\}\]]*\}\]?|\[?\[[^\]\[]*\]\]?"
        matches = re.findall(pattern, string)
        return matches


But it's failing on `"""[[1, 2, 3], [11, 12, 21]"""` because it's matching `[[1, 2, 3], [11, 12, 21]` while the expected output is only  `[1, 2, 3], [11, 12, 21]` and put it in list `[ [[1, 2, 3], [11, 12, 21] ]`



Some test cases

- Case 1: `"[{'a' : 1, 'b' : 2}, {'a' : 1'"`

    Expected output: `[{'a': 1, 'b': 2}]`
 
- Case 2: `'[[1, 2, 3], [11, 12, 21]'`

    Expected output:` [[1, 2, 3], [11, 12, 21]]`

- Case 3: `"""[{'a': [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 'b': [{'a':"""`

    Expected output: `[{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]`

I am getting the output from APIs but can't do anything from their side; sometimes, the server output is complete, and sometimes, it's incomplete. 

I also tried the updated pattern : `\[?\{[^\}\]]*\}\]?|\[[^\]\[]*\]|\[\[[^\]\[]*\]\]` but it's failing on third case. what is the best option to solve this kind of issue?

I can't use `ast.literal_eval` because as I mentioned above the string output is incomplete such as `" [ { 'a' : 1 } , {'b' : "`.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Maurice Meyer](https://stackoverflow.com/users/7216865)** (2023-02-19): Why you got incomplete 'objects' ?
- **[Mous](https://stackoverflow.com/users/16435355)** (2023-02-19): WRT edit: What if you iterate over all substrings, running `ast.literal_eval` on all of them and discard the ones that throw SyntaxError or similar?
- **[dskrypa](https://stackoverflow.com/users/19070573)** (2023-02-19): Why do you need this?  Maybe there's a better solution for your intended goal.
- **[chepner](https://stackoverflow.com/users/1126841)** (2023-02-19): There is a reason parsers don't try to fix "obvious" syntax errors. Why are you trying to do so?
- **[Mous](https://stackoverflow.com/users/16435355)** (2023-02-19): Also, it's impossible to do this with regex, due to arbitrarily-deeply-nested expressions being possible.
- **[dskrypa](https://stackoverflow.com/users/19070573)** (2023-02-19): Re: `I am getting the output from APIs but can't do anything from their side; sometimes, the server output is complete, and sometimes, it's incomplete.`, APIs should serialize data using a format like JSON, not python reprs (incomplete, to boot).  If you are able to provide feedback to the owner of the API, you should make them fix their output.
- **[Mous](https://stackoverflow.com/users/16435355)** (2023-02-19): On closer inspection, this looks an awful lot more like JSON than python objects. Maybe https://stackoverflow.com/questions/53937434/parsing-incomplete-json-array and the answers might be helpful
- **[tevemadar](https://stackoverflow.com/users/7916438)** (2023-02-19): *`"[{'a' : 1, 'b' : 2}, {'a' : 1'}]"`, I only attempt to extract `{'a' : 1, 'b' : 2}` [...], as the second Python object is not yet complete and therefore must be left out.* - how that could become complete, ever, with a pair-less quotation mark inside, and the closing curly brace and bracket already in place? It's not incomplete, but broken.

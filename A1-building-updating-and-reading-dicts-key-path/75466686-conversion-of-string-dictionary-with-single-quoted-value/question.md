---
title: "Conversion of string dictionary with single quoted values to double quoted values"
site: stackoverflow
question_id: 75466686
url: https://stackoverflow.com/q/75466686
asked: 2023-02-16T00:21:17Z
asked_by: "Eyang Daniel"
asked_by_url: https://stackoverflow.com/users/12848495
last_edited: 2024-02-06T09:24:40Z
tags: [python, regex, string, dictionary, replace]
score: -3
views_at_snapshot: 713
answer_count: 1
accepted_answer_id: 75467703
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3ff66f1d93afecec8c2a6c96b9f01d7c2ac741f2e1e86e3fd2a053df3e2d869b
---

# Conversion of string dictionary with single quoted values to double quoted values

Asked by [Eyang Daniel](https://stackoverflow.com/users/12848495) on Stack Overflow, <https://stackoverflow.com/q/75466686>, 2023-02-16, last edited 2024-02-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Given a dictionary represented as a string with keys and values single-quoted. I'm not good with regular expressions, so I want to know if it is possible to convert the keys and values in the string to double-quoted. The reason for this is to parse the string as a dictionary type in other to extract the keys and values pair.

Below is an example illustrating my challenge

```
Initial as string:
{'first_name': 'John', 'age': 89}

Final as string:
{"first_name": "John", "age": 89}
```

I don't know if regex is possible or any other method.
Please help me out

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-02-16): Why not use `ast.literal_eval()`? It understands both single and double quotes, just like regular Python does.
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-02-16): Replacing the quotes won't work well if there are embedded double quotes, you'll get invalid JSON.
- **[Eyang Daniel](https://stackoverflow.com/users/12848495)** (2023-02-16): Let me try, I haven't used that before
- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-02-16): Why didnt you just produce valid JSON in the first place?
- **[Eyang Daniel](https://stackoverflow.com/users/12848495)** (2023-02-16): I'm creating a user input console using cmd. And I want to run a testcase if the user passes in a dictionary (string) with single and double quotes. So, to get the keys and values in dictionary format from the input. Single double and single quoted words are strings, they should work. That why I asked this question.

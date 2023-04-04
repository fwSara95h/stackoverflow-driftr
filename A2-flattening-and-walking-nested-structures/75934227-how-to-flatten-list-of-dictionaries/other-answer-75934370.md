---
title: "How to flatten list of dictionaries"
site: stackoverflow
question_id: 75934227
answer_id: 75934370
url: https://stackoverflow.com/a/75934370
author: "GSquirrel"
author_url: https://stackoverflow.com/users/19293832
posted: 2023-04-04T22:39:16Z
last_edited: 2023-04-04T23:22:20Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 705f912867416200aa1f2cc49ae7ae9d744f89ea0b3da16a016eec00b02c8da9
role: another answer on the same question, kept as context; not my work
---

# Answer by [GSquirrel](https://stackoverflow.com/users/19293832) — 2023-04-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75934370>, 2023-04-04, last edited 2023-04-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here is another aproach which uses the flatten function which takes a nested list or dictionary as input and returns a flattened list of its elements. It uses recursion to handle nested lists and dictionaries of arbitrary depth.

To use the function with your process data structure, you can extract the nested lists from the dictionary values using indexing and pass them to the flatten function. Here's how you can do it:

```

# define the flatten function
def flatten(lst):
    # create an empty list to store the flattened list
    result = []
    # iterate through each element in the input list
    for item in lst:
        # if the element is a dictionary, recursively flatten its values
        if isinstance(item, dict):
            for val in item.values():
                result.extend(flatten(val))
        # if the element is a list, recursively flatten its elements
        elif isinstance(item, list):
            result.extend(flatten(item))
        # otherwise, append the element to the result list
        else:
            result.append(item)
    # return the flattened list
    return result

# extract the nested lists and flatten them
process1 = flatten(process[0]['process1'])
process2 = flatten(process[1]['process2'])

print(process1)
print(process2)

```

This will output:

```
['subprocess1_1', 'subprocess1_2', 'subprocess2', 'subprocess3_1', 'subprocess3_2', 'subprocess4', 'subprocess5_1_1', 'subprocess5_1_2']
['subprocess2_1']
```

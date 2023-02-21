---
title: "Task is to \"stringify\" a value in Python. If the value is a dict obj which has nested dicts, the function must recursively call itself for the nested"
site: stackoverflow
question_id: 75521540
url: https://stackoverflow.com/q/75521540
asked: 2023-02-21T14:01:04Z
asked_by: "David"
asked_by_url: https://stackoverflow.com/users/21258417
last_edited: never
tags: [python, dictionary, nested, stringify]
score: 0
views_at_snapshot: 505
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8503094c8d5a3c12b001ca7a3562da7e65981b2b4d30d6fd19be1edf824f86c2
---

# Task is to "stringify" a value in Python. If the value is a dict obj which has nested dicts, the function must recursively call itself for the nested

Asked by [David](https://stackoverflow.com/users/21258417) on Stack Overflow, <https://stackoverflow.com/q/75521540>, 2023-02-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

My task is to write a function in Python, which would work similarly as JS's JSON.stringify() method. The func's signature is - `stringify(value[, replacer[, spaces_count]])`. So if `value` is a dict with nested dicts, it must call the implemented function recursively for the nested dict. For example the value is:
`data = { "hello": "world", "is": True, "nested": { "count": 5 } }`
Then the result must be:

```
{
  hello: world
  is: True
  nested: {
  count: 5
  }
}
``` 


So I wrote a code:


```
PRIMITIVES = [str, float, int, bool]
PLAINS = [list, tuple, set]


def stringify(value, replacer: str = ' ', spaces_count: int = 1) -> str:
    
    if type(value) in PRIMITIVES:
        return str(value)
    
    elif type(value) in PLAINS:
        return str(value)
    
    else:
        result = list()
        opening_bracket = '{'
        closing_bracket = '}'
        indent = replacer * spaces_count
        result.append(opening_bracket)
        keys = sorted(set(value))
        for key in keys:
            if type(value[key]) in PRIMITIVES or type(value[key]) in PLAINS:
                result.append(f'{indent + str(key)}: {str(value[key])}')
            else:
                
                stringify(value[key])
                result.append(f'{indent + str(key)}: {str(value[key])}')
        result.append(closing_bracket)
        resulting_string = '\n'.join(result)
        return resulting_string
```

And with it I get the following result:


```
{
 hello: world        
 is: True
 nested: {'count': 5}
}
```

P.S. with non-dictionary values the function must just return `str(value)`

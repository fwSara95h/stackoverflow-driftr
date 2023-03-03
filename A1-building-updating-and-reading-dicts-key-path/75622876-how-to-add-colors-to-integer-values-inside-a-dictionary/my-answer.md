---
title: "How to add colors to integer values inside a dictionary in python?"
site: stackoverflow
question_id: 75622876
answer_id: 75623892
url: https://stackoverflow.com/a/75623892
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-03T06:38:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75623892/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5bf147f9aa7c7bce98b1237d702a7aa5cdd15a16364c84def6e7aaed1bb06860
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75623892>, 2023-03-03; **accepted**; score 1. Text as retrieved 2026-10-12.

The [colorama PyPI page](https://pypi.org/project/colorama/) is pretty clear on how to access the ANSI escape sequences that need to be printed to change the color of **printed** text. However, it is quite important to note that:

> *Even if you do store ANSI colored strings in your dictionary, you probably won't see the colors if you print the whole thing, since printing a dictionary prints the repr of its contents. The repr of a string will escape non-printable characters, like the Escape character that leads off each ANSI sequence.* - [Blckknght](https://stackoverflow.com/users/1405065/blckknght)

So, even if you stored the values like 

```py
# !pip install colorama
# from colorama import Fore, Back, Style
input_dict = {'key1': 217, 'key2': 2, 'key3': 9, 'key4': 4, 'key5':6}

colored_dict = {k: f'{Fore.RED if v>5 else Fore.GREEN}{v}' for k, v in input_dict.items()}
```

`colored_dict` would just look like

> ```py
> {'key1': '\x1b[31m217',
>  'key2': '\x1b[32m2',
>  'key3': '\x1b[31m9',
>  'key4': '\x1b[32m4',
>  'key5': '\x1b[31m6'}
> ```

Although, if you printed those saved values separately<sup>([view examples][1])</sup>, the colors will show (just **remember to reset so that the color** doesn't run on to the next print).

---

If you just wanted to fill in your code snippet, then: <sup>([view output][2])</sup>

```py
for key in input_dict:
    if input_dict[key] > 5:
        print(repr(key)+':', Fore.RED, input_dict[key], Fore.RESET)
        # print input_dict with integer values in red color #
    else:
        print(repr(key)+':', Fore.GREEN, input_dict[key], Fore.RESET)
        # print input_dict with integer values in green color # 
```

---

If you want it to be printed looking like a dictionary, then:

```py
## setup
thresh, cHi, cLo = 5, Fore.RED, Fore.GREEN
cKey, cNorm = Fore.BLUE, Fore.RESET ## set Fore.RESET for cKey as well to NOT color keys
input_dict = {'key1': 217, 'key2': 2, 'key3': 9, 'key4': 4, 'key5': 6}
def colorFunc(kx, vx): 
    return cKey+repr(kx)+': '+(cHi if vx>thresh else cLo)+repr(vx)+cNorm
```

```py
# one line:
print('{', ', '.join(colorFunc(k,v) for k,v in input_dict.items()), '}', sep='')
```

```py
# multi-line:
print('{\n ', ',\n '.join(colorFunc(k,v) for k,v in input_dict.items()), '\n}', sep='')
```

> [![op][3]][3]



  [1]: https://i.sstatic.net/duOsx.png
  [2]: https://i.sstatic.net/mTfuM.png
  [3]: https://i.sstatic.net/u4v3G.png

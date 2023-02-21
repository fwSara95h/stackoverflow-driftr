---
title: "Task is to \"stringify\" a value in Python. If the value is a dict obj which has nested dicts, the function must recursively call itself for the nested"
site: stackoverflow
question_id: 75521540
answer_id: 75525251
url: https://stackoverflow.com/a/75525251
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-21T19:51:13Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75525251/revisions
accepted: false
score: 0
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 42beddbb0abe245bb27cecacf23b1f5cf793b9aa8ca6ffd740773f87066ad9be
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75525251>, 2023-02-21; score 0. Text as retrieved 2026-10-12.

> *with non-dictionary values the function must just return `str(value)`*

then why are you checking against *`PRIMITIVES`* and *`PLAINS`*? You should be able to get your desired output<sup>([view screenshot][1])</sup> with just

```py
def stringify(value, replacer:str=' ', spaces_count:int=1) -> str:
    if not isinstance(value, dict): return str(value) # return repr(value) # 
    curIndent, braceIndent = replacer*spaces_count, replacer*(spaces_count-1)
    unbraced = '\n'.join([ # ',\n'.join([ #
        # f'{curIndent}{repr(k)}: {stringify(v, replacer, spaces_count+1).strip()}' 
        f'{curIndent}{k}: {stringify(v, replacer, spaces_count+1).strip()}' 
        for k, v in value.items()
    ])
    return braceIndent + '{\n' + unbraced + '\n' + braceIndent + '}'

dStr = stringify({ "hello": "world", "is": True, "nested": { "count": 5 } })
```

although, if you use [`repr(value)`](https://www.programiz.com/python-programming/methods/built-in/repr)/`{repr(k)}`/`',\n'.join` (see the commented bits of code) instead of *`str(value)`*/*`{k}`*/*`'\n'.join`* [respectively], then 
- [`dStr`][2] could be parsed<sup>([view screenshot][3])</sup> with [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval) (or even just [`eval`](https://www.programiz.com/python-programming/methods/built-in/eval) but that's less safe), and also
- stringified objects with multiline strings wouldn't break
  - for example, see the stringified representation with and without `repr` for <kbd>`{'header': 'some header', 'content': 'para 1\npara 2'}`</kbd> :

      | without `repr`  | with `repr` |
      |:-:|:-:|
      |[![wo][4]][4]|[![with `repr`][6]][6]|



  [1]: https://i.sstatic.net/wEX4H.png
  [2]: https://i.sstatic.net/gvbHP.png
  [3]: https://i.sstatic.net/lWBoV.png
  [4]: https://i.sstatic.net/Liv2w.png
  [6]: https://i.sstatic.net/wWmbF.png

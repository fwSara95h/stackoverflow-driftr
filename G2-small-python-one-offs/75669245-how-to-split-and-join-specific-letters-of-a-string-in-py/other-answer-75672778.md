---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75672778
url: https://stackoverflow.com/a/75672778
author: "Timus"
author_url: https://stackoverflow.com/users/14311263
posted: 2023-03-08T12:01:07Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fd4787178b42dc28d1ffc7203ddf5fe54bbf838e907a432f6746cc5111631311
role: another answer on the same question, kept as context; not my work
---

# Answer by [Timus](https://stackoverflow.com/users/14311263) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75672778>, 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

If you are not opposed to using a module from the standard library, you could use [`re`][re] and do:
```python
import re

result = re.findall("al|\S", original_words)
```
```python
['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', 'al', 'c', 'o', 'h', 'o',
 'l', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
```
If you want to keep the whitespace:
```python
result = re.findall("al|.", original_words)
```
```python
['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', ' ', 'al', 'c', 'o', 'h', 'o',
 'l', ' ', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
```

 [re]:https://docs.python.org/3.11/library/re.html#module-re

---
title: "Dictionary KeyError while defining 100 value and its sha256"
site: stackoverflow
question_id: 75429715
url: https://stackoverflow.com/q/75429715
asked: 2023-02-12T19:43:01Z
asked_by: "nasrin"
asked_by_url: https://stackoverflow.com/users/21199396
last_edited: 2023-02-12T19:52:21Z
last_editor: "Andrej Kesely"
last_editor_url: https://stackoverflow.com/users/10035985
tags: [python, dictionary, key]
score: 0
views_at_snapshot: 241
answer_count: 1
accepted_answer_id: 75441653
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 773a01fbeb8b3c6e4d95c544f4d0a198631fdc1f0c1aaacbd55ac470555cd45e
---

# Dictionary KeyError while defining 100 value and its sha256

Asked by [nasrin](https://stackoverflow.com/users/21199396) on Stack Overflow, <https://stackoverflow.com/q/75429715>, 2023-02-12, last edited 2023-02-12 by [Andrej Kesely](https://stackoverflow.com/users/10035985). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

#can any one help to find out why in below program, i can not find the value of keys? for instance <sha256 #_hashlib.HASH object @ 0x00000284F9296450> indicate 99

```
from hashlib import sha256
data = list (range (100))
s = list()
for i in data:
    s.append(str(i))
#print(s)
output = list()
for ii in s:
    output.append((sha256(ii.encode('utf-8'))))
#print(output)
l = list()
for iii in output:
    - l.append(str(iii))
print(l)
dictionary = dict(zip(l,data))
print(dictionary)
print(dictionary['<sha256 _hashlib.HASH object @ 0x00000284F9296450>'])
```



#KeyError: '<sha256 _hashlib.HASH object @ 0x00000284F9296450>'

#i have changed type of values,it didn't work

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-02-12): `'<sha256 _hashlib.HASH object @ 0x00000284F9296450>'` is the _string representation_ of the hashlib object.  It is not an _actual_ hashlib object.

---
title: "How to polish return and save to individual JSON/csv file?"
site: stackoverflow
question_id: 75576121
answer_id: 75585156
url: https://stackoverflow.com/a/75585156
author: "SunnyD"
author_url: https://stackoverflow.com/users/12417843
posted: 2023-02-27T20:15:54Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b686c1e256915bbb1c06249aa8765a541454c99cd1bc15932d071525338150fd
role: another answer on the same question, kept as context; not my work
---

# Answer by [SunnyD](https://stackoverflow.com/users/12417843) — 2023-02-27

Posted on Stack Overflow, <https://stackoverflow.com/a/75585156>, 2023-02-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Thanks a lot, @Driftr95

The below code allows to input of multiple text files and then saving the return in individual json files.

```
inpFiles = ['text1.txt', 'text2.txt', 'text3.txt']
# ifLen = len(ifLen)
for inpf in inpFiles: # for ifi, inpf in enumerate(inpFiles, 1):
    # print('', end=f'\r[{ifi} of {ifLen}] processing "{inpf}"...')
    with open(inpf) as f: inputList = f.read().splitlines()
    with open(f'{inpf[:-4]}.json', 'w') as f:   
        json.dump({inp: process(inp) for inp in inputList}, f, indent=4)
```

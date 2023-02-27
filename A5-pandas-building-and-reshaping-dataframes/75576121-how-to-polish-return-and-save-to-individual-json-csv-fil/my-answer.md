---
title: "How to polish return and save to individual JSON/csv file?"
site: stackoverflow
question_id: 75576121
answer_id: 75583260
url: https://stackoverflow.com/a/75583260
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-27T16:45:25Z
last_edited: 2023-02-27T18:37:12Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75583260/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 71fcda92ee0d133a8e613aec2fc426ceb6917b0b53bfa322e0a02a8928aa95af
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75583260>, 2023-02-27, last edited 2023-02-27; **accepted**; score 0. Text as retrieved 2026-10-12.

> *Question 1: The order or category (data) is Names, Colors, and Places. But why does the return has Name, Place, Color order instead? This is not important but was wondering why.*

It's probably because of how the contents of 'glove.6B.100d.txt' are ordered/arranged.

---

> *Question 2: Instead of using `print(process('jonny'))`, how can I input list of text from text file? [Lets suppose name of input text file is TEST.txt.]*

Assuming 'TEST.txt' has an input in each line like 

> ```
> jonny
> green
> park
> [input#4]
> [input#5]
> ```

Then you could read them into a list of strings to loop through and apply `process` to:

```py
with open('TEST.txt') as f: 
    inputList = f.read().splitlines()

# for inp in inputList: print(process(inp)) ## OR
outputList = [process(inp) for inp in inputList] 
for op in outputList: print(op) 
```

---

> *Question 3: [...] How can I save the return in TEST.JSON or TEST.csv file? Basically input and output as same name.*

To save as CSV, you could use pandas [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)<sup>([view examples][1])</sup>

```py
import pandas as pd
# pd.DataFrame(outputList, index=inputList).to_csv('TEST.csv') ## same as:
# pd.DataFrame([process(i) for i in inputList], index=inputList).to_csv('TEST.csv')
 
pd.DataFrame(
    [{'input': inp, **process(inp)} for inp in inputList]
).set_index('input').to_csv('TEST.csv')
```

<br>

and to save as JSON, you can use [`json.dump`](https://docs.python.org/3/library/json.html#json.dump)<sup>(view examples: [op1][2], [op2][3])</sup>

```py
import json

with open('TEST.json', 'w') as f: 
    # json.dump([{'input':inp, 'output': process(inp)} for inp in inputList], f) ## op1
    json.dump({inp: process(inp) for inp in inputList}, f) #, indent=4) ## op2
```

---

#### Added EDIT:

> *Let's suppose I have a list of text files for this. Then how would I be able to process all the text files at once and save the return in the same file name? For example, if I use text1.txt, text2.txt, and text3.txt.....return will be text1.json, text2.json, and text3.json.*

```py
inpFiles = ['text1.txt', 'text2.txt', 'text3.txt']
# ifLen = len(ifLen)
for inpf in inpFiles: # for ifi, inpf in enumerate(inpFiles, 1):
    # print('', end=f'\r[{ifi} of {ifLen}] processing "{inpf}"...')
    with open(inpf) as f: inputList = f.read().splitlines()
    with open(f'{inpf[:-4]}.json', 'w') as f:   
        json.dump({inp: process(inp) for inp in inputList}, f, indent=4)
```

[Using *`f'{inpf[:-4]}.json'`* assumes all file names in *`inpFiles`* end with '.txt']

  [1]: https://i.sstatic.net/FD6og.png
  [2]: https://i.sstatic.net/RJCNL.png
  [3]: https://i.sstatic.net/ORc6o.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[SunnyD](https://stackoverflow.com/users/12417843)** (2023-02-27): Wow life saver! thank you so much! bless you, brother. Everything works like a dream!
- **[SunnyD](https://stackoverflow.com/users/12417843)** (2023-02-27): Sorry to ask more, but one last thing. Let's suppose I have a list of text files for this. Then how would I be able to process all the text files at once and save the return in the same file name? For example, if I use text1.txt, text2.txt, and text3.txt.....return will be  text1.json, text2.json, and text3.json. @Driftr95

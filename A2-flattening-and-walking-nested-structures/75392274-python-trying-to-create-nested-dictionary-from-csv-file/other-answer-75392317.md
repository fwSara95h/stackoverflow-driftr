---
title: "Python: Trying to create nested dictionary from CSV File, but getting KeyError"
site: stackoverflow
question_id: 75392274
answer_id: 75392317
url: https://stackoverflow.com/a/75392317
author: "Corralien"
author_url: https://stackoverflow.com/users/15239951
posted: 2023-02-08T22:19:35Z
last_edited: 2023-02-08T23:20:21Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 533b29e7f70f52e2d4d22839534ba7915d0da7794ec29cc3533b6b42217aea2a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Corralien](https://stackoverflow.com/users/15239951) — 2023-02-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75392317>, 2023-02-08, last edited 2023-02-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use a comprehension to convert string values to integers:

```
import csv

def load_csv(filename):
    data = {}
    with open(filename) as csvfile:
        # Your file has 3 invisible characters at the beginning, skip them
        csvfile.seek(3)
        fh = csv.DictReader(csvfile)
        for row in fh:
            key = row.pop('Region')
            data[key] = {k: int(v) for k, v in row.items()}  # <- HERE
        return data

data = load_csv('data.csv')
```

Output:
```
>>> data
{'midwest': {'American': 2500, 'Asian': 2300, 'Black': 2150},
 'north': {'American': 1200, 'Asian': 2300, 'Black': 2300},
 'south': {'American': 1211, 'Asian': 211, 'Black': 2100}}
```

**Bonus**: The same operation with Pandas:
```
import pandas as pd

data = pd.read_csv('data.csv', index_col='Region').T.to_dict()
print(data)

# Output
{'midwest': {'American': 2500, 'Asian': 2300, 'Black': 2150},
 'north': {'American': 1200, 'Asian': 2300, 'Black': 2300},
 'south': {'American': 1211, 'Asian': 211, 'Black': 2100}}
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): Hi, using first method still getting the KeyError do you know why this could be? It is spelled Region in the file
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-08): As I haven't this problem on your sample, I guess there is something wrong with your file. Can you share it?
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): Yes, how do I share it?
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): I have attached a picture of the csv file in VSCode
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-08): You can use wetransfer or google drive?
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): Yes, do you have your emai;l
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): No I cant use pandas
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-08): You have 3 invisible characters before Region (hexadecimal: ef bb bf)
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): Do you know the fix for this? how did these come
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-08): I don't know why you have them in your file but I already posted a fix (use seek to move the pointer). I tested and it works with your file.
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): Even with the seeker am getting the error
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-08): I tested with your file, I have no error. I really don't understand why! Where do your file come from?
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-08): I downloaded it from my assignment
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-11): do you know if there's a way to do this without DictReader?
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-02-12): Why do you want a such thing? You can do it with csv.reader but it does not make much sense.

---
title: "CSV file save fieldnames each time I run the code while converting dictionary to CSV"
site: stackoverflow
question_id: 75919848
url: https://stackoverflow.com/q/75919848
asked: 2023-04-03T13:10:40Z
asked_by: "Mayur "
asked_by_url: https://stackoverflow.com/users/21187920
last_edited: never
tags: [python, csv, dictionary, opencsv]
score: 0
views_at_snapshot: 44
answer_count: 1
accepted_answer_id: 75920474
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 74ae54771d8690bfea91938ca079b14c98f8e63523292ead0f2286fb1a5b1b12
---

# CSV file save fieldnames each time I run the code while converting dictionary to CSV

Asked by [Mayur ](https://stackoverflow.com/users/21187920) on Stack Overflow, <https://stackoverflow.com/q/75919848>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

so i am attempting to convert dictionary to csv. i want it to append to the same csv file each time for that i used "a" mode. but the issue is each time i run the code it is also writing the keys of dictionary as row. following code and screenshot attached explains the situation

```
def is_known():
    with open("data/data_known.csv", "a",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=current_card.keys())
            writer.writeheader()
            writer.writerow(current_card)
```
here current_card is a dictonary generated each time from another csv using the following code

```
global data
data = pandas.read_csv("data/data_unknown.csv")
to_learn = data.to_dict(orient="records")
global current_card
current_card = random.choice(to_learn)
print(current_card)
```



[screenshot for reference ](https://i.sstatic.net/nlDft.png)

any help is appreciated!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[eike](https://stackoverflow.com/users/4253931)** (2023-04-03): You only want to write the header once and call `writerow` for every new set of data you want to convert.

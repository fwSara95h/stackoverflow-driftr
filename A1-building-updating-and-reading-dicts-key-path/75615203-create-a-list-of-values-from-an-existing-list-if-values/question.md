---
title: "Create a list of values from an existing list if values are nearby"
site: stackoverflow
question_id: 75615203
url: https://stackoverflow.com/q/75615203
asked: 2023-03-02T12:06:56Z
asked_by: "sailestim"
asked_by_url: https://stackoverflow.com/users/5661316
last_edited: never
tags: [python, list, loops, dictionary]
score: 0
views_at_snapshot: 71
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 24452340e7545bafb034a138b949f4e0c6f7e1d981538b2fc15d50524732ceaa
---

# Create a list of values from an existing list if values are nearby

Asked by [sailestim](https://stackoverflow.com/users/5661316) on Stack Overflow, <https://stackoverflow.com/q/75615203>, 2023-03-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of dictionaries 
```
[{"Name": 'A', "Area": 10000, "Price": 100}, 
{"Name": 'B', "Area": 9500, "Price": 99},
{"Name": 'C', "Area": 11000, "Price": 101},
{"Name": 'D', "Area": 12000, "Price": 150}
{"Name": 'E', "Area": 14000, "Price": 200},
{"Name": 'F', "Area": 14500, "Price": 400},
{"Name": 'G', "Area": 12999, "Price": 159}]
```

I'd like to create 2 new lists of dictionaries based on the two threshold criteria on *Area* and *Price* key. At this example the threshold I use is 1000 for *Area* and 10 for *Price*, so I'm expecting to receive 2 lists:

Possible duplicates which follow the threshold:
```
[{"Name": 'A', "Area": 10000, "Price": 100},    #Because it is less than 1000 in Area and less than 10 in Price for B and C items
{"Name": 'B', "Area": 9500, "Price": 99},    #For A and C 
{"Name": 'C', "Area": 11000, "Price": 101},    #For A and B
{"Name": 'D', "Area": 12000, "Price": 150},    #For G, but not for C because the price difference is more than 10
{"Name": 'G', "Area": 12999, "Price": 159}]    #For D
```

The remaining items from original list of dicts which were not selected as duplicates 
```
[{"Name": 'E', "Area": 14000, "Price": 200},    #Not selected because the price difference is more than 10
{"Name": 'F', "Area": 14500, "Price": 400}    #The same
```

The only idea, which comes to my mind is the naive solution to perform 2 loops for the each list to compare the *Area* and *Price* values with others. I am sure there is more *pythonic* way of the solution

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mrblue6](https://stackoverflow.com/users/18505884)** (2023-03-02): This line will check if the area of a dictionary is within threshold of the next dictionary. It only checks the next dictionary in the list, so it doesn't solve your problem but hopefully gives you an idea of what you could do. `dicts_range = range(0, len(dicts) - 1)` `k = [dicts[i] if(-1000 <= dicts[i]["Area"] - dicts[i+1]["Area"] <= 1000) else 1+1 for i in dicts_range]`
- **[mrblue6](https://stackoverflow.com/users/18505884)** (2023-03-02): The `else 1+1` is just there because it wasn't letting me to `else continue`
- **[mrblue6](https://stackoverflow.com/users/18505884)** (2023-03-02): Checking both price and area: `k = [dicts[i] if((-1000 <= dicts[i]["Area"] - dicts[i+1]["Area"] <= 1000) and (-10 <= dicts[i]["Price"] - dicts[i+1]["Price"] <= 10)) else 1+1 for i in dicts_range]`

---
title: "How to map a function over a dataframe field that is a list"
site: stackoverflow
question_id: 75827968
answer_id: 75845156
url: https://stackoverflow.com/a/75845156
author: "harriet"
author_url: https://stackoverflow.com/users/17433572
posted: 2023-03-25T23:45:18Z
last_edited: 2023-03-25T23:53:23Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1c07395b6ae5714da581ba21823185578786f9363c274afc021f1b647f7e030d
role: another answer on the same question, kept as context; not my work
---

# Answer by [harriet](https://stackoverflow.com/users/17433572) — 2023-03-25

Posted on Stack Overflow, <https://stackoverflow.com/a/75845156>, 2023-03-25, last edited 2023-03-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Including this in case another example will help you:

I made an activities.json to test:

    {"STUDENT_ID": "FredID", "RECORD_ID": "gobbledeegook1", "NODE_NAME": "Node1", "ACTIVITY_NAME": "MyActivity1", "ACTIVITY_GRADE": "PreK, Kindergarten"}
    {"STUDENT_ID": "FredID", "RECORD_ID": "gobbledeegook2", "NODE_NAME": "Node1", "ACTIVITY_NAME": "MyActivity1", "ACTIVITY_GRADE": "Kindergarten"}
    {"STUDENT_ID": "FredID", "RECORD_ID": "gobbledeegook3", "NODE_NAME": "Node2", "ACTIVITY_NAME": "MyActivity2", "ACTIVITY_GRADE": "1st Grade"}
    {"STUDENT_ID": "JaniceID", "RECORD_ID": "gobbledeegook4", "NODE_NAME": "Node3", "ACTIVITY_NAME": "MyActivity3", "ACTIVITY_GRADE": "Kindergarten"}
    {"STUDENT_ID": "JaniceID", "RECORD_ID": "gobbledeegook5", "NODE_NAME": "Node3", "ACTIVITY_NAME": "MyActivity3", "ACTIVITY_GRADE": "1st Grade"}

and then create a dictionary (nodes) with key values for each node and a set of grades listed for these nodes. I used .strip() when iterating over the grades:list() produced by .split(',') because sometimes there is whitespace (i.e. " Kindergarten"):

    import pandas as pd
    path = "activities.jsonl"
    df = pd.read_json(path_or_buf=path, lines=True, orient='records')

    nodes = dict()
    for i in range(len(df)):
        currNode = df["NODE_NAME"][i]
        grades = df["ACTIVITY_GRADE"][i].split(',')
        if currNode not in nodes:
            nodes[currNode] = set()
        for grade in grades:
            nodes[currNode].add(grade.strip())
    # {'Node1': {'Kindergarten', 'PreK'}, 'Node2': {'1st Grade'}, 'Node3': {'Kindergarten', '1st Grade'}}
    indices = {"Preschool": -2, "PreK": -1, "Kindergarten": 0, "1st Grade": 1, "2nd Grade": 2, "3rd Grade": 3, "4th Grade": 4, "5th Grade": 5}
    minGrades = dict()
    for node in nodes:
        currMin = ""
        currIndex = 10
        for grade in nodes[node]:
            if indices[grade] < currIndex:
                currIndex = indices[grade]
                currMin = grade
        minGrades[node] = currMin

    df['MIN_NODE_GRADE'] = [None for i in range(len(df))]
    for i in range(len(df)):
        currNode = df["NODE_NAME"][i]
        minGrade = minGrades[currNode]
        df['MIN_NODE_GRADE'][i] = minGrade

    print(df)

which produces the updated df:

      STUDENT_ID       RECORD_ID  ...      ACTIVITY_GRADE MIN_NODE_GRADE
    0     FredID  gobbledeegook1  ...  PreK, Kindergarten           PreK
    1     FredID  gobbledeegook2  ...        Kindergarten           PreK
    2     FredID  gobbledeegook3  ...           1st Grade      1st Grade
    3   JaniceID  gobbledeegook4  ...        Kindergarten   Kindergarten
    4   JaniceID  gobbledeegook5  ...           1st Grade   Kindergarten

-- I also assumed "PreK" was a typo.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-26): Thanks for your help! I am not advanced enough to understand it and therefore troubleshoot it... I don't know how to work with json's, and I would need to export my dataframe as a json and then re-import it in order to test this. But I'm sure it works well for those who are more advanced!
- **[harriet](https://stackoverflow.com/users/17433572)** (2023-03-26): I just used the json to make the dataframe -- after that, it should work the same! But, I get you--it's a bit more code xD

---
title: "Python: Trying to create nested dictionary from CSV File, but getting KeyError"
site: stackoverflow
question_id: 75392274
url: https://stackoverflow.com/q/75392274
asked: 2023-02-08T22:14:00Z
asked_by: "Ak2012"
asked_by_url: https://stackoverflow.com/users/20180341
last_edited: 2023-02-08T23:17:58Z
tags: [python, file, dictionary]
score: 1
views_at_snapshot: 118
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b4f258d2676fab839c79f7ae5cd0ec2844735e47bcd5581aab6d8131fa128bda
---

# Python: Trying to create nested dictionary from CSV File, but getting KeyError

Asked by [Ak2012](https://stackoverflow.com/users/20180341) on Stack Overflow, <https://stackoverflow.com/q/75392274>, 2023-02-08, last edited 2023-02-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am currently am trying to create a nested dictionary from a csv file.

The CSV File represents how many people there are for each demographic region. In the nested dictionary each key is a region and the value is another dictionary. The inner dictionary uses the demographic as key and the number of people for its value.
```
Region,American,Asian,Black
midwest,2500,2300,2150
north,1200,2300,2300
south,1211,211,2100
```

Currently have:
```
def load_csv(filename):
data={}
    with open(filename) as csvfile:
        fh = csv.DictReader(csvfile)
        for row in fh:
            key = row.pop('Region')
            data[key] = row
        return data
```

Expected Output (must convert the numbers from strings to integers):
```
{'west':{'American': 2500, 'ASIAN': 2300, ...}, 'north':{'American': 1200, ..}...}
```

I'm getting stuck when running my code as it is giving me "KeyError: 'Region'"

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-02-08): This would be so much shorter with pandas [`.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv) and [`.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html?highlight=to_dict#pandas.DataFrame.to_dict) : just **`def load_csv(filename): return pd.read_csv(filename, index_col=0).to_dict('index')`** [This just takes the first column as index, no matter what it is; you could also use `index_col='Region'` and it would raise error if `Region` column was missing]
- **[Ak2012](https://stackoverflow.com/users/20180341)** (2023-02-11): We are not able to use pandas

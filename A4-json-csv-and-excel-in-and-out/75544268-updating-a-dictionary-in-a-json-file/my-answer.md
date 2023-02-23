---
title: "Updating a dictionary in a JSON File"
site: stackoverflow
question_id: 75544268
answer_id: 75546639
url: https://stackoverflow.com/a/75546639
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-23T15:07:35Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75546639/revisions
accepted: false
score: 1
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a21266ddc64701bed7e0a06e02d997723e73800ad7e142e818fac25b7295b37f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75546639>, 2023-02-23; score 1. Text as retrieved 2026-10-12.

> *With `json` format data in a file, you cannot reliably overwrite parts of the file. You should read the entire file, make changes as python objects, and finally write the entire file back.* – [quamrana](https://stackoverflow.com/users/4834/quamrana)

You can do so with the code below.<sup>([view result][1])</sup>

```python
with open('testaccount.json', 'r') as f: 
    data = json.load(f)

for ri, record in enumerate(data["account_details"]):
    if record["Username"] == "TestingUsername":
        new_data = {'Details': {'Preset1': {
                    'Username': 'TestingUsername',
                    'Password': 'TestingPassword3',
                    'URL': 'TestingURL.com:'          }}}
        
        data["account_details"][ri].update(new_data)
# print(data)

with open('testaccount.json', 'w') as f: 
    json.dump(data, f, indent=4)
```

<sup>**Note that *`record.update(new_data)`* would not affect `data` as `record` is just a copy of `data["account_details"][ri]`.**</sup>


  [1]: https://i.sstatic.net/3xpMC.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Trqzy](https://stackoverflow.com/users/15612849)** (2023-02-23): Is there a way to add accounts rather than overwriting? This works as intended but I wanna be able to add more presets.
- **me** (2023-02-23): @Trqzy No. As stated, JSON files can't added to or updated if you want to maintain valid json structures - you'll always have to load, edit and overwrite like this. If you want to be able to append, you'll need to store your data as CSV or something, and if you want to be able to interact [i.e., edit previous data as well without loading] you could try something like .db files with [SQLite](https://towardsdatascience.com/d553989c87bd), but both will require you to flatten your data, so you'll have at least 2 tables if you don't want data redundancies
- **me** (2023-02-23): @Trqzy If you don't want to flatten, I think there's also NoSQL options like mogodb support nested structures, but I'm not so familiar with that, and I don't know if the data can be interactable from a file like with SQLite
- **[Trqzy](https://stackoverflow.com/users/15612849)** (2023-02-24): Thing is I have to use a JSON file. But taking in the solution you gave, can't I just add more presets then overwrite that record? If I was to put the Details dictionary into a list and then add to it then overwrite the dictionary would this not work?
- **me** (2023-02-24): @Trqzy yes ofc you can add/edit as much as you like before overwriting. You can do whatever you like before `.dump`
- **[Trqzy](https://stackoverflow.com/users/15612849)** (2023-02-24): What would the code be like if I wanted to add to the details dictionary then overwrite it?
- **[Trqzy](https://stackoverflow.com/users/15612849)** (2023-02-24): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/252103/discussion-between-trqzy-and-driftr95).

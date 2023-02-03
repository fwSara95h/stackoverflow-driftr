---
title: "How do i store key-value information that has variables in python?"
site: stackoverflow
question_id: 75336224
answer_id: 75341197
url: https://stackoverflow.com/a/75341197
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-03T21:29:57Z
last_edited: 2023-02-03T22:03:05Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75341197/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5c7a72b4c9860fcf6ed0bbfec692c4d8303648ed09ce7f07cf209a0c84b50f40
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75341197>, 2023-02-03, last edited 2023-02-03; **accepted**; score 0. Text as retrieved 2026-10-12.

JSON files cannot be appended to [afaik] without loading the previous data and then updating with new data before saving again [so, the file *will* be over-written, but since the old data was loaded, it will be saved again but with the addition of the new data]. You could have a function for loading lists from JSON files - something like

```python
# import json
def list_fromJsonFile(filename, printWarnings=False):
    try: 
        with open(filename, 'r') as f: retList = json.load(f)
    except Exception as e:
        retList = []
        if printWarnings: print('Failed to load', repr(e))
    if not isinstance(retList, list): 
        if printWarnings: print('Returning as', [{'previous_data': type(retList)}])
        retList = [{'previous_data': retList}]
    return retList
```

With that, I don't see why this should cause any issues [in terms of JSON handling]:

```python 
    def create_task():
        storageFilePath = 'taskstorage.json' # path to storage
        tasksList = list_fromJsonFile(storageFilePath) # load previous data

        taskDict = {
            'name': TaskNameEntry.get()
            'Group': GroupNameEntry.get()
            'Priority': PriorityEntry.get()
            'Start_Date': start_date_entry.get()
            'End_Date': end_date_entry.get()
            'Start_Time': start_time_entry.get()
            'end_time': end_time_entry.get()
        }

        with open(storageFilePath, 'w') as jsonfile:
            json.dump(
                tasksList+[taskDict], jsonfile, indent=4,
                default=lambda o: getattr(o, '__dict__', str(o))
            ) 
        messagebox.showinfo('eTasks', 'Task saved')
```

<sup>[ As far as I'm aware, the values returned by `Entry.get()` are JSON-serializable, but still I passed *`default=lambda o: getattr(o, '__dict__', str(o))`* to [`.dump`](https://docs.python.org/3/library/json.html#json.dump) just in case, so that any non-serializable values are converted to dictionaries (or, if that's not possible, to string).]</sup>

Since you're saving *`tasksList+[taskDict]`*, you should not be losing any of the old data; and then, if you want to

> be able to call each task separately by name 

You can load the saved list and convert that list to a [nested] dictionary keyed to `name`.

```python
tasks_list = list_fromJsonFile('taskstorage.json', printWarnings=True)
tasks_by_name = {t['name']: t for t in tasks_list if isinstance(t,dict) and 'name' in t}
```

<sup>**Note that if there are any duplicate `name`s, only the last task `t` of each `name` will remain in `tasks_by_name`.**</sup>

You can loop through the task dictionaries with `for task in tasks_list`, or get a task (named `task_name='task_1'`, for example) with `tasks_by_name[task_name]`, or `tasks_by_name['task_1']`, or [if you're not sure that there's a task with that name] **`tasks_by_name.get(task_name)`**.

---

If you don't want to have to load previous data every time you want to add a new task, I suggest [using CSV files](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) for storage instead.

```python
# import os
# import pandas as pd

    def create_task():
        storageFilePath = 'taskstorage.csv' # path to storage

        # taskDict = {...} ## AS BEFORE

        wHed = not os.path.isfile(storageFilePath)
        pd.DataFrame([taskDict]).to_csv(storageFilePath,mode='a',index=False,header=wHed)
        messagebox.showinfo('eTasks',f'Task saved to {os.path.abspath(storageFilePath)}') 
```

<sup>[ Passing `mode='a'` appends to file instead of over-writing old data, and the `wHed` flag is for adding the headers row if a new file is created. ]</sup>

In this case, a function like `list_fromJsonFile` is no longer needed as the tasks can be loaded with [`.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). 

```python
# tasks_by_name = pd.read_csv('taskstorage.csv').set_index('name').to_dict('index')#maybe
tasks_list = pd.read_csv('taskstorage.csv').to_dict('records')
tasks_by_name = {t['name']: t for t in tasks_list if isinstance(t,dict) and 'name' in t}
```

---

> dbm overwrote the previous data

From what I understand, you can only have one instance of each key in a dbm file. You could make the name *part* of the keys to keep from overwriting other tasks [as long as the names are unique].

```python
    def create_task():
        with dbm.open('taskstorage.db' , 'c') as taskdb:
            tName = TaskNameEntry.get()
            taskdb[f'{tName} name']=tName
            taskdb[f'{tName} Group']=GroupNameEntry.get()
            taskdb[f'{tName} Priority']=PriorityEntry.get()
            taskdb[f'{tName} Start_Date']=start_date_entry.get()
            taskdb[f'{tName} End_Date']=end_date_entry.get()
            taskdb[f'{tName} Start_Time']=start_time_entry.get()
            taskdb[f'{tName} end_time']=end_time_entry.get()
        messagebox.showinfo('eTasks', 'Task saved')
```

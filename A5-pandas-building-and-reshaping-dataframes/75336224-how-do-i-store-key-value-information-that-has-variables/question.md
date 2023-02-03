---
title: "How do i store key-value information that has variables in python?"
site: stackoverflow
question_id: 75336224
url: https://stackoverflow.com/q/75336224
asked: 2023-02-03T13:12:24Z
asked_by: "Minion123"
asked_by_url: https://stackoverflow.com/users/19969808
last_edited: 2023-02-03T13:23:52Z
last_editor: "brunns"
last_editor_url: https://stackoverflow.com/users/1073696
tags: [python, dictionary, datastore]
score: 0
views_at_snapshot: 170
answer_count: 1
accepted_answer_id: 75341197
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5f9f4adc66930b57adc0c1f693581e6a1ac353a94ba8446152092edc39fb6ad3
---

# How do i store key-value information that has variables in python?

Asked by [Minion123](https://stackoverflow.com/users/19969808) on Stack Overflow, <https://stackoverflow.com/q/75336224>, 2023-02-03, last edited 2023-02-03 by [brunns](https://stackoverflow.com/users/1073696). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm creating an app to store tasks. However, I can't find a working solution that stores more than one task.
This is the code I'm running that you should need:

```python
def newtaskwin():
    newtaskwin=Toplevel(todohome)
    newtaskwin.geometry()

    taskbxfrme=tk.Frame(newtaskwin)
    TaskNameLbl=tk.Label(newtaskwin, text='Task Name:').grid(row=1, column=0, pady=5)
    TaskNameEntry=ttk.Entry(newtaskwin, width=100)
    TaskNameEntry.grid(row=1, column=1, pady=5)

    GroupNameLbl=tk.Label(newtaskwin, text='Group:').grid(row=2, column=0, pady=5)
    GroupNameEntry=ttk.Entry(newtaskwin, width=100)
    GroupNameEntry.grid(row=2, column=1, pady=5)

    PriorityLbl=tk.Label(newtaskwin, text='Priority:').grid(row=3, column=0, pady=5)
    PriorityEntry=ttk.Entry(newtaskwin, width=100)
    PriorityEntry.grid(row=3, column=1, pady=5)

    start_date_lbl=tk.Label(newtaskwin, text='Start Date:').grid(row=4, column=0, pady=5)
    start_date_entry=ttk.Entry(newtaskwin, width=100)
    start_date_entry.grid(row=4, column=1, pady=5)

    end_date_lbl=tk.Label(newtaskwin, text='End Date:').grid(row=5, column=0, pady=5)
    end_date_entry=ttk.Entry(newtaskwin, width=100)
    end_date_entry.grid(row=5, column=1, pady=5)

    start_time_lbl=tk.Label(newtaskwin, text='Start Time:').grid(row=6, column=0, pady=5)
    start_time_entry=ttk.Entry(newtaskwin, width=100)
    start_time_entry.grid(row=6, column=1, pady=5)

    end_time_lbl=tk.Label(newtaskwin, text='End Time:').grid(row=7, column=0, pady=5)
    end_time_entry=ttk.Entry(newtaskwin, width=100)
    end_time_entry.grid(row=7, column=1, pady=5)


    def create_task():
        with dbm.open('taskstorage.db' , 'n') as taskdb:
            taskdb['name']=TaskNameEntry.get()
            taskdb['Group']=GroupNameEntry.get()
            taskdb['Priority']=PriorityEntry.get()
            taskdb['Start_Date']=start_date_entry.get()
            taskdb['End_Date']=end_date_entry.get()
            taskdb['Start_Time']=start_time_entry.get()
            taskdb['end_time']=end_time_entry.get()
            messagebox.showinfo('eTasks', 'Task saved')
        
        
    create_task_btn=tk.Button(newtaskwin, command=create_task, width=10, text='Save').grid(row=9, column=0)
```

I tried using json and dbm; json didn't allow me to store the dictionary with variables, dbm overwrote the previous data and json didn't dump the data because of the immutable and mutable data type rules in dictionaries in python.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[geekay](https://stackoverflow.com/users/1478801)** (2023-02-03): pickle them and store them
- **[Reinderien](https://stackoverflow.com/users/313768)** (2023-02-03): First, this has too much tkinter and not enough data to be reproducible. Second - isn't overwriting a file what you want to do? If not, what do you want to do?
- **[Minion123](https://stackoverflow.com/users/19969808)** (2023-02-03): What I want to be able to do is store multiple tasks in the same file, without deleting the previous contents, and be able to call each task separately by name in the main code. Also, how do i make it reproducible?
- **[pho](https://stackoverflow.com/users/843953)** (2023-02-03): _"how do i make it reproducible?"_: See [mre]

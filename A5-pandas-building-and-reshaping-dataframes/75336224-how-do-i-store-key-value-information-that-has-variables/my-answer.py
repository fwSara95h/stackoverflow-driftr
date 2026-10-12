# Code from my Stack Overflow answer https://stackoverflow.com/a/75341197 (posted 2023-02-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
tasks_list = list_fromJsonFile('taskstorage.json', printWarnings=True)
tasks_by_name = {t['name']: t for t in tasks_list if isinstance(t,dict) and 'name' in t}

# --- block 4 ---
# import os
# import pandas as pd

    def create_task():
        storageFilePath = 'taskstorage.csv' # path to storage

        # taskDict = {...} ## AS BEFORE

        wHed = not os.path.isfile(storageFilePath)
        pd.DataFrame([taskDict]).to_csv(storageFilePath,mode='a',index=False,header=wHed)
        messagebox.showinfo('eTasks',f'Task saved to {os.path.abspath(storageFilePath)}')

# --- block 5 ---
# tasks_by_name = pd.read_csv('taskstorage.csv').set_index('name').to_dict('index')#maybe
tasks_list = pd.read_csv('taskstorage.csv').to_dict('records')
tasks_by_name = {t['name']: t for t in tasks_list if isinstance(t,dict) and 'name' in t}

# --- block 6 ---
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

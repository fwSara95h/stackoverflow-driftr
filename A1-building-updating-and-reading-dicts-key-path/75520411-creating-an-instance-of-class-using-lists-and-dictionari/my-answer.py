# Code from my Stack Overflow answer https://stackoverflow.com/a/75524347 (posted 2023-02-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
equipments = ['EAF1','EAF2','AOD1', 'AOD2','LF1','LF2']
procTimes = {"1": 80.0, "2": 40.0}
eleCon = {"1": 34.0, "2": 49.0}

# --- block 2 ---
class Tasks():
    def __init__(self, equipment, id, processingtime:dict={}, electricityconsumption:dict={}, **kwargs):
        self.equipment = equipment
        self.id = id
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.processingtime = processingtime.get(id)
        self.electricityconsumtption = electricityconsumption.get(id)

tasksList = [
    Tasks(taskEq, str(taskId), procTimes, eleCon, kwarg1=f'kw1_{taskId}', kwarg2=f'kw2_{taskId}') 
    for taskId, taskEq in enumerate(equipments, 1)
]

# --- block 3 ---
class Task():
    def __init__(self, id, equipment, **kwargs):
        self.id=id
        self.equipment=equipment
        for key,value in kwargs.items(): setattr(self,key,value)

# --- block 4 ---
## Task(task_id,task_eq,processingtime=...,electricityconsumption=...) # <-- format
tasksList = [Task(
    str(taskId), taskEq, 
    processingtime=procTimes.get(str(taskId)), 
    electricityconsumption=eleCon.get(str(taskId))    
) for taskId, taskEq in enumerate(equipments, 1)]

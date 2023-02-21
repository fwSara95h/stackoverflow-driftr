---
title: "Creating an instance of class using lists and dictionaries"
site: stackoverflow
question_id: 75520411
url: https://stackoverflow.com/q/75520411
asked: 2023-02-21T12:16:55Z
asked_by: "Margi Shah"
asked_by_url: https://stackoverflow.com/users/19551188
last_edited: never
tags: [python, list, dictionary, class, object]
score: -1
views_at_snapshot: 69
answer_count: 1
accepted_answer_id: 75524347
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 17804fc7b7d2282affc50f090d3d28530acbb451bc6241ae09899a5e3ca7dcb2
---

# Creating an instance of class using lists and dictionaries

Asked by [Margi Shah](https://stackoverflow.com/users/19551188) on Stack Overflow, <https://stackoverflow.com/q/75520411>, 2023-02-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working with classes and functions in python where I am facing some issues. I will explain step by step what I am trying to do:

1. I have a list of tasks to be accomplished. e.g:
   1:EAF Processing task for heat 1
   2:EAF Processing task for heat 2

Here, I have tried to create a id.e.g :
   
```
self.id=id
```
2. Each equipment is associated with list of equipment from the list of equipments.I have tried to implement it via :


```
equipment = ['EAF1','EAF2','AOD1', 'AOD2','LF1','LF2']
self.equipment=equipment
```
3. Each id(task) will have the processing time.e.g:
{"1" :80.0
 "2" :40.0}
I am unsure how to implement such logic?

4. Each task will have electricity consumption. e.g:
{"1" :34.0
 "2" :49.0}

I have tried to implement the class like:


```
class Tasks():
    def __init__(self,equipment,id,**kwargs,processingtime,electricityconsumption):
        self.equipment=equipment
        self.id=id
        for key,value in kwargs.iteritems():
            setattr(self,key,value)
        self.processingtime=processingtime
        self.electricityconsumtption=electricityconsumption
```
However, I am not completely convinced and it throws an error. 

It would be great if someone helps me in creating this logic of the class object.

I tried to create the instance of class using available data. But however I am somehow not able to interpret the definition of the object and did not know how to create the instances using these data.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Abdul Aziz Barkat](https://stackoverflow.com/users/14991864)** (2023-02-21): There shouldn't be any arguments after `**kwargs`, it should be the last argument. Also why are you even using it there? You already seem to be taking all the arguments you say you need to store.
- **[Margi Shah](https://stackoverflow.com/users/19551188)** (2023-02-21): @AbdulAzizBarkat, Yes correct. I have processing times & electricity consumption as a dictionary. Can I use them as the instances?
- **[Abdul Aziz Barkat](https://stackoverflow.com/users/14991864)** (2023-02-21): Just pass the correct value in while instantiating `Tasks`? You shouldn't pass the entire dictionary in, given that it has information about the other tasks too.
- **me** (2023-02-21): [When you create a new `Tasks` object] how are you calling `Tasks`? You can just have *`def __init__(self,equipment,id,**kwargs)`* and call it like `Tasks(some_equipment, some_id, attr_x=value_x, processingtime={"1" :80.0 "2" :40.0}, electricityconsumption={"1" :34.0 "2" :49.0})` and so on and it'll do what I think you want it to [you'll no longer need the last 2 lines in *`__init__`*]
- **[Margi Shah](https://stackoverflow.com/users/19551188)** (2023-02-21): @Driftr95, I have different processing times & electricity consumption for each id. How do I call that?
- **[Alias Cartellano](https://stackoverflow.com/users/16653700)** (2023-02-21): Make the object using the values from your dictionary using `Task(equipment, id, processingTimeDictionary.get(i), electricityConsumptionDictionary.get(i))`.
- **me** (2023-02-21): @MargiShah I've added an answer based on my assumptions, but if that's not what you're going for, please clarify by including a sample of your current data and what data you would want one `Tasks` object to contain

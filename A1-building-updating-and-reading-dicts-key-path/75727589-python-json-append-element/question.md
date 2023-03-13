---
title: "Python - Json: append element"
site: stackoverflow
question_id: 75727589
url: https://stackoverflow.com/q/75727589
asked: 2023-03-13T22:48:51Z
asked_by: "JonesDK"
asked_by_url: https://stackoverflow.com/users/21392387
last_edited: never
tags: [python, json, dictionary]
score: 0
views_at_snapshot: 122
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 15340c0f5a7ce52d5c78eb97ab9e4097eed5548dea2eba43a54125f6d65866b1
---

# Python - Json: append element

Asked by [JonesDK](https://stackoverflow.com/users/21392387) on Stack Overflow, <https://stackoverflow.com/q/75727589>, 2023-03-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to add a element to a json file, but i can add it to the level 4 of the file (LogDetails), however, it works for level 3 (Logs).

I'm all new to Python and i can seem to figure this out, can someone help? :-)


```
import json

#Normaly loaded from a json file, but inserted here to make the exampel more simple - i hope :)
jsonfile = {
	"Job": {
		"id": "",
		"LoggingData": {
			"Logs":[{
				"LogDetails": [{
                }]
			}]
		}
	}
}

def AddToJson(new_data,jsondata=""):
    print("jsondata type:", type(jsondata))
    if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"]:
        print("Joy - Found LogDetails") 
        jsondata["Job"]["LoggingData"]["Logs"]["LogDetails"].append(new_data)
    else:
        for sub in jsondata["Job"]["LoggingData"]["Logs"]:
            print("Value of sub:"+str(sub))
        jsondata["Job"]["LoggingData"]["Logs"].append(new_data)

    return(jsondata)

DataToAddToExistingJson = {"Step id": 1, "Step name": "Test"}

NewJsonfile =AddToJson(new_data=DataToAddToExistingJson,jsondata=jsonfile)
print ("NewJsonfile type:",type(NewJsonfile))
print ("NewJsonfile value:",NewJsonfile)
```

Output:

```
jsondata type: <class 'dict'>
Value of sub:{'LogDetails': [{}]}
NewJsonfile type: <class 'dict'>
NewJsonfile value: {'Job': {'id': '', 'LoggingData': {'Logs': [{'LogDetails': [{}]}, {'Step id': 1, 'Step name': 'Test'}]}}}
PS C:\> 

```



I would have expected it to find the lowest level of the dict named LogDetails, but it seems to ignore it.

Wanted output for first run:
```
{
	"Job": {
		"id": "",
		"LoggingData": {
			"Logs": [{
				"LogDetails": [{
					"Step id": 1,
					"Step name": "Test"
				}]
			}]
		}
	}
}
```

and the afterwards something like this:

```
{
	"Job": {
		"id": "",
		"LoggingData": {
			"Logs": [{
				"LogDetails": [{
					"Step id": 1,
					"Step name": "Test"
				}, {
					"Step id": 2,
					"Step name": "Test"
				}]
			}]
		}
	}
}
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Mike 'Pomax' Kamermans](https://stackoverflow.com/users/740553)** (2023-03-13): Don't work with json. Work with data. Then turn that data _into_ JSON only at the very last possible moment where you need a string.

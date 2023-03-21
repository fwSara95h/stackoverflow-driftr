---
title: "Pull data from a json and create an excel file with the data"
site: stackoverflow
question_id: 75805680
url: https://stackoverflow.com/q/75805680
asked: 2023-03-21T19:36:39Z
asked_by: "Daniel Crain"
asked_by_url: https://stackoverflow.com/users/11052850
last_edited: 2023-03-27T06:30:37Z
last_editor: "braX"
last_editor_url: https://stackoverflow.com/users/8422953
tags: [python, json, excel, xlwt]
score: -1
views_at_snapshot: 1353
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6977bbbb09893b8d9024e924b501fd377bbf69a70284f3f636a5e51cf0d51b9b
---

# Pull data from a json and create an excel file with the data

Asked by [Daniel Crain](https://stackoverflow.com/users/11052850) on Stack Overflow, <https://stackoverflow.com/q/75805680>, 2023-03-21, last edited 2023-03-27 by [braX](https://stackoverflow.com/users/8422953). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to write a python script to:
1. Grab a JSON file.
2. Pull specific header from the json file. (couldn't figure this out)
3. Create the headers in the excel file as columns. 
4. Parse through the json and put the data in the appropriate column.

I'm fairly new and struggling to get it to work.

```
import json
import xlwt
# Workbook is created
wb = xlwt.Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
# open json file and store it in data variable
with open('input.json') as f:
    data = json.load(f)
# write the column names in the excel sheet
sheet1.write(0, 0, 'Name')
sheet1.write(0, 1, 'Schedule')
sheet1.write(0, 2, 'Time Window')
sheet1.write(0, 3, 'Type')
sheet1.write(0, 4, 'Tiers')
# iterate over the data and write it to the excel file
row = 1;
for item in data:
#write each value to the corresponding column
    sheet1.write(row, 0, item['Name'])
    sheet1.write(row, 1, item['Schedule'])
    sheet1.write(row, 2, item['Time Window'])
    sheet1.write(row, 3, item['Type'])
    sheet1.write(row, 4, item['Tiers'])
    row += 1;
#save the file
wb.save('data_converted_to_excel.xls')
```

JSON Example
```
{
  "name": "PLACEHOLDER",
  "description": "Health Rule Export",
  "version": 1,
  "healthRuleMembers": [
    {
      "model": {
        "id": 123,
        "name": "PLACEHOLDER",
        "enabled": true,
        "useDataFromLastNMinutes": 30,
        "waitTimeAfterViolation": 30,
        "scheduleName": "Always",
        "affects": {
          "affectedEntityType": "TIER_NODE_HARDWARE",
          "affectedEntities": {
            "tierOrNode": "NODE_AFFECTED_ENTITIES",
            "typeofNode": "DOT_NET_NODES",
            "affectedNodes": {
              "affectedNodeScope": "ALL_NODES"
            }
          }
        },
        "evalCriterias": {
          "criticalCriteria": {
            "conditionAggregationType": "ALL",
            "conditionExpression": null,
            "conditions": [
              {
                "name": "PLACEHOLDER",
                "shortName": null,
                "evaluateToTrueOnNoData": false,
                "evalDetail": {
                  "evalDetailType": "SINGLE_METRIC",
                  "metricAggregateFunction": "VALUE",
                  "metricPath": "PLACEHOLDER",
                  "metricEvalDetail": {
                    "metricEvalDetailType": "SPECIFIC_TYPE",
                    "compareCondition": "GREATER_THAN_SPECIFIC_VALUE",
                    "compareValue": 75
                  }
                },
                "triggerEnabled": false,
                "minimumTriggers": 0
              }
            ],
            "evalMatchingCriteria": null
          },
          "warningCriteria": {
            "conditionAggregationType": "ALL",
            "conditionExpression": null,
            "conditions": [
              {
                "name": "PLACEHOLDER",
                "shortName": null,
                "evaluateToTrueOnNoData": false,
                "evalDetail": {
                  "evalDetailType": "SINGLE_METRIC",
                  "metricAggregateFunction": "VALUE",
                  "metricPath": "PLACEHOLDER",
                  "metricEvalDetail": {
                    "metricEvalDetailType": "SPECIFIC_TYPE",
                    "compareCondition": "GREATER_THAN_SPECIFIC_VALUE",
                    "compareValue": 50
                  }
                },
                "triggerEnabled": false,
                "minimumTriggers": 0
              }
            ],
            "evalMatchingCriteria": null
          }
        }
      },
      "memberType": "HEALTH_RULE"
    },
```


I tried use what my friend said to use
item = json.loads(item) 
but haven't been able to get it to work.

I'm a beginner. Sorry!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2023-03-21): It is hard to help without seeing a sample json data but look at using [pandas.json_normalize](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html), which will create a `pandas.DataFrame` then you can do [to_excel()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
- **[Daniel Crain](https://stackoverflow.com/users/11052850)** (2023-03-21): I will try this. Thanks Chris! I will also update with an example of the json, I just have to redact the data.
- **[Daniel Crain](https://stackoverflow.com/users/11052850)** (2023-03-21): Added the JSON. I need to convert these alerting rules into an excel file and I figured Python was the best way to go about this. I don't need all of it pulled, just a few core sections and dump the rest into a json column.
- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2023-03-21): Thank you for adding the sample data. What "core sections" do you need under `healthRuleMembers`?
- **[Daniel Crain](https://stackoverflow.com/users/11052850)** (2023-03-21): Name, Schedule, Time window, Type, Tiers, JSON. Thanks for being willing to help w/ this!
- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2023-03-21): What keys in the json file do those headings belong to: `model.name`, `model.scheduleName`, `model.waitTimeAfterViolation`? Does the following get you close -- `import pandas as pd; pd.json_normalize(data, 'healthRuleMembers').to_excel('test.xlsx', index=False)` where data is how you are currently opening the file - `data = json.load(f)`
- **[Daniel Crain](https://stackoverflow.com/users/11052850)** (2023-03-21): model.name = name, model.scheduleName = schedule, model.waitTimeAfterViolation = Time Window. I forgot to clarify that, my bad! Also, yes, this is indeed proving to be more fruitful! Would it be easier to just pull it all and create a column for each?
- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2023-03-21): Based on the sample data, it is probably easiest to pull everything: `df = pd.json_normalize(data, 'healthRuleMembers')` and then just keep the columns you want -- `df[['model.id', 'model.name', 'model.scheduleName', ... ]].to_excel('test_file.xlsx', index=False)`
- **[It_is_Chris](https://stackoverflow.com/users/9177877)** (2023-03-21): Glad I could help. Good luck on the project.

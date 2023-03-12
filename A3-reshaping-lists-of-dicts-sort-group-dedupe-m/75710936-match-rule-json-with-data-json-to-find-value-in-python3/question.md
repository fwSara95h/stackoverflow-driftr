---
title: "Match rule json with data json to find value in python3"
site: stackoverflow
question_id: 75710936
url: https://stackoverflow.com/q/75710936
asked: 2023-03-12T03:39:39Z
asked_by: "Sudipta Dhara"
asked_by_url: https://stackoverflow.com/users/2947218
last_edited: 2023-03-13T08:54:46Z
last_editor: "JIST"
last_editor_url: https://stackoverflow.com/users/20266647
tags: [python, json, python-3.x]
score: 0
views_at_snapshot: 306
answer_count: 1
accepted_answer_id: 75716929
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7595dfa692e1e8fa671847cae53a94550cb71d90383ccf21528b05645b49efee
---

# Match rule json with data json to find value in python3

Asked by [Sudipta Dhara](https://stackoverflow.com/users/2947218) on Stack Overflow, <https://stackoverflow.com/q/75710936>, 2023-03-12, last edited 2023-03-13 by [JIST](https://stackoverflow.com/users/20266647). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

**PYTHON3**
## Need to Find articleid by applying rules on data ##
Given a set of rules in JSON format, which includes article IDs and corresponding properties rules.

Eg: `rules.json`
```
{
  "rules": [
    {
      "articleId": "art1",
      "properties_rule": [
        {
          "condition": "EQ",
          "logicalOperator": "AND",
          "propertyId": 487,
          "value": "aaaa"
        },
        {
          "condition": "EQ",
          "logicalOperator": "",
          "propertyId": 487,
          "value": "zzzz"
        }
      ],
      
    },
    {
      "articleId": "art2",
      "properties_rule": [
        {
          "condition": "GTE",
          "logicalOperator": "AND",
          "propertyId": 487,
          "value": "bbbb"
        },
        {
          "condition": "LTE",
          "logicalOperator": "",
          "propertyId": 487,
          "value": "eeee"
        }
      ],
      
    },
    {
      "articleId": "art3",
      "properties_rule": [
        {
          "condition": "GTE",
          "logicalOperator": "",
          "propertyId": 487,
          "value": "ffff"
        }
      ],
      
    }
  ]
}
```

Qs well as a set of data in JSON format, which includes values for certain properties. 
Like Eg: `data.json`

```
{
  "data": {
    "1": {
      "properties_values": [
        {
          "value": {
            "property_id": 487,
            "property_value": "aaaa",
            "response_id": 1
          }
        }
      ]
    },
    "2": {
      "properties_values": [
        {
          "value": {
            "property_id": 487,
            "property_value": "bbbb",
            "response_id": 2
          }
        }
      ]
    },
    "3": {
      "properties_values": [
        {
          "value": {
            "property_id": 487,
            "property_value": "eeee",
            "response_id": 3
          }
        }
      ]
    }
  }
}
```

the task is to apply the rules on the data and determine the article ID that matches the rules.

How can we use the provided rules and data JSON to determine the corresponding "articleId" for each entry in the "data" JSON, based on the conditions specified in the "properties_rule" arrays of the rules JSON? The "property_id" field in the "data" JSON corresponds to the "propertyId" field in the "rules" JSON, and the "property_value" field in the "data" JSON corresponds to the "value" field in the "rules" JSON.

-----------------------------------------------------------------------
## Tried this To Solve this But didn't liked so many for loops ##
To determine the corresponding "articleId" for each entry in the "data" JSON based on the conditions specified in the "properties_rule" arrays of the rules JSON, we can follow the following steps in Python:

1. Load the rules and data JSON into Python dictionaries using the json module.
2. Loop through each entry in the "data" JSON.
3. For each entry, loop through the "rules" JSON to find a matching article ID based on the conditions specified in the "properties_rule" arrays.
4. For each rule, loop through the "properties_values" array in the data entry to find a matching property ID.
5. If a matching property ID is found, check if the property value meets the condition specified in the rule. If it does not meet the condition, move on to the next rule.
6. If all conditions are met, return the article ID associated with the rule.
7. If no matching article ID is found, return a default value or raise an error.

Here is sample code that implements this logic:

```
import json

# Load the rules and data JSON files into memory
with open('rules.json', 'r') as f:
    rules_data = json.load(f)
rules = rules_data['rules']

with open('data.json', 'r') as f:
    data = json.load(f)
data = data['data']

# Loop through each rule and check if it matches the data
for rule in rules:
    properties_rule = rule['properties_rule']
    articleId = rule['articleId']
    
    # Check if all the conditions in the properties_rule array are satisfied
    matched = True
    for prop_rule in properties_rule:
        propertyId = prop_rule['propertyId']
        value = prop_rule['value']
        condition = prop_rule['condition']
        
        # Check if any of the survey responses match the condition
        response_matched = False
        for key, value_dict in data.items():
            properties_value = value_dict['properties_value']
            for prop_value in properties_value:
                survey_response = prop_value['survey_response']
                if survey_response['property_id'] == propertyId:
                    property_value = survey_response['property_value']
                    if condition == 'EQ' and property_value == value:
                        response_matched = True
                    elif condition == 'GTE' and property_value >= value:
                        response_matched = True
                    elif condition == 'LTE' and property_value <= value:
                        response_matched = True
        # If none of the survey responses match the condition, set matched to False
        if not response_matched:
            matched = False
            break
    
    # If all the conditions are satisfied, return the articleId of that rule
    if matched:
        print("Article ID: ", articleId)
        break

# If none of the rules match the data, return a default articleId
if not matched:
    print("Default Article ID")
```


-----------------------------------------------------------------------
## But Looking for effecient way of doing it. Don't want so many for loops ##

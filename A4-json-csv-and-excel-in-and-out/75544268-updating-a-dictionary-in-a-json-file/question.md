---
title: "Updating a dictionary in a JSON File"
site: stackoverflow
question_id: 75544268
url: https://stackoverflow.com/q/75544268
asked: 2023-02-23T11:34:16Z
asked_by: "Trqzy"
asked_by_url: https://stackoverflow.com/users/15612849
last_edited: 2023-02-23T11:54:26Z
tags: [python, json, dictionary]
score: 0
views_at_snapshot: 98
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ec55f390ed3566f590fd88b70bcdc1f1cf6bdd7891a2198db9d328f8feb2376b
---

# Updating a dictionary in a JSON File

Asked by [Trqzy](https://stackoverflow.com/users/15612849) on Stack Overflow, <https://stackoverflow.com/q/75544268>, 2023-02-23, last edited 2023-02-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Trying to update a certain dictionary in a json file but unable to do so as it just adds a new dictionary to the database rather than being under the dictionary.
An example, of what I'm trying to achieve is:

Before running the function the database looks like:

    {
        "account_details": [
            {
                "Username": "TestingUsername",
                "Password": "232Pass",
                "Email": "TestingEmail@outlook.com",
                "Token": "18973871HIA"
            }
        ]
    }

After running the function this is what the database looks like:

    {
        "account_details": [
            {
                "Username": "TestingUsername",
                "Password": "232Pass",
                "Email": "TestingEmail@outlook.com",
                "Token": "18973871HIA"
            }
        ]
    }{
        "Username": "TestingUsername",
        "Password": "232Pass",
        "Email": "TestingEmail@outlook.com",
        "Token": "18973871HIA",
        "Details": {
            "Preset1": {
                "Username": "TestingUsername",
                "Password": "TestingPassword3",
                "URL": "TestingURL.com:"
            }
        }
    }

The functions, function is to take in the Presetname (TestingPreset39), under the Details dictionary, which then includes the Username (Testing_username) , Password (TestingPresetPassword) & Url (preset.com). 

However, what I want it to look like is:

    {
        "account_details": [
            {
                "Username": "ComputingCourse32",
                "Password": "NoNUmbers",
                "Email": "computingcw@cwl.com",
                "Token": "4L8PWWRFYL",
                "Testing": "Testing",
                "Details": {
                    "Preset1": {
                        "Username": "Username1",
                        "Password": "Password1",
                        "URL": "http://testing.cwl.com"
                    }
                }
            },

I've tried to convert the database into a list as a way to append to the list then putting it in the database:

       with open("testaccount.json", "r+") as file:
            data = json.load(file)
            for record in data["account_details"]:
                if record["Username"] == username:
                    if type(record) is dict:
                        data = [record]
                        # data['specific_dict'].append(new_dict)
    
                        data.append ({
                            "Details" : {
                            "Preset1":{
                            "Username": "TestingUsername",
                            "Password": "TestingPassword",
                            "URL": "TestingURL.com"
                            }
                            }
                        })
                       
                        print(data)

Also, I've tried to use the update() function:

    with open("testaccount.json", "r+") as file:
        data = json.load(file)
        for record in data["account_details"]:
            if record["Username"] == "TestingUsername":
                new_data = {"Details":{
                    "Preset1":{
                    "Username": "TestingUsername",
                    "Password": "TestingPassword3",
                    "URL": "TestingURL.com:"
                    }
                }}
                record.update(new_data)
                print(record)

Though both ways put the new data in the database neither ways actually add it under the dictionary.

[![enter image description here](https://i.sstatic.net/p09Js.png)](https://i.sstatic.net/p09Js.png)


  [1]: https://i.sstatic.net/TsbmT.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[quamrana](https://stackoverflow.com/users/4834)** (2023-02-23): Why does the `after` image look exactly like the `before` image? Why are you posting images of text when you could have cut and pasted the text itself into your question?
- **[ivvija](https://stackoverflow.com/users/10513287)** (2023-02-23): When opening with `r+` your pointer is at the beginning. `json.load` moves it to the end, so `json.dump` appends to the file. Properly update the records in `data` and overwrite the file.
- **[Trqzy](https://stackoverflow.com/users/15612849)** (2023-02-23): @ivvija Wouldn't this overwrite everything in the database?  I like the idea of overwriting but I would only want to overwrite a specific dictionary any idea on how this would be done?
- **[quamrana](https://stackoverflow.com/users/4834)** (2023-02-23): With `json` format data in a file, you cannot reliably overwrite parts of the file. You should read the entire file, make changes as python objects, and finally write the entire file back.

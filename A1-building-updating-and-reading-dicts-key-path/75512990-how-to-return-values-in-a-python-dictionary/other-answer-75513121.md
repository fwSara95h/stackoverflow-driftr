---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
answer_id: 75513121
url: https://stackoverflow.com/a/75513121
author: "Ruler"
author_url: https://stackoverflow.com/users/20360197
posted: 2023-02-20T18:49:50Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c911334757415e14e5ac30461f8d335c9b5cce8be22d1eb4aca7577359c42d53
role: another answer on the same question, kept as context; not my work
---

# Answer by [Ruler](https://stackoverflow.com/users/20360197) — 2023-02-20

Posted on Stack Overflow, <https://stackoverflow.com/a/75513121>, 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could do achieve this by first using the .get() method, then filtering them out by their specific variables.

For example, you could use the following snippet as an overview of how to do this:
    
    # Initial dictionary
    dict = {
        'Tim': ['red', 'pizza', 'soda'],
        'Jake': ['green', 'burger', 'juice'],
        'Mary': ['blue', 'salad', 'water']
    }
    
    # Check input for name
    name = input("Enter a name:")
    
    # Returns values for inputted name in dictionary
    name_values_in_dict = dict.get(name)

    # If it is none, return that it could not be found.
    if name_values_in_dict is None:
         print("Name could not be found in dictionary.")
    
    # If it is found, store in variables and print them out.
    favoriteColor = name_values_in_dict[0]
    favoriteFood = name_values_in_dict[1]
    favoriteDrink = name_values_in_dict[2]

    print(f'Favorite color is: {favoriteColor}, favorite food is: {favoriteFood}, and favorite drink is: {favoriteDrink}')

---
title: "Filter strings in a list for for numbers at specific index"
site: stackoverflow
question_id: 77115962
url: https://stackoverflow.com/q/77115962
asked: 2023-09-16T00:56:31Z
asked_by: "Jackie Marie"
asked_by_url: https://stackoverflow.com/users/22572344
last_edited: 2023-09-16T01:58:20Z
tags: [python, string, list, integer]
score: 0
views_at_snapshot: 93
answer_count: 1
accepted_answer_id: 77116197
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0ce91b86795be9c2b6bac3c12ec29236370131169dcc88e66f5391d27741260c
---

# Filter strings in a list for for numbers at specific index

Asked by [Jackie Marie](https://stackoverflow.com/users/22572344) on Stack Overflow, <https://stackoverflow.com/q/77115962>, 2023-09-16, last edited 2023-09-16. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am filtering through a text project of rearranging addresses from other texts. I have a list I am calling rest. Each list is a different address and description on a new line of text.

I want to copy all words from the first index, up until the zip code, but the text words have some house numbers as the first index, and I want to stop from the list not just at any numeric value, but specially one that is a number and not the first index. How would I iterate through these lists?

    rest = ["town name", "state", "98420", "description"],["222", "street", "state", "98420", "description"], ["town name", "state", "94820", "description"]
    
    addr = []
    for i in rest:
        addr.append(rest[i])
        if len(i) == 5:
         # append and end list

These are just examples, my real lists look like
rest = ['lilypad', 'CA', '94820', 'beautiful', 'green', 'city'], ['1800', 'turtle', 'Ave', 'CA', '94820', 'tropical']

and I want the list to be addr = ['lilypad,' 'CA', 94820'], ['1800', 'turtle', 'Ave', 'CA', '94820']

I am filtering through several lines of addresses, but the numbers and names are mixed up.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jackie Marie](https://stackoverflow.com/users/22572344)** (2023-09-16): I guess I can iterate through the lists for a numeric value and string must be 5 characters in length
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-09-16): This python code has indentation errors.  What is the point of the indented list on line 2 of the code?  It is not assigned to any variable.  It's just hanging out all by itself.  Why is `for i in rest:` indented?  etc etc.  Please fix these indentation errors so that we can actually **run** this code.
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-09-16): Also, none of the data in the list is numeric, so `if i.isnumeric()` will never be true...
- **[Jackie Marie](https://stackoverflow.com/users/22572344)** (2023-09-16): I edited it to show what my list of strings look like.
- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2023-09-16): "How would I iterate through these lists?" well, apparently you already know how to get at the list, and you already know how to write a loop, so it's not clear to me what the problem is. Do you know how to skip the first element when looping over them? Or else where exactly do you get stuck?

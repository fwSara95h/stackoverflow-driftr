---
title: "How can I simplify my dict statements into one statement?"
site: stackoverflow
question_id: 75499914
url: https://stackoverflow.com/q/75499914
asked: 2023-02-19T11:47:17Z
asked_by: "beachDXD"
asked_by_url: https://stackoverflow.com/users/21239366
last_edited: never
tags: [python, dictionary]
score: -1
views_at_snapshot: 58
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 75c57657aec2090dca1316c4e3f09c299f6ffda2b440283b8a5011be7d595539
---

# How can I simplify my dict statements into one statement?

Asked by [beachDXD](https://stackoverflow.com/users/21239366) on Stack Overflow, <https://stackoverflow.com/q/75499914>, 2023-02-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to combine my two dictionaries to read easier and simplify my code but every time I merge them I keep getting errors or the items not properly reading. 

    rooms = {
    'Stable': {'West': 'Foyer'},
    'Foyer': {'South': 'Great Hall'},
    'Great Hall': {'South': 'Dining Room', 'East': 'Study', 'West': 'Balcony’, ‘North’: ‘Foyer'},
    'Study': {'North': 'Library', 'West': 'Great Hall'},
    'Dining Room': {'North': 'Great Hall', 'East': 'Kitchen'},
    'Library': {'South': 'Study'},
    'Kitchen': {'West': 'Dining Room'},
    'Balcony': {'East': 'Great Hall'},
    }
    items = {
    'Foyer': 'Shield',
    'Great Hall': 'Sword',
    'Study': 'Armor',
    'Library': 'Spell Book',
    'Dining Room': 'Helmet',
    'Kitchen': 'Cooked Chicken',
    'Balcony': 'Dark Knight',

    }

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[constantstranger](https://stackoverflow.com/users/18135454)** (2023-02-19): what do you want the output to look like?
- **[beachDXD](https://stackoverflow.com/users/21239366)** (2023-02-19): The output is part of the text based game i am working on for my project in class. I was given feedback that i needed to combine the two dictionaries for easier readability. When I combine the two dictionaries into this 'Great Hall': {'South': 'Dining Room', 'item': 'Helmet', 'East': 'Study', 'item': 'Armor', 'West': 'Balcony’, 'item': 'Dark Knight', ‘North’: ‘Foyer'}, I get errors or the item doesn't prompt when executing the code. I would be happy to send you the whole thing if it is easier to see my entire code. @constantstranger
- **[roganjosh](https://stackoverflow.com/users/4799172)** (2023-02-19): It doesn't make sense to combine them; there's a clear separation of "things" between the two
- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-02-19): You can do `rooms, items = {..}, {..}`, but that will not be easier to read.
- **[roganjosh](https://stackoverflow.com/users/4799172)** (2023-02-19): The structure you presented in your comment doesn't make sense because you have to know the direction in the first place. What if I wanted to go North from the Stable? That's a KeyError that I can't know about as a player
- **[roganjosh](https://stackoverflow.com/users/4799172)** (2023-02-19): Actually, on further reading of your proposed structure in the comment, you've avoided a big trap which would lead to massive duplication. Perhaps without realising it, you've used normalisation on your data - I suggest you go back and tell your instructor that you've used [normalisation](https://en.wikipedia.org/wiki/Database_normalization) in this case
- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-02-19): @roganjosh The dict in their comment doesn't even work, you can't have multiple `'item'` keys in the same dict. They'd need `NotStr('item')` for that (who knew that that thing would become useful so quickly :-)
- **[roganjosh](https://stackoverflow.com/users/4799172)** (2023-02-19): @KellyBundy Oh man, `NotStr` is already haunting me? :P There are problems with this setup for sure, but I really disagree with the advice that's been given.

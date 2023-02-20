---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
answer_id: 75513179
url: https://stackoverflow.com/a/75513179
author: "jackal"
author_url: https://stackoverflow.com/users/17580381
posted: 2023-02-20T18:56:48Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aed9568b01f4bf174240e322173780f1286064ffedfb43b0fb0fbd8c87c93827
role: another answer on the same question, kept as context; not my work
---

# Answer by [jackal](https://stackoverflow.com/users/17580381) — 2023-02-20

Posted on Stack Overflow, <https://stackoverflow.com/a/75513179>, 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Using a list where each element implicitly corresponds to some type (in this case colour, food, drink) is rarely a good idea. Much better to use a class. Then, with judicious variable naming, it's quite obvious what each value means. Something like this:

    class Favourites:
        def __init__(self, food, colour, drink):
            self._food = food
            self._colour = colour
            self._drink = drink
        def __repr__(self):
            return f'{self._food=} {self._colour=} {self._drink=}'
    
    database = dict()
    
    while (name := input('Name: ')):
        food = input('Food: ')
        colour = input('Colour: ')
        drink = input('Drink: ')
        database[name] = Favourites(food, colour, drink)
    
    print(database)

Now we can enter "favourites" for multiple people. Just hit return (empty input) to break the loop and see what's been constructed

---
title: "Having trouble adding both one and 2 word dict key values to inventory list in my text based game"
site: stackoverflow
question_id: 75430676
url: https://stackoverflow.com/q/75430676
asked: 2023-02-12T22:53:27Z
asked_by: "zeroMana"
asked_by_url: https://stackoverflow.com/users/21199447
last_edited: 2023-02-12T23:02:19Z
last_editor: "Michael M."
last_editor_url: https://stackoverflow.com/users/13376511
tags: [python, python-3.x, dictionary, inventory, text-based]
score: 0
views_at_snapshot: 44
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d3955ac53100540e22a3fffa24947944406d9bbe1cf509bda8947da53eda103f
---

# Having trouble adding both one and 2 word dict key values to inventory list in my text based game

Asked by [zeroMana](https://stackoverflow.com/users/21199447) on Stack Overflow, <https://stackoverflow.com/q/75430676>, 2023-02-12, last edited 2023-02-12 by [Michael M.](https://stackoverflow.com/users/13376511). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So far I have been able to add either one-word values or 2-word values but not both. For example, I want to go to one location and add a skull to my inventory, then move to another location and add an energy potion to my inventory. With my current code, I can add the energy potion by using `.split(maxsplit=1)` or `.split(' ', 1)`. That was to solve the issue of not being able to add a value with 2 words. But this seems to prevent adding values with one word to the inventory.


```
while True:
    instructions()
    player_status(rooms, current_room, inventory)
    time.sleep(0.5)

    # sets up user command to move player between rooms.
    command = input('\nWhat do you want to do?\n>').title().strip()
    if command in rooms[current_room]:
        current_room = rooms[current_room][command]
        time.sleep(0.5)

    # command to add item to inventory and remove it from dict.
    elif command.lower().split()[0] == 'get':
        obj = command.lower().split(maxsplit=1)[1]
        if obj in rooms[current_room]['item']:
            del rooms[current_room]['item']
            inventory.append(obj)
        else:
            print("I don't see that here.")

    # a command to quit the game.
    elif command.lower() in ('q', 'quit'):
        time.sleep(0.5)
        print('\nThanks for playing.')
        break

    # if player inputs an invalid command.
    else:
        time.sleep(0.5)
        print('\nYou can\'t go that way!')
```


Here is an example of the output:

```
You are at occult bookstore.
There is a Skull
You have: ['energy potion']

What do you want to do?
>get skull
I don't see that here.
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Galo do Leste](https://stackoverflow.com/users/2794417)** (2023-02-12): Seems to me that you have a 'Skull' in the room, but you are trying to pick up a 'skull'. `obj = command.lower().split(maxsplit=1)[1]` converts everything to lower case. But your script prompts with `There is a Skull`, suggesting it is stored with a capital in your room inventory.
- **[zeroMana](https://stackoverflow.com/users/21199447)** (2023-02-12): You are a lifesaver! I probably never would have caught that. Thanks. Everything works now.

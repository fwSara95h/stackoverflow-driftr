---
title: "How to search for a key that is a float using an int that the float would round to"
site: stackoverflow
question_id: 75717254
url: https://stackoverflow.com/q/75717254
asked: 2023-03-13T00:48:27Z
asked_by: "Eutopia"
asked_by_url: https://stackoverflow.com/users/18457417
last_edited: 2023-03-13T20:10:05Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary, floating-point, integer]
score: -1
views_at_snapshot: 102
answer_count: 1
accepted_answer_id: 75728342
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0918e2e768cfd1cfe971c10fb203f5e9805ce88feb426eee6289762002cf2918
---

# How to search for a key that is a float using an int that the float would round to

Asked by [Eutopia](https://stackoverflow.com/users/18457417) on Stack Overflow, <https://stackoverflow.com/q/75717254>, 2023-03-13, last edited 2023-03-13 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have two lists that represent the x and y coordinates as a plane, and each point on the plane has a random number assigned to it which i use as a key to search for the coordinates, the problem is i need there to be a chance that the random number assigned to a point is a duplicate so i used float but now i need to search through the dictionaries using an int as the key to see if that number exists and what point it is assigned to. So essentially I'm wondering if it's possible to search for the rounded version of a key for example if the key is 10.3 i need to find it using an int equal to 10.


```
x_amount = int(input("Height of room: "))
y_amount = int(input("Width of room: "))
# Asks for height and width of plane

Room_Total = x_amount * y_amount
numbers = []
length = len(str(Room_Total)) + 1
x_values = {}
y_values = {}
create_number = y_amount

def num_find(num):
    y_coord = y_values[num]
    x_coord = x_values[num]
    # Here is where i want to search for the coordinates using an int

for num in range(1, (y_amount + 1)):
    for n in range(1, (x_amount + 1)):
        number = 1
        while number != 0:
            number = random.uniform(1, Room_Total)
            if number not in numbers:
                numbers.append(round(number))
                x_values[number] = num
                y_values[number] = n
                number = 0
# Randomly generates a number for every place in the grid
      
plane = input("Want to see the plane? y/n ")
if plane == "y":
    for i in numbers:
        num_gap = length - len(str(i))
        create_number = create_number - 1
        if create_number == -1:
            print("")
            create_number = y_amount - 1
            print(i,end="  ")
            for num in range(1, num_gap):
                print(" ", end="")
       else:
           print(i,end="  ")
           for num in range(1, num_gap):
               print(" ", end="")
# Prints grid if the user wants it (So that if the grid is 100 by 100 for example it doesn't print it)

```
I searched for similar problems that have an answer but haven't quite found anything that applies to this situation and haven't been sure what else to try.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jarmod](https://stackoverflow.com/users/271415)** (2023-03-13): See PEP8 recommendation for [indentation](https://peps.python.org/pep-0008/#indentation). You have 1, 2, and 4. Use 4.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-13): This code doesn't run. You're going to want to make it work, then copy the whole working code. Also you must provide the input and expected output.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-13): Well, work up until the error you want help with, not some unrelated typo.
- **[Eutopia](https://stackoverflow.com/users/18457417)** (2023-03-13): Sorry i think that's because i accidentally put some text in as code it should just fine now and the input is any two numbers (the height and width of the grid) it shouldn't matter which two numbers you input
- **[Сергей Кох](https://stackoverflow.com/users/18400908)** (2023-03-13): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
- **[Eutopia](https://stackoverflow.com/users/18457417)** (2023-03-13): Alright i tried to clarify it as much as possible, thanks for the feedback
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-13): Is this some sort of design to have duplicates that are unique? Or is your real problem how to store multiple values for a key? But no, if you want dict keys of random floats you can't have constant time lookup without looking for the exact key. You can iterate over the keys to find matches.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-13): It really sounds like an x-y problem. https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem

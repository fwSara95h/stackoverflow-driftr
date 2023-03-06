---
title: "python say isalpha() is not defined despite it being built in (I think)"
site: stackoverflow
question_id: 75655791
answer_id: 75656043
url: https://stackoverflow.com/a/75656043
author: "naimaaannnn"
author_url: https://stackoverflow.com/users/21025910
posted: 2023-03-06T21:33:06Z
last_edited: 2023-03-07T08:03:24Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0a251c3fd37c629abc7c37c9a771b644a1de2859cacdeda989b14741bf7965d8
role: another answer on the same question, kept as context; not my work
---

# Answer by [naimaaannnn](https://stackoverflow.com/users/21025910) — 2023-03-06

Posted on Stack Overflow, <https://stackoverflow.com/a/75656043>, 2023-03-06, last edited 2023-03-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

```isalpha()``` is a method for the ```str``` class which returns ```True``` if all the characters inside a string are letters and ```False``` if that's not the case. Example:
```
>>> MyString = "fwUBCEFèfewf"
>>> MyString.isalpha()
True
>>> MyOtherString = "f13bbG"
>>> MyOtherString.isalpha()
False
```

In order to separate all the letters and numbers inside the item array you need to rewrite your code like this:
```
letters = []
numbers = []

item=[1,7,-10,34,2,"a",-8]
for things in item:
    if str(things).isalpha():
        letters.append(things)
    else:
        numbers.append(things)

print(letters)
print(numbers)

# output:
# ['a']
# [1, 7, -10, 34, 2, -8]
```

You will have to do ```str(things)``` inside the conditions because the ```isalpha()``` is only a function you can use on strings and not integers. If you don't add this you will get an error saying ```AttributeError: 'int' object has no attribute 'isalpha'```.

You could also do this if you use the ```isinstance()``` function to check wether ```things``` is a string or not. You would do it like this:

```
letters = []
numbers = []

item=[1,7,-10,34,2,"a",-8]
for things in item:
    if isinstance(things, str) and things.isalpha():
        letters.append(things)
    else:
        numbers.append(things)

print(letters)
print(numbers)

# output:
# ['a']
# [1, 7, -10, 34, 2, -8]
```

Since the letters can only be strings you can check if the ```things``` is of type ```str``` with the ```isinstance()``` function. Here two conditions have to be ```True```. 


I hope that I could help you :)

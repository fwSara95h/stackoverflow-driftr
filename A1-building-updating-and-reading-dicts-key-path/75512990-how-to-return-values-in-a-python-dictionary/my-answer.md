---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
answer_id: 75528781
url: https://stackoverflow.com/a/75528781
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-22T06:00:59Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75528781/revisions
accepted: false
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8bd1e77db802c7f46cd2c406a7ad5594b2d9eabdd8f0d45252d79e8d3191d2ae
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75528781>, 2023-02-22; score 1. Text as retrieved 2026-10-12.

As others have already mentioned, it's not the best idea to name a variable `dict`, as it already means something in python, so I'll redefine it as **`favsDict`** for context in the rest of my answer.

```py
favsDict = { 'Tim': ['red', 'pizza', 'soda'],
             'Jake': ['green', 'burger', 'juice'],
             'Mary': ['blue', 'salad', 'water']    }
```

---

> *I really just don't know how to call specific values in this specific type dictionary in python*

You might like to take a look at the documentation on [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) and how to access values with keys [as well as [lists](https://docs.python.org/3/tutorial/introduction.html#lists), the values of which can be accessed with indices], but below are some examples with `favsDict`:

- <kbd>`favsDict['Jake']`</kbd> should return `['red', 'pizza', 'soda']`
- <kbd>`favsDict['Tim'][0]`</kbd> should return `'red'` 
- <kbd>`favsDict['Mary'][2]`</kbd> should return `'water'` 
- <kbd>`tim_ffood = favsDict['Tim'][1]`</kbd> should effectively be the same as `tim_ffood = 'pizza'`

---

> *How would I go about letting a user input a name and then set the contents of that person's information as values of variables in the code?*

It's common to use the built-in [`input`](https://docs.python.org/3/library/functions.html#input) function to prompt and get user input, and there are many ways to set the variables. ([View tests](https://i.sstatic.net/77qbS.gif) of the example below.)

```py
search_name = input('Please enter a name: ')
if search_name in favsDict:
    favsList = favsDict[search_name]

    # favoriteColor, favoriteFood, favoriteDrink = favsDict[search_name] # = favsList ## OR
    # favoriteColor,favoriteFood,favoriteDrink = favsList[0],favsList[1],favsList[2] ## OR

    favoriteColor = favsList[0] # favsDict[search_name][0]
    favoriteFood = favsList[1] # favsDict[search_name][1]
    favoriteDrink = favsList[2] # favsDict[search_name][2]

    for fCat, fVal in zip(['color','food','drink'], favsList): 
        print(f"\t{search_name}'s favourite {fCat} is {fVal}")
else: print(f'! Could not find any records for {repr(search_name)} !')
```

---

If you want to build `favsDict` from user input <sup>([view test][1])</sup> and you have a set number of people to add: 

```py
personsCt = 3 # how many names/people
fav_categories = ['Color', 'Food', 'Drink'] # list template for asking

favsDict = {input(f'\n[Person#{i+1}] Please Enter\n\tName: '): [
    input(f'\tFavorite {f}: ') for f in fav_categories
] for i in range(personsCt)}

print()
favsDict
```

<br>

If you want to let the user decide when to stop, you can use a `while` loop <sup>([view test][2])</sup>

```py
fav_categories = ['color', 'food', 'drink'] # list template for asking
favsDict = {} # initiate

while (pName := input(f'\n[Just press Enter to exit]\nEnter name: ')):
    fPromptr = lambda fc: input(f"\t{pName}'s favorite {fc} is: ")
    favsDict[pName] = [fPromptr(fCat) for fCat in fav_categories]

print()
favsDict
```

<sup>Btw, the [walrus operator](https://www.digitalocean.com/community/tutorials/how-to-use-assignment-expressions-in-python) `:=` only works in python 3.8 or higher; without it, you'd need *`pName=input(...)`* before and at the end of *`while pName:...`* [like this][3].</sup>

**Note that if any names are repeated, only the most recently entered data for that name will remain.**


  [1]: https://i.sstatic.net/vVsyE.png
  [2]: https://i.sstatic.net/lrdt8.png
  [3]: https://i.sstatic.net/CWd57.png

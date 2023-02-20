---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
answer_id: 75513396
url: https://stackoverflow.com/a/75513396
author: "Raydel Miranda"
author_url: https://stackoverflow.com/users/2890724
posted: 2023-02-20T19:25:08Z
last_edited: 2023-02-20T19:48:07Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4fd9fe12887186d4ad4e20225af68632930f39b46c61d674051ca2cfaaea57ac
role: another answer on the same question, kept as context; not my work
---

# Answer by [Raydel Miranda](https://stackoverflow.com/users/2890724) — 2023-02-20

Posted on Stack Overflow, <https://stackoverflow.com/a/75513396>, 2023-02-20, last edited 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Well, since you're new I will try to explain a little bit.

> First off, try to not use reserved words as variable names `dict` is a python reserved word for the type `dictionary`.

Also for user input I recomend you to read: [Basic Input, Output, and String Formatting in Python][1]


### A very high view of Dicts ...

A Python dictionary is a collection of Key-Value pairs, meaning that you have several items each with an "index" or "name" (the key) and a value (anything, in your case, lists)

So when you have:

    MyDict = {
        'Tim': ['red', 'pizza', 'soda'],
        'Jake': ['green', 'burger', 'juice'],
        'Mary': ['blue', 'salad', 'water']
    }

That means you have 3 keys, Tim, Jake, and Mary, so if you use the key `Tim` you will be accessing the value of that item which is the list: `['red', 'pizza', 'soda']` and for getting the first element of that list you could:

    tim_favorite_color = MyDict['Tim'][0]

    # Which is the same as:
    tim_favorites = MyDict['Tim']
    tim_favorite_color = tim_favourites[0] # red

### Addendum

In order to make your code more readable you could use another data structure for the list of favorites, I would suggest a [namedtuple][2].

    from collections import namedtuple
    
    FavoriteValues = namedtuple("FavoriteValues", ["color", "food", "drink"])
    Favorites = {
        'Tim': FavoritesValues('red', 'pizza', 'soda')
    }
    # This allows you write code like:
    Favorites['Tim'].food  # pizza


### Even better...

> I will tet somethig for you, you will have to search info about
classes and lambda  ;)

So, the other thing you would like to use to make your code even better, is use [DefaultDict][3] and class.


    from collections import defaultdict
    
    
    class TFavorite:
    
        def __init__(self, color, food, drink):
            self.color = color
            self.food = food
            self.drink = drink
    
    Favorites = defaultdict(lambda: TFavorite('unknown', 'unknown', 'unknown'))
    
    # prints 'unknown' first time we lookup for Tim
    # so no previous info.
    print(Favorites['Tim'].color) 
    
    Favorites['Tim'].color = 'red'
    print(Favorites['Tim'].color) # prints 'red'
    
    print(Favorites['Tim'].food) # still unknown


  [1]: https://realpython.com/python-input-output/
  [2]: https://www.geeksforgeeks.org/namedtuple-in-python/
  [3]: https://www.geeksforgeeks.org/defaultdict-in-python/

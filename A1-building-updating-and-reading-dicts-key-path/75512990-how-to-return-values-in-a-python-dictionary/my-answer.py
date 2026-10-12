# Code from my Stack Overflow answer https://stackoverflow.com/a/75528781 (posted 2023-02-22), extracted verbatim; may need the question's context to run.

# --- block 1 ---
favsDict = { 'Tim': ['red', 'pizza', 'soda'],
             'Jake': ['green', 'burger', 'juice'],
             'Mary': ['blue', 'salad', 'water']    }

# --- block 2 ---
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

# --- block 3 ---
personsCt = 3 # how many names/people
fav_categories = ['Color', 'Food', 'Drink'] # list template for asking

favsDict = {input(f'\n[Person#{i+1}] Please Enter\n\tName: '): [
    input(f'\tFavorite {f}: ') for f in fav_categories
] for i in range(personsCt)}

print()
favsDict

# --- block 4 ---
fav_categories = ['color', 'food', 'drink'] # list template for asking
favsDict = {} # initiate

while (pName := input(f'\n[Just press Enter to exit]\nEnter name: ')):
    fPromptr = lambda fc: input(f"\t{pName}'s favorite {fc} is: ")
    favsDict[pName] = [fPromptr(fCat) for fCat in fav_categories]

print()
favsDict

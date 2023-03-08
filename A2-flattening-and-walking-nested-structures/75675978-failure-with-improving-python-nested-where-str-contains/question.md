---
title: "Failure with improving Python nested where(str.contains)"
site: stackoverflow
question_id: 75675978
url: https://stackoverflow.com/q/75675978
asked: 2023-03-08T16:54:48Z
asked_by: "James Ogle"
asked_by_url: https://stackoverflow.com/users/9381740
last_edited: never
tags: [python, dictionary, optimization, lambda, nested]
score: 0
views_at_snapshot: 63
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 04785cbb71dc04bdc66d7021d22371849ac2e27583a7ad4ff24bdce0c0e8b351
---

# Failure with improving Python nested where(str.contains)

Asked by [James Ogle](https://stackoverflow.com/users/9381740) on Stack Overflow, <https://stackoverflow.com/q/75675978>, 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So I have a column called Job Type that has user input strings.  Data entry is supposed to stick to certain terms but with turn over oddities have been creeping in along with the normal misspellings.  I have a set of nested where statements that cleans up most of the strings.  However I am not sure of the long term efficiencies of this approach let alone the readability of the code as additional terms are added.  I thought I could convert it to lambda function that uses a dictionary of the terms and another lambda function in the dictionary to return anything I haven't thought of yet as the Job Type but I am getting a KEYERROR.   

Working code is:

```
#Homogenizes Job Type
f_terms = ['FLOOR','FLR', 'TF', 'FT']   #List of common entries for FLOORS
w_terms = ['WALL', 'WL', 'TW' ]         #List of common entries for WALLS
c_terms = ['CAR','CPT']                 #List of common entries for CARPET
kbs_terms = ['KBS','BACKSPLASH']        #List of common entries for KBS (Kitchen Backsplash)
fire_terms = ['FIRE', 'FP', 'FRP']      #List of common entries for FIREPLACES
w_terms = ['WOOD', "WD"]                #List of common entries for WOOD
v_terms = ["VINYL", 'LVP','VP']         #List common entries for VINYL
pw_terms = ['PREWALK', 'PW']            #List of common entries for PREWALK
t_terms = ['TILE']                      #List of common entries for TILE (Generic Tile Repairs)
ft_terms = ['FINE', 'F/T']              #List of common entries for FINE TUNES

df['Job Type'] = np.where(df['Job Type'].str.contains('|'.join(floor_terms)),"FLOORS",
                 np.where(df['Job Type'].str.contains('|'.join(wall_terms)),"WALLS",
                 np.where(df['Job Type'].str.contains('|'.join(carpet_terms)),"CARPET",
                 np.where(df['Job Type'].str.contains('|'.join(kbs_terms)),"KBS",
                 np.where(df['Job Type'].str.contains('|'.join(fire_terms)),"FIREPLACE",
                 np.where(df['Job Type'].str.contains('|'.join(wood_terms)),"WOOD",
                 np.where(df['Job Type'].str.contains('|'.join(vinyl_terms)),"VINYL", 
                 np.where(df['Job Type'].str.contains('|'.join(prewalk_terms)), "PREWALK",
                 np.where(df['Job Type'].str.contains('|'.join(tile_terms)), "TILE", 
                 np.where(df['Job Type'].str.contains('|'.join(ft_terms)), "FINE TUNE",
                          df['Job Type']))))))))))
```

Nonworking code is:

```
term_map = {
    'FLOOR|FLR|TF|FT': 'FLOORS',
    'WALL|WL|TW': 'WALLS',
    'CAR|CPT': 'CARPET',
    'KBS|BACKSPLASH': 'KITCHEN BACKSPLASH',
    'FIRE|FP|FRP': 'FIREPLACE',
    'WOOD|WD': 'WOOD',
    'VINYL|LVP|VP': 'VINYL',
    'PREWALK|PW': 'PREWALK',
    'TILE': 'TILE',
    'FINE|F/T': 'FINE TUNE',
    '.+': lambda x: x
}

pattern = re.compile('|'.join('(?:{})'.format(term) for term in term_map.keys()))
df['Job Type'] = df['Job Type'].str.replace(pattern, lambda match: term_map[match.group(0)] \
                 if isinstance(term_map[match.group(0)], str) else term_map[match.group(0)] \
                 (match.group(0)), regex=True)

*KEYERROR: 'WALL'*
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mrblue6](https://stackoverflow.com/users/18505884)** (2023-03-08): Can you please post the full error?

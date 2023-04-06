---
title: "traversing the multi index dictionaries which is present in dataframe & store the values in a list"
site: stackoverflow
question_id: 75937977
answer_id: 75946645
url: https://stackoverflow.com/a/75946645
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-06T06:55:28Z
last_edited: 2023-04-06T07:04:46Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75946645/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5f11626994a253a866a9c5dc93ba040ed0e4382d1a810d02136115d8300a2c63
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75946645>, 2023-04-06, last edited 2023-04-06; score 0. Text as retrieved 2026-10-12.

If you [use nested list comprehension instead](https://stackoverflow.com/a/45079294/6146136) of nested for-loops:

```py
# import pandas as pd
# import ast ## I just needed this to parse the RESPONSE column from csv
# df = pd.read_csv('https://raw.githubusercontent.com/ajayvd/dataframe/main/data_sub.csv')
# df['RESPONSE'] = df['RESPONSE'].apply(ast.literal_eval) # maybe only after read_csv

k3List = ('provider', 'storeExternalId') 
get_e = lambda resp_v:resp_v['store-boundary-dsp']['estimates']
def get_separate_lists(data_frame,column='RESPONSE', k3List=k3List, get_l=get_e): 
    def get_k3(k3):
        return [e[k3] for resp in data_frame[column] for e in get_l(resp) if k3 in e]
      
    isList = isinstance(k3List, (list,tuple,set)) 
    lists = [get_k3(k) for k in (k3List if isList else [k3List])]
    return lists if isList else lists[0]

provider, store_id = get_separate_lists(df)
# provider = get_separate_lists(df, k3List='provider')
# store_id = get_separate_lists(df, 'RESPONSE', 'storeExternalId') 
```

[`k3List` can be a single key or a list (or tuple or set) of keys, and `get_l` should be a function.]

---

If you want parallel lists, you can start with a list of tuples and then [unpack](https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480) and [`zip`](https://www.programiz.com/python-programming/methods/built-in/zip) to basically "unzip" them into separate lists:

```py
# k3List, get_e = ... ## as before
def get_tuple_lists(data_frame,column='RESPONSE', k3List=k3List, get_l=get_e): 
    return [    tuple(e.get(k3) for k3 in k3List) 
                for resp in data_frame[column] for e in get_l(resp)    ]

provider_stores = get_tuple_lists(df)
provider, store_id = [list(t) for t in zip(*provider_stores)]
# provider, store_id = list(zip(*provider_stores)) ## 2 tuples instead of 2 lists
```

---

With either function, `print(f'{store_id=}\n{provider=}')` should print

> ```py
> store_id=['1504', '1504', '9346', '9346', '1035', '4883', '3791', '5464', '5464', '3869', '3869', '7510', '6221', '5708', '5708', '3465']
> provider=['Instacart', 'DoorDash', 'DoorDash', 'Uber', 'DoorDash', 'DoorDash', 'DoorDash', 'Postmates', 'DoorDash', 'Skipcart', 'DoorDash', 'DoorDash', 'DoorDash', 'Postmates', 'DoorDash', 'DoorDash']
> ```

But the direct output of `get_tuple_lists` would look like

> ```py
> provider_stores=[('Instacart', '1504'), ('DoorDash', '1504'), ('DoorDash', '9346'), ('Uber', '9346'), ('DoorDash', '1035'), ('DoorDash', '4883'), ('DoorDash', '3791'), ('Postmates', '5464'), ('DoorDash', '5464'), ('Skipcart', '3869'), ('DoorDash', '3869'), ('DoorDash', '7510'), ('DoorDash', '6221'), ('Postmates', '5708'), ('DoorDash', '5708'), ('DoorDash', '3465')]
> ```

---
---

<br>

If you're not sure that the outer keys used (like *`store-boundary-dsp`* and *`estimates`* above) exist on every row, you can use `try...except` in `get_l`:

```py
def get_b(resp_v):
    try: return resp_v['store-boundary-dsp']['boundaries']
    except: return [] 
boundary_names = set(get_separate_lists(df, k3List='name', get_l=get_b))
# --> # boundary_names={'9346 - Area - 1', '1504 - Primary', '1504-Primary'}
``` 

---
---
---

<br>

Just some notes about the snippet in your question:

> ```py
>     for index, row in data_frame.iterrows():
>         for i in range(0,len(row[column])):
>             for k,v in row[column]['store-boundary-dsp']['estimates'][i].items():
>                # if k==....
> ```

- You don't really need to use `.iterrows()` or  `range` or `.items()` here - you can just use 
  ```py
      for rc in data_frame[column]:
          for est in rc['store-boundary-dsp']['estimates']:
              if 'storeExternalId' in est: store_id.append(est['storeExternalId'])
              if 'provider' in est: provider.append(est['provider'])
  ```
- Even in the *`for k,v`* loop, defining `store_val` or `provider_val` (as `v`) is redundant [unless you plan to use them outside of their respective `if` blocks or plan to modify `v` in some way] when you can just **`.append(v)`**
- You could also add extract any number of lists [from `store-boundary-dsp.estimates`] by adding them to the `all_lists` dictionary below [instead of coding more `if`s inside *`for est...`*]
  ```py
      all_lists = {
          'storeExternalId': (store_id := []),
          'provider': (provider := []),
      }

      for rc in data_frame[column]:
            for est in rc['store-boundary-dsp']['estimates']:
                for k in all_lists:
                    if k in est: all_lists[k].append(est[k])
  ```

<br>

- You could also [use nested list comprehension instead](https://stackoverflow.com/a/45079294/6146136) of nested for-loops:
  ```py
      def get_k3(k3, k2='estimates', k1='store-boundary-dsp'):
          return [e[k3] for resp in data_frame[column] for e in resp[k1][k2] if k3 in e]
      
      k3List = ['provider', 'storeExternalId'] ## line them up EXACTLY
      provider, store_id = [get_k3(k) for k in k3List]
  ```



<br>

---

<br>

Btw, you can also use [`.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html) and [`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) to completely flatten the DataFrame:

```py
df1 = pd.concat([df[['CREATEDAT']], pd.json_normalize(df['RESPONSE'])], axis=1)
df1.columns = [c.split('.',1)[-1] for c in df1.columns]
lCols = ['value', 'errors', 'tags.1504']
dlCols = ['boundaries', 'distances', 'estimates', 'fulfillments']
for c in (lCols+dlCols): df1 = df1.explode(c)

df1 = pd.concat([df1.drop(dlCols, axis=1).reset_index(drop=True), *[
    pd.json_normalize(df1[c]).rename(columns=lambda cn: f'{c}.{cn}')
    for c in dlCols 
]],  axis=1)#.dropna(axis='columns', thresh=140) 
## dropna(axis='columns',thresh=N)--> only keep columns with < N empty cells
```

> [![flatfilt][1]][1]

> [![flatfull][2]][2]


  [1]: https://i.sstatic.net/8o6Q9.png
  [2]: https://i.sstatic.net/N2t5v.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[lifo](https://stackoverflow.com/users/10484786)** (2023-04-06): thanks a lot for such a clear explanation

# Code from my Stack Overflow answer https://stackoverflow.com/a/75946645 (posted 2023-04-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
# k3List, get_e = ... ## as before
def get_tuple_lists(data_frame,column='RESPONSE', k3List=k3List, get_l=get_e): 
    return [    tuple(e.get(k3) for k3 in k3List) 
                for resp in data_frame[column] for e in get_l(resp)    ]

provider_stores = get_tuple_lists(df)
provider, store_id = [list(t) for t in zip(*provider_stores)]
# provider, store_id = list(zip(*provider_stores)) ## 2 tuples instead of 2 lists

# --- block 3 ---
> store_id=['1504', '1504', '9346', '9346', '1035', '4883', '3791', '5464', '5464', '3869', '3869', '7510', '6221', '5708', '5708', '3465']
> provider=['Instacart', 'DoorDash', 'DoorDash', 'Uber', 'DoorDash', 'DoorDash', 'DoorDash', 'Postmates', 'DoorDash', 'Skipcart', 'DoorDash', 'DoorDash', 'DoorDash', 'Postmates', 'DoorDash', 'DoorDash']
>

# --- block 4 ---
> provider_stores=[('Instacart', '1504'), ('DoorDash', '1504'), ('DoorDash', '9346'), ('Uber', '9346'), ('DoorDash', '1035'), ('DoorDash', '4883'), ('DoorDash', '3791'), ('Postmates', '5464'), ('DoorDash', '5464'), ('Skipcart', '3869'), ('DoorDash', '3869'), ('DoorDash', '7510'), ('DoorDash', '6221'), ('Postmates', '5708'), ('DoorDash', '5708'), ('DoorDash', '3465')]
>

# --- block 5 ---
def get_b(resp_v):
    try: return resp_v['store-boundary-dsp']['boundaries']
    except: return [] 
boundary_names = set(get_separate_lists(df, k3List='name', get_l=get_b))
# --> # boundary_names={'9346 - Area - 1', '1504 - Primary', '1504-Primary'}

# --- block 6 ---
>     for index, row in data_frame.iterrows():
>         for i in range(0,len(row[column])):
>             for k,v in row[column]['store-boundary-dsp']['estimates'][i].items():
>                # if k==....
>

# --- block 7 ---
for rc in data_frame[column]:
    for est in rc['store-boundary-dsp']['estimates']:
        if 'storeExternalId' in est: store_id.append(est['storeExternalId'])
        if 'provider' in est: provider.append(est['provider'])

# --- block 8 ---
all_lists = {
    'storeExternalId': (store_id := []),
    'provider': (provider := []),
}

for rc in data_frame[column]:
      for est in rc['store-boundary-dsp']['estimates']:
          for k in all_lists:
              if k in est: all_lists[k].append(est[k])

# --- block 9 ---
def get_k3(k3, k2='estimates', k1='store-boundary-dsp'):
    return [e[k3] for resp in data_frame[column] for e in resp[k1][k2] if k3 in e]

k3List = ['provider', 'storeExternalId'] ## line them up EXACTLY
provider, store_id = [get_k3(k) for k in k3List]

# --- block 10 ---
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

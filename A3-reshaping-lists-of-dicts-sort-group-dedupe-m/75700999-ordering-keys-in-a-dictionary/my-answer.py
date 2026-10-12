# Code from my Stack Overflow answer https://stackoverflow.com/a/75702903 (posted 2023-03-11), extracted verbatim; may need the question's context to run.

# --- block 1 ---
reordered = {}
for song in output:
    for chunk in output[song]:
        for attr, val in output[song][chunk].items():
            reordered.setdefault(attr, {})
            reordered[attr].setdefault(song, {})
            reordered[attr][song][chunk] = val

# --- block 2 ---
def get_flatDict(obj, parentKeys=tuple(), asDict=True):
    if not isinstance(obj, dict): 
        return {parentKeys: obj} if asDict else [(parentKeys, obj)]

    kvPairs = []
    for k, v in obj.items(): 
        kvPairs += get_flatDict(v, parentKeys=(*parentKeys,k), asDict=False)
    return dict(kvPairs) if asDict else kvPairs

# --- block 3 ---
reordered = {}
for (song, chunk, attr), val in get_flatDict(output).items():
    reordered.setdefault(attr, {})
    reordered[attr].setdefault(song, {})
    reordered[attr][song][chunk] = val

# --- block 4 ---
output = { 'song1': {
    'chunk1': {'attr1': 'value1', 'attr2': 'value2', 'attr3': 'value3'},
    'chunk2': {'attr1': 'value4', 'attr2': 'value5', 'attr3': 'value6'},
    'chunk3': {'attr1': 'value7', 'attr2': 'value8', 'attr3': 'value9'}},
  'song2': {'chunk1': {'attr1': 'value0'}} }

# --- block 5 ---
> { 
>   'attr1': {
>     'song1': {'chunk1': 'value1', 'chunk2': 'value4', 'chunk3': 'value7'},
>     'song2': {'chunk1': 'value0'}
>   },
>   'attr2': {
>     'song1': {'chunk1': 'value2', 'chunk2': 'value5', 'chunk3': 'value8'}
>   },
>   'attr3': {
>     'song1': {'chunk1': 'value3', 'chunk2': 'value6', 'chunk3': 'value9'}
>   }
> }
>

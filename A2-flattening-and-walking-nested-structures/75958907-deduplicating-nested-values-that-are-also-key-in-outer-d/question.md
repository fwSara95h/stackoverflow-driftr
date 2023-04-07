---
title: "Deduplicating nested values that are also key in outer dictionary - Python"
site: stackoverflow
question_id: 75958907
url: https://stackoverflow.com/q/75958907
asked: 2023-04-07T13:33:52Z
asked_by: "alvas"
asked_by_url: https://stackoverflow.com/users/610569
last_edited: never
tags: [python, dictionary, duplicates, key-value]
score: 0
views_at_snapshot: 44
answer_count: 1
accepted_answer_id: 75961692
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c873f3d61799439ecb96d34c227ec3f7e3d7186b36bea3945f8cdd3c52785443
---

# Deduplicating nested values that are also key in outer dictionary - Python

Asked by [alvas](https://stackoverflow.com/users/610569) on Stack Overflow, <https://stackoverflow.com/q/75958907>, 2023-04-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Given an input dictionary, 

```
x = {'A fantastic gift for art lovers': ['Designed for adults, this stunning piece '
                                     'of 3D art can be proudly displayed on a '
                                     'wall following a rewarding build '
                                     'experience.'],
 'Build and relax': ['Art lovers can enjoy a relaxing and immersive building '
                     'experience as they create this unique artwork from 1,810 '
                     'pieces.'],
 'Create your own artwork': ['Build Hokusai’s The Great Wave with layers of '
                             'LEGO® bricks.'],
 'Finishing touch': ['Add a decorative tile with Hokusai’s signature.'],
 'Hokusai – The Great Wave': ['Create your own artwork',
                              'Build Hokusai’s The Great Wave with layers of '
                              'LEGO® bricks.',
                              'The Great Wave comes to life!',
                              'The picture’s multiple layers create a stunning '
                              '3D effect.',
                              'Finishing touch',
                              'Add a decorative tile with Hokusai’s '
                              'signature.'],
 'Immerse yourself in the world of art': ['Listen to the set’s Soundtrack, '
                                          'tailor-made with content to enhance '
                                          'the time you spend building this '
                                          'Japanese wall art.'],
 'Recreate an iconic piece of Japanese art': ['Celebrate your passion for '
                                              'Japanese art when you build '
                                              'this incredible LEGO® version '
                                              'of Hokusai’s The Great Wave.'],
 'The Great Wave comes to life!': ['The picture’s multiple layers create a '
                                   'stunning 3D effect.']}
```

There are some duplicates in the inner list values of the keys, e.g. 

```
>>> y = x['The Great Wave comes to life!']
>>> y
['The picture’s multiple layers create a stunning 3D effect.']

>>> z = x['Hokusai – The Great Wave'][3]
>>> z
'The Great Wave comes to life!'
```

The goal is to remove `y`, if `z` is in any key of `x`.

The expected output of the deduplicated `x` should look like this:

```
{'A fantastic gift for art lovers': ['Designed for adults, this stunning piece '
                                     'of 3D art can be proudly displayed on a '
                                     'wall following a rewarding build '
                                     'experience.'],
 'Build and relax': ['Art lovers can enjoy a relaxing and immersive building '
                     'experience as they create this unique artwork from 1,810 '
                     'pieces.'],
 'Hokusai – The Great Wave': ['Create your own artwork',
                              'Build Hokusai’s The Great Wave with layers of '
                              'LEGO® bricks.',
                              'The Great Wave comes to life!',
                              'The picture’s multiple layers create a stunning '
                              '3D effect.',
                              'Finishing touch',
                              'Add a decorative tile with Hokusai’s '
                              'signature.'],
 'Immerse yourself in the world of art': ['Listen to the set’s Soundtrack, '
                                          'tailor-made with content to enhance '
                                          'the time you spend building this '
                                          'Japanese wall art.'],
 'Recreate an iconic piece of Japanese art': ['Celebrate your passion for '
                                              'Japanese art when you build '
                                              'this incredible LEGO® version '
                                              'of Hokusai’s The Great Wave.']}
```


I've tried the following:

```python
    to_delete = []
    for k,v in x.items():
        for vv in v:
            if vv in x:
                to_delete.append(vv)
                
    for d in x:
        if d in x:
            del x[d]
```

And a simpler form:

```python
    for k in list(x.keys()):
        if k in x:
            for vv in x[k]:
                if vv in x:
                    del features[vv]
```

Both code snippet would work to get the expected output but there's some quirks to them and I wonder if there's a better way to process it. The code above works well on small dictionary but at millions/billions scale, it's just way too inefficient to iterate through the keys twice. 

 - The first snippet loops through the key-value pairs and then keep a list of keys to delete. The main issue is that the dictionary has to be looped through 2 times instead of one

 - The 2nd snippet has this odd `if k in x` because when we loop through a copy of the `list(x.keys())`, the keys iterated are the old key and as the dictionary keys get dynamically popped, it's needed to check that it exists before checking if it's a duplicate

## Is there a better way to iterate through a dictionary and then delete duplicates? 

E.g. maybe something like flatten the values into a set and do an intersection with the keys? Would that be a faster compute if `x` is a huge dictionary?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Brendan Abel](https://stackoverflow.com/users/1547004)** (2023-04-07): If a key is deleted, would you still want duplicate values from that key to also be deleted, even though that key doesn't exist anymore?
- **[alvas](https://stackoverflow.com/users/610569)** (2023-04-08): Would the value still exist in the dictionary object when a key is deleted? Cos it won't be accessible anyway.
- **[Brendan Abel](https://stackoverflow.com/users/1547004)** (2023-04-08): Yes, but in your first example, you're deleting them in a separate pass. So you find all the keys first.

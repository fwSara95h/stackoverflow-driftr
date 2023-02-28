---
title: "How to remove or ignore an entry in a JSON file using python?"
site: stackoverflow
question_id: 75598088
url: https://stackoverflow.com/q/75598088
asked: 2023-02-28T22:52:35Z
asked_by: "Hosein Nikkhah"
asked_by_url: https://stackoverflow.com/users/21258013
last_edited: 2023-03-01T03:05:21Z
last_editor: "OneCricketeer"
last_editor_url: https://stackoverflow.com/users/2308683
tags: [python, json]
score: 1
views_at_snapshot: 1311
answer_count: 2
accepted_answer_id: 75598450
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a5b4a3f304596ea9f523f5dd3c6b2a0fbca10768eeaf6ed3778ee31e12696327
---

# How to remove or ignore an entry in a JSON file using python?

Asked by [Hosein Nikkhah](https://stackoverflow.com/users/21258013) on Stack Overflow, <https://stackoverflow.com/q/75598088>, 2023-02-28, last edited 2023-03-01 by [OneCricketeer](https://stackoverflow.com/users/2308683). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working on a code that extracts data from a JSON file here is the JSON file: [Google CDN](https://www.gstatic.com/ipranges/cloud.json)

and here is a sample of JSON code:

```
{
  "syncToken": "1677578581095",
  "creationTime": "2023-02-28T02:03:01.095938",
  "prefixes": [{
    "ipv4Prefix": "34.80.0.0/15",
    "service": "Google Cloud",
    "scope": "asia-east1"
  }, {
    "ipv4Prefix": "34.137.0.0/16",
    "service": "Google Cloud",
    "scope": "asia-east1"
  }, {
    "ipv4Prefix": "35.185.128.0/19",
    "service": "Google Cloud",
    "scope": "asia-east1"
  }, {
    "ipv6Prefix": "2600:1900:40a0::/44",
    "service": "Google Cloud",
    "scope": "asia-south1"
  },
```

I know where the problem is but can not fix the issue with solutions on this website and getting another error every time.

This is my code

```
import json
f = open('cloud.json')
data = json.load(f)
array = []

for i in data['prefixes']:
    array = [i['prefix'] for i in data['ipv4Prefix']]
f_path = (r"ip.txt")
with open (f_path ,'w') as d:
       for lang in array:
        d.write("{}\n".format(lang))
f.close()
```

Basically I want to extract only ipv4 address but there are some ipv6 address randomly in block that causes this error so I get key error like this: KeyError: 'ipv4Prefix'

I know why I am getting this error so I tried deleting that whole entry with ipv6Prefix so I added this part to my code:

```
    if data[i]["prefixes"] == "ipv6Prefix":
        data.pop(i)
```

for this one I get TypeError: unhashable type: 'dict' which is new to me, I also tried this as someone pointed out in another question but it didn't work.

```
del data[ipv6Prefix]
```

Now my final code is like this and getting this error: TypeError: list indices must be integers or slices, not str which is understandable.

```
import json
f = open('cloud.json')
data = json.load(f)
array = []
for i in data['prefixes']:
    if [i]["prefixes"] == ['ipv6Prefix']:
        data.pop(i)
    array = [i['prefix'] for i in data['ipv4Prefix']]
f_path = (r"ip.txt")
with open (f_path ,'w') as d:
       for lang in array:
        d.write("{}\n".format(lang))
f.close()
```

So how can I delete entries with 'ipv6Prefix' or better to say, ignore them in my for loop?

I found [this](https://stackoverflow.com/questions/65521978/ignore-specific-json-keys-when-extracting-data-in-python) question but answer does not fit my code at all.

what's the problem with my code?

I tried several methods like `del` and `dict.pop()` but still I get error.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-02-28): `array = [i['prefix'] for i in data['ipv4Prefix']]` replaces `array` each time through the loop. You probably want to append to `array`, not reassign it.
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-02-28): There is no `data['ipv4Prefix']`. And it's not a list, so why do you want to loop through it? There's also no `prefix` key in any of the dictionaries, so what is `i['prefix']` supposed to be?
- **[Hosein Nikkhah](https://stackoverflow.com/users/21258013)** (2023-02-28): I don't think if append helps in this case but let me try it, and about `i['prefix']` you mentioned, if you open the link you'll see around 540 entries which is why I used this, it actually helps to call each entry in a time and then with `data['ipv4Prefix']` I can extract all ipv4 addresses, this is at least what I tried for another json file and worked perfectly, I can share the code if you like. @Barmar
- **[Hosein Nikkhah](https://stackoverflow.com/users/21258013)** (2023-02-28): @Barmar Check this [link](https://codeshare.io/PdEwNo), you can see I used same approach in both my codes but this only does not work because of random ipv6prefix objects in it
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-03-01): I checked the link, I don't see `prefix` anywhere. There's just `ipv4Prefix` and `ipv6Prefix`.
- **[Hosein Nikkhah](https://stackoverflow.com/users/21258013)** (2023-03-01): it's for another JSON file, code I shared in that link extracts data from AWS however in this code I shared on stack overflow I am trying to extract from Google JSON file

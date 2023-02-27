---
title: "How to polish return and save to individual JSON/csv file?"
site: stackoverflow
question_id: 75576121
url: https://stackoverflow.com/q/75576121
asked: 2023-02-27T01:33:32Z
asked_by: "SunnyD"
asked_by_url: https://stackoverflow.com/users/12417843
last_edited: 2023-02-27T16:49:18Z
last_editor: "pho"
last_editor_url: https://stackoverflow.com/users/843953
tags: [python, json, csv]
score: -1
views_at_snapshot: 75
answer_count: 2
accepted_answer_id: 75583260
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a1c6e0be76766621929ce17d293a3d396e66399fd71a34c3690c68cdc0e06bd3
---

# How to polish return and save to individual JSON/csv file?

Asked by [SunnyD](https://stackoverflow.com/users/12417843) on Stack Overflow, <https://stackoverflow.com/q/75576121>, 2023-02-27, last edited 2023-02-27 by [pho](https://stackoverflow.com/users/843953). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Below code is from https://stackoverflow.com/questions/47666699/using-word2vec-to-classify-words-in-categories and I need some help on input and return saveing. Any help would be greatly appreciated.

```
# Category -> words
data = {
  'Names': ['john','jay','dan','nathan','bob'],
  'Colors': ['yellow', 'red','green', 'oragne', 'purple'],
  'Places': ['tokyo','bejing','washington','mumbai'],
}
# Words -> category
categories = {word: key for key, words in data.items() for word in words}

# Load the whole embedding matrix
embeddings_index = {}
with open('glove.6B.100d.txt', encoding='utf-8') as f:
  for line in f:
    values = line.split()
    word = values[0]
    embed = np.array(values[1:], dtype=np.float32)
    embeddings_index[word] = embed
print('Loaded %s word vectors.' % len(embeddings_index))
# Embeddings for available words
data_embeddings = {key: value for key, value in embeddings_index.items() if key in categories.keys()}

# Processing the query
def process(query):
  query_embed = embeddings_index[query]
  scores = {}
  for word, embed in data_embeddings.items():
    category = categories[word]
    dist = query_embed.dot(embed)
    dist /= len(data[category])
    scores[category] = scores.get(category, 0) + dist
  return scores

# Testing
print(process('jonny'))
print(process('green'))
print(process('park'))
```

And the return looks like:
```
Loaded 400000 word vectors.
{'Names': 7.965438079833984, 'Places': -0.3282392770051956, 'Colors': 1.803783965110779}
{'Names': 11.360316085815429, 'Places': 3.536876901984215, 'Colors': 21.82199630737305}
{'Names': 10.234728145599364, 'Places': 8.739515662193298, 'Colors': 10.761297225952148}
```



Below are the changes I want to make to this scrip but keep failing :( Please help.

Question 1: The order or category (data) is Names, Colors, and Places. But why does the retun has Name, Place, Color order instead? This is not important but was wondering why.

Question 2: Instead of using **print(process('jonny'))**, how can I input list of text from text file?

Question 3: Lets suppose name of input text file is TEST.txt. How can I save the return in TEST.JSON or TEST.csv file? Basically input and output as same name.

Thank yo so much!

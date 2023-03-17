---
title: "use of reverse dictionary to replace missing values"
site: stackoverflow
question_id: 75766867
url: https://stackoverflow.com/q/75766867
asked: 2023-03-17T11:07:05Z
asked_by: "Anastasia"
asked_by_url: https://stackoverflow.com/users/20689651
last_edited: 2023-03-17T12:41:54Z
last_editor: "Jeronimo"
last_editor_url: https://stackoverflow.com/users/8547331
tags: [python, dictionary, replace]
score: 0
views_at_snapshot: 100
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d8a5909258f16a943e7ee001f65d6c744c9102b72ed38634eb7165d79bbdae84
---

# use of reverse dictionary to replace missing values

Asked by [Anastasia](https://stackoverflow.com/users/20689651) on Stack Overflow, <https://stackoverflow.com/q/75766867>, 2023-03-17, last edited 2023-03-17 by [Jeronimo](https://stackoverflow.com/users/8547331). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I use the following dictionary to replace missing values in a column in my dataframe:

```python
dct = {
'Central and Eastern Europe': [
    'Albania','Bosnia and Herzegovina','Bulgaria','Croatia','Czech Republic','Estonia','Hungary','Kosovo',
    'Latvia','Lithuania','Montenegro','North Macedonia','Poland','Romania','Serbia','Slovakia','Slovenia'],
'Commonwealth of Independent States': [
    'Armenia','Azerbaijan','Belarus','Georgia','Kazakhstan','Kyrgyzstan','Moldova','Russia','Tajikistan','Turkmenistan','Ukraine','Uzbekistan'],
...
}
```

Now i use the following code to invert the dictionary:

```python
revdct = {c: r for r, lst in dct.items() for c in lst}
nan = float('NaN')
df = df.set_index('Country')['Region'].fillna(revdct).reset_index()
df
```

df only shows the dataframe with the two columns 'Country' and 'Region'
how do i get the whole dataframe printed, since it has also other columns?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[pho](https://stackoverflow.com/users/843953)** (2023-03-20): [How to make good reproducible pandas examples](//stackoverflow.com/q/20109391/843953) Sure, we can fabricate a dataframe with example data to test your/our code on, but wouldn't it be _so much easier_ if you just included a sample of your dataframe in your question?!

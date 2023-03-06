---
title: "Counting positive words in a passage python"
site: stackoverflow
question_id: 75646277
url: https://stackoverflow.com/q/75646277
asked: 2023-03-06T00:48:10Z
asked_by: "Alexandra Barraza"
asked_by_url: https://stackoverflow.com/users/21321474
last_edited: 2023-03-06T06:58:16Z
last_editor: "Talha Tayyab"
last_editor_url: https://stackoverflow.com/users/13086128
tags: [python, python-3.x, list, dictionary, return]
score: -2
views_at_snapshot: 243
answer_count: 3
accepted_answer_id: 75646466
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1621a566568d1552cc4d8f12fc38f61ff99d0535b51cd22f522d9c50aaa032c3
---

# Counting positive words in a passage python

Asked by [Alexandra Barraza](https://stackoverflow.com/users/21321474) on Stack Overflow, <https://stackoverflow.com/q/75646277>, 2023-03-06, last edited 2023-03-06 by [Talha Tayyab](https://stackoverflow.com/users/13086128). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have to count the times positive and negative words appear in a passage. 

I have a list of positive words, list of negative words, and a passage excerpt. 
```
pos_words = ['happy', 'like', 'love', 'good', 'favorite', 'best', 'great', 'amazing', 'joyful', 'positive']
neg_words = ['sad', 'dislike', 'hate', 'angry', 'horrible', 'bad', 'worst', 'boring', 'negative']
passage_excerpt = "I love CSS 1, it's my favorite class and not as horrible as I thought"
``` 

I have to return a dictionary titled sentiment_info that looks like this: 
```
{'num_pos_words': ..., # how many positive words
 'num_neg_words': ..., # how many negative words
 'num_words_total': ... # how many total words
```




I have tried this code so far: 
```
def calculate_words(x):
    cleaned_passage = clean_text(x)
    num_pos_words = 0 
    num_neg_words = 0 
    num_words_total = 0 
    if x in pos_words and passage_excerpt:
        num_pos_words += 1 
    if x in neg_words and passage_excerpt: 
        num_neg_words += 1 
    num_words_total = num_pos_words + num_neg_words

    return{'num_pos_words': num_pos_words,
     'num_neg_words': num_neg_words,
     'num_words_total': num_words_total}
```
I do not know if a function was the correct approach or I needed a for loop.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Julien](https://stackoverflow.com/users/4565947)** (2023-03-06): [ask] and [mre]
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-03-06): `if x in pos_words and passage_excerpt` This is not doing what you think.
- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-03-06): What is `x` supposed to be?  You haven't shown us how this function is called.
- **[Daniel Hao](https://stackoverflow.com/users/10760768)** (2023-03-06): What is the ```clean_text()``` supposed to do?  can you show it?

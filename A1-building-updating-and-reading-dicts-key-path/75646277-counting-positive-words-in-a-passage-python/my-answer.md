---
title: "Counting positive words in a passage python"
site: stackoverflow
question_id: 75646277
answer_id: 75646470
url: https://stackoverflow.com/a/75646470
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-06T01:51:58Z
last_edited: 2023-03-06T03:40:27Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75646470/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a107cbb8526ee4a189710ecef620c42eeacb145d9edabdb6fdebb0d266752bad
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75646470>, 2023-03-06, last edited 2023-03-06; score 0. Text as retrieved 2026-10-12.

How are you calling `calculate_words`? And yes, you need to **loop** through the words [which you can use [`.split`](https://www.programiz.com/python-programming/methods/string/split) to get], but that does not preclude using a function. I think your intended purposes can be served with something like 

```py
def calculate_words(x, pList=['good'], nList=['bad']):
    x_words = x.split() ## without cleaning
    # x_words = clean_text(x).split() ## words after cleaning
    num_pos_words, num_neg_words = 0, 0
    for w in x_words:
        if w in pList: num_pos_words += 1
        elif w in nList: num_neg_words += 1

    num_words_total = num_pos_words + num_neg_words # only count if +ve or -ve
    # num_words_total = len(x_words) # count ALL words

    return {  'num_pos_words': num_pos_words,
              'num_neg_words': num_neg_words,
              'num_words_total': num_words_total  }

passage_word_counts = calculate_words(passage_excerpt, pos_words, neg_words)
```

then `passage_word_counts` would return

> ```py
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 3}
> ```

Although, if you used `num_words_total = len(x_words)` then `passage_word_counts` would return

> ```py
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 15}
> ```

---

Btw, the [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) is quite handy for this sort of thing.

<br>

```py
import collections

# passage_words = clean_text(passage_excerpt).split() 
passage_words = passage_excerpt.split()
passage_word_counts = {**collections.Counter(
    'num_pos_words' if w in pos_words else (
        'num_neg_words' if w in neg_words else 'num_na_words'
    ) for w in passage_excerpt.split()
), 'num_words_total': len(passage_words)} 
```

> ```py
> # passage_word_counts = \
> {'num_na_words': 12,
>  'num_pos_words': 2,
>  'num_neg_words': 1,
>  'num_words_total': 15}
> ```

<br>

or 

```py
import collections

# passage_words = clean_text(passage_excerpt).split() 
passage_words = passage_excerpt.split()
passage_word_counts = collections.Counter((
    'num_pos_words' if w in pos_words else 'num_neg_words'    
) for w in passage_excerpt.split() if w in pos_words+neg_words)
passage_word_counts['num_words_total'] = sum(passage_word_counts.values())
```

> ```py
> # passage_word_counts = \
> {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 3}
> ```

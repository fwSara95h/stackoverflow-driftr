---
title: "Python Pandas: Append a column with each cell being a dictionary to pre-existing data-frame"
site: stackoverflow
question_id: 75749042
url: https://stackoverflow.com/q/75749042
asked: 2023-03-15T19:02:59Z
asked_by: "Hyperi"
asked_by_url: https://stackoverflow.com/users/21406023
last_edited: 2023-03-16T08:02:08Z
last_editor: "Community"
last_editor_url: https://stackoverflow.com/users/-1
tags: [python, python-3.x, pandas, dataframe, dictionary]
score: -1
views_at_snapshot: 313
answer_count: 1
accepted_answer_id: 75755016
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0e99c160ca56503ca07ac2396e73a6b1e90c419bbddfed7c8eacfa37bcebc803
---

# Python Pandas: Append a column with each cell being a dictionary to pre-existing data-frame

Asked by [Hyperi](https://stackoverflow.com/users/21406023) on Stack Overflow, <https://stackoverflow.com/q/75749042>, 2023-03-15, last edited 2023-03-16 by [Community](https://stackoverflow.com/users/-1). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a DataFrame `df` of form:

```lang-none       
index  name      val            
0       Abc    17.29
1       Bcd  137.036
2       Cde      666
```

---

I want to append a column called `"ColDict"` to `df` wherein each element of the column is a dictionary. The keys for the dictionaries would be `str(b)` for `b` being some number in an arbitrary list `list_b` and the values matched with key `str(b)` would be the output of `myfunc(df["val"], b)`, that is `myfunc()` applies to `df["val"]` (for the given row) and `b` in the specified order, for some float-valued function `myfunc` (which I have written). All of the dictionaries will be of the same length (in terms of key count) because the keys all will belong to and exhaust `list_b`.

For concreteness in this example, we can take `list_b = [5, 7.6, 10, 20]`, but it really should be 'open-ended'. Likewise, we can take `myfunc(x, b)` to round `x` down to the greatest multiple of `b` which is less than or equal to `x`.

In this case, the final result should look like this:

```lang-none       
index  name      val   ColDict            
0       Abc    17.29   {"5": myfunc(17.29, 5), "7.6": myfunc(17.29, 7.6), "10": myfunc(17.29, 10), "20": myfunc(17.29, 20)}
1       Bcd  137.036   {"5": myfunc(137.036, 5), "7.6": myfunc(137.036, 7.6), "10": myfunc(137.036, 10), "20": myfunc(137.036, 20)}
2       Cde      666   {"5": myfunc(666, 5), "7.6": myfunc(666, 7.6), "10": myfunc(666, 10), "20": myfunc(666, 20)}
```
where `myfunc(v, b)` is a float-valued output (not the string "myfunc(v, b)" or anything similar thereto).

___

I am having three issues:

1. The first problem is getting a multivariate (here: binary) function to apply to the elements of a DataFrame column. The `apply()` and `map()` methods seem to work only for univariate functions... I can podge together a `lambda` expression for this, but it seems like a sloppy solution. Also, I am not sure that I am evaluating element-wise, which is what I want, via this attempted solution path.

2. The second problem is getting Python to accept the assignment of any new column at all. It keeps telling me that I am trying to set a value on a copy of a slice. I may have gotten around this issue, in the case of a single fixed b, but I would like to know how to do so in the canonical way. (Yes, I am new to Python).

3. The third problem is that my compiler does not seem to like to have dictionaries as cell values in a DataFrame. Maybe. It is telling me that the length of values (the number of terms in list_b, which is 4 in th above example) does not match length of the index (1 + the last index of df; so, from the above table, it would be 3). Perhaps my code is trying to assign vertically through the table somehow instead, and dictionary-valued cells could be acceptable if it were executed properly?

    - I theoretically could just assign n new columns to the DataFrame, with the name of each column being `"ColDict_[b]"` where `b` is variable, if I solve problems #1 and #2, where `n = len(list_b)`. However, I think that the dictionary presentation would be cleaner for my situation. If appending multiple columns is the only or best way to do it, though, then please teach me how to do so instead. Note, however, that I also do not know how to make a variable column label (like `"ColDict_[b]"` for variable `b`) in the assignment environment, so that would have to be taught as well.

Thank you.

---

What I have tried so far:

I have tried many things, but these are my best attempts so far.

<br>

1. For a fixed `b` (such as: `b = 5`), I tried: 

   ```py
   df = df.assign(ColDict_5 = df["val"].map(lambda x: myfunc(x, 5)).
   ```
   This at least compiles. But I am not sure that this even works for this specific case. If it were to, I still cannot generalize it to multiple b values in a single step, nor do I know that this solution is best in terms of performance, presentation, or methodology, albeit syntactically operational.

<br>


2. Dictionary comprehension does not seem to work. Both of these fail: 

   ```py
   df = df.assign(ColDict = {str(b): myfunc(df["val"], b) for b in list_b})
   ```

   ```py
   df = df.assign(ColDict = {str(b): df["val"].map(lambda x: myfunc(x, b)) for b in list_b})
   ```

   The former fails at least because it is trying to convert the series to a float. The latter fails for the aforementioned reason (the length of the values exceeds the number of rows).

<br>

3. If I want to assign a fixed list (here: `[1, 2]`) to a new column for each row, then this works:

   ```py
   df = df.assign(colFixedList =  pd.Series( [[1,2]] * len(df.index) ) )
   ```

   This might generalize to my goal, but I am not yet sure how to make it do so.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-03-15): I'm not entirely sure I understand what you're trying to do, but is it anything like what you might get if you tried **`df['ColDict'] = [{str(b): myfunc(v, b) for b in list_b} for v in df['val']]`** or `df['ColDict'] = df['val'].apply(lambda v: {str(b): myfunc(v, b) for b in list_b})`? [Nothing wrong with *"podging together a lambda expression"* btw, it's not sloppy as long as the expression is simple enough.]
- **[Hyperi](https://stackoverflow.com/users/21406023)** (2023-03-16): For clarity: I want ColDict in the zeroth row to have {"5": myfunc(17.29, 5), "7.6": myfunc(17.29, 7.6), "10": myfunc(17.29, 10), "20": myfunc(17.29, 20)} as its entry. The next row would be the same, except with the 17.29 swapped out for 137.036 in each occurrence. (Assuming list_b to and df to be as above).
- **[Hyperi](https://stackoverflow.com/users/21406023)** (2023-03-16): Both your first and second solutions seem to work. (I dislike using lambda expressions here because I already defined the function elsewhere and it feels wrong to need to define a separate univariate function for this context. But that is probably just a personal issue). Any idea about how to avoid the "a value is trying to be set on a copy of a slice from a DataFrame" warning, which seems to not matter? It arises in both solutions for me. Anyway, nice job! Write this up as an answer and I will then give you the credit. Thanks! :)

---
title: "Creating a MultiIndex pandas dataframe with columns from Excel files"
site: stackoverflow
question_id: 75948675
answer_id: 75954774
url: https://stackoverflow.com/a/75954774
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-07T01:02:06Z
last_edited: 2023-04-07T10:39:00Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75954774/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: efc8f1fe2c39b2d7d80af2fdeb056d1ae032f1fd82b341304d19c0160d6af7cc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75954774>, 2023-04-07, last edited 2023-04-07; score 0. Text as retrieved 2026-10-12.

I'm still not quite sure I understand your exactly what you're dealing with and what you want in the end, but if your sample DataFrame is recreated<sup>**([view screenshot][1])**</sup> with 

> ```py
> df = pd.DataFrame([
>   [140.5745654, 90.9496963, 157.5959379, 101.2858137, 236.882037, 105.4921111],
>   [140.8908259, 91.01647765, 157.4825549, 101.4976646,236.6523714,105.2591143],
>   [141.1076296, 91.08488883, 157.3080705, 101.8022116],
>   [141.3524628, 91.17138846, 157.3539987, 102.167996],
>   [143.2526588, 92.28797636], [143.776291, 92.62887289]
> ], columns=pandas.MultiIndex.from_tuples([
>     ('C5P', 'CI2', 1, 'p'), ('C5P', 'CI2', 1, 'q'), ('C5P', 'CI2', 2, 'p'), 
>     ('C5P', 'CI2', 2, 'q'), ('C5P', 'CI2', 3, 'p'), ('C5P', 'CI2', 3, 'q')
> ], names=['borehole', 'sample','specimen', '']))
> ```

then if you `.pivot` and `.stack` again:

```py
df_pivot = df.T.reset_index().pivot(['borehole', 'sample','specimen'], '', )
df_stack = df_pivot.swaplevel(0,1,1).stack(1)
``` 

|`df_pivot.T`|`df_stack`|`df_stack.droplevel(3, axis='index')`|
|:-:|:-:|:-:|
|[![pivot_t][3]][3]<sub>([`df_pivot`][2] has been transposed to fit better)</sub>|[![stack][4]][4]_____________________________|[![droplevl][6]][6]____|

<br>

---

<br>

### ADDED EDIT: Single-Column DF

```py
df.T.stack().to_frame().swaplevel().sort_index() ## OR
# df.unstack().to_frame().swaplevel().sort_index()
```

[![desired][7]][7]



  [1]: https://i.sstatic.net/FOaAC.png
  [2]: https://i.sstatic.net/055W5.png
  [3]: https://i.sstatic.net/iM8CK.png
  [4]: https://i.sstatic.net/l3OF1.png
  [6]: https://i.sstatic.net/6UaDv.png
  [7]: https://i.sstatic.net/tU698.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user2078621](https://stackoverflow.com/users/2078621)** (2023-04-07): that's great, thank you  so much for your help. What I would actually achieve is exactly like the left example you provided, but with p and q being sub level columns of each 1, 2, 3 specimen like what I showed in my post.
- **me** (2023-04-07): @user2078621 that's actually even easier: just use `df.T.stack().to_frame().swaplevel().sort_index()` ([view result](https://i.sstatic.net/tU698.png)) or *`df.unstack().to_frame().swaplevel().sort_index()`*
- **[user2078621](https://stackoverflow.com/users/2078621)** (2023-04-07): the piece of code that you proposed in your answer, prior to any ```.pivot``` and ```.stack``` does exactly what I want. Now the only problem is that I have data in columns, not in rows as in your code! How can I use data in columns provided they have different lengths?
- **me** (2023-04-07): Just transpose with `.T`? But that's all I'm doing before *prior to any `.pivot` and `.stack`*, so you'd just be reversing that...? I'm even more confused now...
- **me** (2023-04-07): Does [my `df`](https://i.sstatic.net/FOaAC.png) look like it's meant to be btw? and would you mind manually mocking up an output for your sample data that looks like you'd want it to in the end? [Also, can I see that `df.to_dict('tight')` snippet I mentioned before? And whether the sample data is all from one file of 3(?) separate files?]
- **me** (2023-04-07): Sorry if that feels like too many questions, but I do need that info to properly reproduce your data and to understand what you want....
- **[user2078621](https://stackoverflow.com/users/2078621)** (2023-04-07): Yes, your df looks exactly as it is meant to be. Clearly there'll be more "boreholes", other "samples" for each borehole, and "specimens" 1, 2, 3 for each sample. The Excel files are named [borehole]_[sample].xlsx and contain various columns, among which the "p" and "q" I want to extract. The length of the columns may differ from file to file.

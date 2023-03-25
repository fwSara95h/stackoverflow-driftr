---
title: "How to map a function over a dataframe field that is a list"
site: stackoverflow
question_id: 75827968
answer_id: 75845119
url: https://stackoverflow.com/a/75845119
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-25T23:35:33Z
last_edited: 2023-03-27T05:07:46Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75845119/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 82a849b00dddca151420fe99caed4fe6a714d80036325f1309a87adb3992712d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75845119>, 2023-03-25, last edited 2023-03-27; **accepted**; score 1. Text as retrieved 2026-10-12.

If you had `df` as below,

```py
df = pd.DataFrame(
    columns=['STUDENT_ID', 'RECORD_ID', 'NODE_NAME', 'ACTIVITY_NAME', 'ACTIVITY_GRADE'],
    data=[  ['FredID', 'gobbledeegook1', 'Node1', 'MyActivity1', 'PreK, Kindergarten PreK'], 
            ['FredID', 'gobbledeegook2', 'Node1', 'MyActivity1', 'Kindergarten PreK'], 
            ['FredID', 'gobbledeegook3', 'Node2', 'MyActivity2', '1st Grade 1st Grade'], 
            ['JaniceID', 'gobbledeegook4', 'Node3', 'MyActivity3', 'Kindergarten Kindergarten'], 
            ['JaniceID', 'gobbledeegook5', 'Node3', 'MyActivity3', '1st Grade Preschool']    ]
)  
```
<sup>(I altered the last row so that it doesn't look like the added column only has the minimum for that row in the final output.)</sup>

and a reference dictionary `index_to_grade`

```py
## I changed "Pre-K" to "PreK" since that's how it seems to be in your dataset
index_to_grade = {-2: 'Preschool', -1: 'PreK', 0: 'Kindergarten', 1: '1st Grade', 2: '2nd Grade', 3: '3rd Grade', 4: '4th Grade', 5: '5th Grade'}
# grade_to_index = {g: i for i, g in index_to_grade.items()} ## not needed for my solution
```

---

> *How can I create a function that will map the grade_to_index dictionary across each value of the comma-separated string that is ACTIVITY_GRADE, take the minimum for that activity, then group by node and take the min over the node's activities?*

You can write a function like

```py
def get_min_gi(grades:str, refDict=index_to_grade, defaultVal=None):
    inds = [i for i,g in refDict.items() if g in grades]
    return min(inds) if inds else defaultVal
```

and [`.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html) it to `df['ACTIVITY_GRADE']`

```py
df['min_grade'] = df['ACTIVITY_GRADE'].apply(get_min_gi) ## will be over-written
min_node_grade_index = df.groupby('NODE_NAME')['min_grade'].transform('min')
df['min_grade'] = min_node_grade_index.map(index_to_grade) ## over-write
```

[![opdf][1]][1]

---
---

About why your code might not have worked:


> *`grade_to_index = {"Preschool": -2, "Pre-K": -1, ....`*

> *`FredID  gobbledeegook1  Node1   MyActivity1 PreK, Kindergarten  PreK`*
   
`grade_to_index` has key "Pre-K", but your sample dataset contains various instances of "PreK" (is it just a typo?)

---

And also, 

> *`df.ACTIVITY_GRADE.str.split(",", expand = True)`* - ([view sample output][2])

> *`df[___].replace(grade_to_index)`* - ([view sample output][3])

The issue here is that not all you `ACTIVITY_GRADE` strings are properly comma-separated, so the `split` wouldn't work as intended; and even if they were comma separated, you should split by <kbd>`', '`</kbd> [at least for your sample data] because `.replace` will not work if there's extra whitespace around the keywords; and even then, you'd have more than 2 columns<sup>([view sample output][4])</sup> as a result (row 1 has 3 grades), so the *`df[['activity_grade_a', 'activity_grade_b']] =`* part would raise error.
    
(That's why I prefer using a function like `get_min_gi` above since it should work for any number of grades.)

---

### ADDED EDIT

> [![desiredOp][5]][5]

To get that, I would suggest something like

```py
# df['row_min_grade'] = df['ACTIVITY_GRADE'].apply(get_min_gi) # temporary 
df['row_min_grade'] = [min([grade_to_index.get(v,v) for v in i]) for i in df['ACTIVITY_GRADE'].str.split(","‌​)] # temporary 
df['min_node_grade'] = df.groupby('NODE_NAME')['row_min_grade'].transform('min').map(inv_map) 
df['min_activity_grade'] = df.groupby('ACTIVITY_NAME')['row_min_grade'].transform('min').map(inv_map)
df.drop(['row_min_grade'], axis='columns') # drop temporary column
```


  [1]: https://i.sstatic.net/TRnMn.png
  [2]: https://i.sstatic.net/K3Hbs.png
  [3]: https://i.sstatic.net/XAQiu.png
  [4]: https://i.sstatic.net/lyLfv.png
  [5]: https://i.sstatic.net/PNRW2.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-26): Thanks!! Getting errors trying this (argument of type 'float' is not iterable). Deeply apologize for type-os; spent hours trying post fake data (see comments). There aren't leading strings.  Based on your response, trying: temp_gr_list=df_has_activity['ACTIVITY_GRADE'].str.split(",") #produces  [Kindergarten, PreK]. Nd to turn into indices and take min. Try test_gr_index = list(map(lambda x: x.replace(grade_to_index), test_gr_list))  >>“'list' object has no attribute 'replace'” test_gr_index =  [i.str.replace(grade_to_index) for i in test_gr_list] >>“'list' object has no attribute 'str'”
- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-26): Update: I've spent two hours trying to reformat the data into a markup, sanitize it, and make it illustrative so that I could re-post the question, and I can't do it successfully. Can you please tell me: I really think that some combination of strip > make it a list > map the list to indexes > take the minimum is what I need, but I can't make it work. Help very much appreciated!
- **me** (2023-03-26): @CiviLearner about the *“'list' object has no attribute..."* errors, *`[Kindergarten, PreK]`* [or any other value in `temp_gr_list`, and I'm assuming the same for `test_gr_list` values] is a [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) so you can't treat them like pandas [Series](https://pandas.pydata.org/docs/reference/series.html)
- **me** (2023-03-26): .you could try something like `test_gr_index = [[grade_to_index.get(i,i) for v in i] for i in test_gr_list]` but note that you'll end up with a list of lists of indices, not a flat list of indices like you would with `test_gr_index = [min([grade_to_index.get(i,i) for v in i]) for i in test_gr_list]`
- **me** (2023-03-26): Also, you should keep in mind that [`str.replace`](https://www.programiz.com/python-programming/methods/string/replace) is **NOT the same** as [`Series.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html)
- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-26): Hm. I'm not sure how to get from your comment about "a list of lists with indices" to the minimum node grade-->  For a given node, I have a row 1 with activity_grade = Kindergarten, Pre-K, and row2 with activity_grade = Kindergarten, 1st Grade. **My goal is to get the node_min_grade = Pre-K**. How can I use split on activity_grade to turn them into a list e.g. [Pre-K, Kindregarten] then map the activity grades to an index e.g. [-1,0] -- this is the part that is erroring out-- ,then take the minimum by activity and then by node? Thanks!
- **me** (2023-03-26): @CiviLearner sounds very much like what my answer is doing [is it not giving your desired results?], but to break it down,
- **me** (2023-03-26): minimum grade index by row <--- `df['row_min_grInds'] = [min([grade_to_index.get(i,i) for v in i]) for i in test_gr_list]` [the flat list I mentioned before]
- **me** (2023-03-26): minimum grade index by activity <--- `df['activity_min_grInds'] = df.groupby('ACTIVITY_NAME')['row_min_grInds'].transform('min')` [this wasn't something I realized you wanted before]
- **me** (2023-03-26): minimum grade by node <--- `df['node_min_inds'] = df.groupby('NODE_NAME')['activity_min_grInds'].transform('min').map(inv_map)`
- **me** (2023-03-26): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/252797/discussion-between-driftr95-and-civilearner).

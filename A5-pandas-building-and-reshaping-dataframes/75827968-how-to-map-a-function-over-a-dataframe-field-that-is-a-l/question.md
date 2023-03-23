---
title: "How to map a function over a dataframe field that is a list"
site: stackoverflow
question_id: 75827968
url: https://stackoverflow.com/q/75827968
asked: 2023-03-23T21:04:00Z
asked_by: "CiviLearner"
asked_by_url: https://stackoverflow.com/users/20429165
last_edited: 2023-03-26T15:09:04Z
last_editor: "harriet"
last_editor_url: https://stackoverflow.com/users/17433572
tags: [python, dictionary, group-by, split]
score: 0
views_at_snapshot: 242
answer_count: 2
accepted_answer_id: 75845119
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f86c8d57f57b96e415db0d3782a574037ea891fb9380a883bed30dc7489537c2
---

# How to map a function over a dataframe field that is a list

Asked by [CiviLearner](https://stackoverflow.com/users/20429165) on Stack Overflow, <https://stackoverflow.com/q/75827968>, 2023-03-23, last edited 2023-03-26 by [harriet](https://stackoverflow.com/users/17433572). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have spent hours troubleshooting this and really appreciate your help!

Each node can have multiple activities, and each activity can have up to two associated grades, which were an ARRAY type in SQL. My goal is to get the minimum activity grade for each node. I imported the ACTIVITY_GRADE field using ARRAY_TO_STRING(ACTIVITY_GRADE) AS ACTIVITY_GRADE (there might be a better way to import it to make it a list I can iterate over?) 

The data looks like the below, and my goal is to get the last column as it is shown: min_node_grade.




<pre>STUDENT_ID	RECORD_ID	   NODE_NAME ACTIVITY_NAME	ACTIVITY_GRADE	     GOAL = GET THIS min_node_grade
FredID	   gobbledeegook1	Node1	MyActivity1	   PreK, Kindergarten	PreK
FredID	   gobbledeegook2	Node1	MyActivity1	   Kindergarten	        PreK
FredID	   gobbledeegook3	Node2	MyActivity2	   1st Grade	        1st Grade
JaniceID   gobbledeegook4	Node3	MyActivity3	   Kindergarten	        Kindergarten
JaniceID   gobbledeegook5	Node3	MyActivity3	   1st Grade	        Kindergarten</pre>



I have gone a likely unnecessarily complicated route. How can I create a function that will map the grade_to_index dictionary across each value of the comma-separated string that is ACTIVITY_GRADE, take the minimum for that activity, then group by node and take the min over the node's activities?

```
#split it into two columns
df[['activity_grade_a', 'activity_grade_b']] = df.ACTIVITY_GRADE.str.split(",", expand = True)

#map it to integers so can take min to identify grade
grade_to_index = {"Preschool": -2, "Pre-K": -1, "Kindergarten": 0, "1st Grade": 1, '2nd Grade':2,'3rd Grade':3,'4th Grade':4,'5th Grade':5}

#map to invert the dictionary in order to get it back to text form
inv_map = {v: k for k, v in grade_to_index.items()}

#create columns with the index for the one or two grades. 
df['activity_grade_a_index']=df['activity_grade_a'].replace(grade_to_index)
df['activity_grade_b_index']=df['activity_grade_b'].replace(grade_to_index)

#get minimum of each row across the two columns; axis=1 says looks across columns
df['activity_min_grade_index'] = df[['activity_grade_a_index', 'activity_grade_b_index']].min(axis=1)

#group by node and get the minimum of activity-level minimums, map it to a new field
df['min_node_grade_index']=df.groupby('NODE_NAME')['activity_min_grade_index'].transform('min')

#get the grade back
df['min_node_grade']=df['min_node_grade_index'].replace(inv_map)`
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[juanpa.arrivillaga](https://stackoverflow.com/users/5014455)** (2023-03-23): you really need to provide a [mcve]. If you are asking about pandas, provide an example *input dataframe* and the corresponding *example output dataframe*. Don't give us vague descriptions
- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-25): Thank you for the feedback! New poster here. I have edited the text to hopefully clarify. (I have read at least 5 StackExchange posts trying to figure out how to copy/paste a table into this post and they tell me to use Markdown format, but not how to achieve that. I've tried pasting it from Word...Notepad...I put it into a Jupyter Notebook markdown cell and copied from there...I tried a Latex table generator.... How do I get it into the right format?)
- **me** (2023-03-25): @CiviLearner you can print or save markdown with [`.to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html) like  *`print(df.loc[:5].to_markdown(index=False))`* ([view sample output](https://i.sstatic.net/baKXf.png)). If you you paste that markdown in your question (make sure to leave an empty line before and after), then anyone can access it with [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) like *`pd.read_html(link_to_this_question)[0]`*
- **me** (2023-03-25): You can also use [`.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) to covert the DataFrame to dictionary ([view sample output](https://i.sstatic.net/8qmCl.png)) [it's just a little bit better for preserving data-types], and then anyone could copy it and reproduce some of your `df`
- **[CiviLearner](https://stackoverflow.com/users/20429165)** (2023-03-26): Thanks! I used print(df.loc[:5].to_markdown(index=False))...but then I need to bring the data into something to sanitize it and remove IDs and such. So I exported the markdown to Jupyter Notebook and am attempting to work with it (insert 2 hours here...). I'll get there! Any way to take something from Excel and put it into Markdown?
- **me** (2023-03-26): @CiviLearner yes, you can just just use [`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) first like `print(pd.read_excel(path_to_excel_file).to_markdown(index=False))` [include the `sheet_name` argument if you're reading from a file with multiple sheets]

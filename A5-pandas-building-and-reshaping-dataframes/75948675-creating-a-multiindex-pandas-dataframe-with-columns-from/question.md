---
title: "Creating a MultiIndex pandas dataframe with columns from Excel files"
site: stackoverflow
question_id: 75948675
url: https://stackoverflow.com/q/75948675
asked: 2023-04-06T10:53:03Z
asked_by: "user2078621"
asked_by_url: https://stackoverflow.com/users/2078621
last_edited: 2023-04-06T17:19:41Z
tags: [python, pandas, dataframe, multi-index]
score: -1
views_at_snapshot: 150
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c4b9cadce5749848bace388cbcc4dc8889cc1bde5f9f218137fc8586c7910e24
---

# Creating a MultiIndex pandas dataframe with columns from Excel files

Asked by [user2078621](https://stackoverflow.com/users/2078621) on Stack Overflow, <https://stackoverflow.com/q/75948675>, 2023-04-06, last edited 2023-04-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I managed to add lower-levels to MultiIndex as shown here using `.stack()`:

https://stackoverflow.com/questions/42612236/how-can-i-add-a-level-to-a-multiindex

With

```
lists

[('C5P', 'CI3'),
 ('C2P', 'CI4'),
 ('C1', 'CI3'),
 ('C7', 'CI4'),
 ('C3P', 'CI1'),
 ('C3P', 'CI2'),
 ('C4', 'CI1'),
 ('C3P', 'CI3'),
 ('C4P', 'CI4'),
 ('C5P', 'CI2'),
 ('C4P', 'CI3'),
 ('C3P', 'CI4'),
 ('C2P', 'CI2'),
 ('C6', 'CI2'),
 ('C7', 'CI2'),
 ('C7', 'CI3'),
 ('C1P', 'CI1'),
 ('C2P', 'CI3'),
 ('C2', 'CI1'),
 ('C4P', 'CI2'),
 ('C2', 'CI2'),
 ('C3', 'CI2'),
 ('C1P', 'CI2'),
 ('C6', 'CI1'),
 ('C3', 'CI3'),
 ('C1', 'CI1'),
 ('C5P', 'CI1'),
 ('C3P', 'CI4'),
 ('C5', 'CI2'),
 ('C4', 'CI2')]

index = pd.MultiIndex.from_tuples(lists,names=['borehole','sample'])

d = pd.DataFrame(data=1,index=index, columns=['1','2','3']).stack()
e = pd.DataFrame(data=1,index=d.index, columns=['p','q']).stack()
```

The result is something like:

```
borehole  sample      
C4        CI1     1  p    1
                     q    1
                  2  p    1
                     q    1
                  3  p    1
                     q    1
          CI2     1  p    1
                     q    1
                  2  p    1
                     q    1
                  3  p    1
                     q    1
C5P       CI3     1  p    1
                     q    1
                  2  p    1
                     q    1
                  3  p    1
                     q    1
          CI2     1  p    1
                     q    1
                  2  p    1
                     q    1
                  3  p    1
                     q    1
          CI1     1  p    1
                     q    1
                  2  p    1
                     q    1
                  3  p    1
                     q    1
```

What I would actually like to obtain is to have this arranged in columns and populate columns 'p' and 'q' from Excel files. I am stuck at trying to assign data to p and q.
Sample data as follows:
```
borehole	C5P						
sample	    CI2						
specimen	1		                2		                3		
	        p	        q	        p	        q	        p	        q	
	        140.5745654	90.9496963	157.5959379	101.2858137	236.882037	105.4921111	
	        140.8908259	91.01647765	157.4825549	101.4976646	236.6523714	105.2591143	
	        141.1076296	91.08488883	157.3080705	101.8022116			
	        141.3524628	91.17138846	157.3539987	102.167996			
	        143.2526588	92.28797636					
	        143.776291	92.62887289
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-04-06): Your example is not reproducible, missing `index`.
- **me** (2023-04-06): What do your excel file and your `index` variable look like?
- **[user2078621](https://stackoverflow.com/users/2078621)** (2023-04-06): @Driftr95, excel files with q p columns of equal length but varying from file to file
- **me** (2023-04-06): @user2078621 but what are the contents of the columns in the files like? how do you want to line them up with your `index`? do you just want to use the values in the columns repeated like you are with `[1,2,3]` and `['p','q']`?
- **[user2078621](https://stackoverflow.com/users/2078621)** (2023-04-06): @Driftr95 edited with sample data
- **me** (2023-04-06): @user2078621 Are specimens 1, 2, and 3 from the same file? Would you mind using `df.to_dict('tight')` so I can reproduce it exactly?

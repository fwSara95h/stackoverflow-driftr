---
title: "Check if column name from one dataframe matches with index value of another dataframe and populate value into a new column"
site: stackoverflow
question_id: 74790102
url: https://stackoverflow.com/q/74790102
asked: 2022-12-13T19:40:49Z
asked_by: "Newlearner"
asked_by_url: https://stackoverflow.com/users/19921895
last_edited: 2022-12-13T19:58:03Z
tags: [python, pandas, dataframe]
score: 1
views_at_snapshot: 276
answer_count: 2
accepted_answer_id: 74790535
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f78264d2ae9a211c3b1eef590774c82cd5a9b3afe45debeeb3623dd3122f0c68
---

# Check if column name from one dataframe matches with index value of another dataframe and populate value into a new column

Asked by [Newlearner](https://stackoverflow.com/users/19921895) on Stack Overflow, <https://stackoverflow.com/q/74790102>, 2022-12-13, last edited 2022-12-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have two dataframes, df_rates and df_profit as shown below. df_rates has a time-date value its column name with values as certain rates and the index values denotes the minutes before the time-date value of the column. (i.e. row 1 denotes 0 mins before 2012-03-31 23:45:00, row 2 denotes 5 mins before  2012-03-31 23:45:00 and so on).  Whereas df_profit has timestamps as its index and there is a  Profit column.

I want to add the Profit column from df_profit as a new column to df_rates under the following condition:

1\.       If the timestamp (2012-03-31 23:45:00) at index of df_profit matches with the column name of df_rates (2012-03-31 23:45:00), then populate the new column with the corresponding profit value (354.664).

2\.       The next value (125.76) in line from Profit column of df_profit, where the timestamp is ‘2012-03-31 23:30:00’ should be populated in the new column against row where ‘Mins before time’ is 15 and so on. (Since the difference in time between 2012-03-31 23:45:00 and 2012-03-31 23:30:00 is 15 mins)

I have been trying a lot on how to do it but I am at a loss. Could someone please help or guide with this?

```
df_rates
Mins before time	 2012-03-31 23:45:00
0	                     113.1
5	                     112.1
10	                     113.1
15	                     113.17
20	                     103.17
25	                     133.17
30	                     101.39


df_profit
	                     Profit
2012-04-01 00:30:00	     251.71
2012-04-01 00:15:00	     652.782
2012-04-01 00:00:00	     458.099
2012-03-31 23:45:00	     3504.664
2012-03-31 23:30:00	     1215.76
2012-03-31 23:15:00	    -21.48
2012-03-31 23:00:00	    -8.538
	

Expected dataframe:
Mins before time	2022-01-31 23:45:00+01:00	New_column
0	                   113.1	                 3504.664
5	                   112.1	
10	                   113.1	
15	                   113.17	                 1215.76
20	                   103.17	
25	                   133.17	
30	                   101.39	                 -21.48
```

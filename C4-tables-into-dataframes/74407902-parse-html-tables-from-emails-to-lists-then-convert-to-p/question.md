---
title: "Parse html tables from emails to lists then convert to pandas dataframe"
site: stackoverflow
question_id: 74407902
url: https://stackoverflow.com/q/74407902
asked: 2022-11-11T20:39:58Z
asked_by: "Dante"
asked_by_url: https://stackoverflow.com/users/20191122
last_edited: 2022-11-13T22:28:43Z
tags: [python, pandas, beautifulsoup]
score: -1
views_at_snapshot: 790
answer_count: 1
accepted_answer_id: 74421202
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9688471b2d94df8e6dcc8a27c2c18b16ebb4cadc7591a89067367fbb3fc109bb
---

# Parse html tables from emails to lists then convert to pandas dataframe

Asked by [Dante](https://stackoverflow.com/users/20191122) on Stack Overflow, <https://stackoverflow.com/q/74407902>, 2022-11-11, last edited 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I’m  an absolute Beginner in Python , and I am trying to create a script which loops through an email folder and grabs a html table within the emails and convert to a pandas dataframe for export to excel.

The code below loops through the folder and adds each table and its contents to a list []
```
# importing the libraries
import pandas as pd
import win32com.client
from bs4 import BeautifulSoup


# connect to outlook email inbox
outlook = win32com.client.Dispatch("Outlook.Application")
mapi= outlook.GetNamespace("MAPI")

inbox = mapi.Folders['emailaddress'].Folders['Inbox'].Folders['Testfolder']
Mail_Messages = inbox.Items


# loop through email folder and seach for table in email messages and add to a list

output = []
for mail in Mail_Messages:
    body = mail.HTMLBody
    html_body = BeautifulSoup(body,"lxml")
    html_tables = html_body.find('table')
    
    # read html table to dataframe list

    df = pd.read_html(str(html_tables))
    #pd.concat(df).set_index(0).T
    df= df[0].set_index(0).T
    df.reset_index(level=None, drop=True, inplace=False, col_level=0, col_fill='')
    output.append(df)

    #print (df)
    
print(output)

[0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8
1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8, 0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8
1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8, 0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8
1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8]


```
What I’m trying to achieve is, for every table in the email folder add the table to a new row  
So it would finally end up something like this 
```
Column1	Column2	Column3	Column4	Column5	Column6	Column7	Column8
Value1	Value2	Value3	Value4	Value5	Value6	Value7	Value8
```
I’m struggling to get the lists that are created into a structure that could be converted into a pandas dataframe to be exported to excel.

As I’ve said I’m a beginner , and looking some help on how this could be achieved.

Here's a screenshot of the table i'm tring to grab.. 
[![Picture of the table in the email below.][1]][1]


  [1]: https://i.sstatic.net/fRXcC.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Scott Boston](https://stackoverflow.com/users/6361531)** (2022-11-11): `df[0].set_index(0).T` pd.read_html returns a list of dataframes, you havea list with one dataframe. df[0] gets the first element of this list.  Next, use set index to move column 0, into the index you may need set_index('0') depending on if that column headers is a string or integer. Last, transpose the dataframe.
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-11): Thanks Scott !!! that helps,  how could this work in a loop when there could be multiple tables to bring together in one dataframe?
- **me** (2022-11-13): @Dante `pd.concat(df).set_index(0).T` to combine all tables in `df` before transposing
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-13): @Driftr95 , i'm still struggling to get the lists into a dataframe to export to excel. i currently get this as the output for the 3 emails that contain the tables. [0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8 1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8, 0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8 1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8, 0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8 1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8]

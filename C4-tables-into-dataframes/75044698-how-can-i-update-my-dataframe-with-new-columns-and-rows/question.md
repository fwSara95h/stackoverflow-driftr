---
title: "How can I update my Dataframe with new columns and rows while webscraping?"
site: stackoverflow
question_id: 75044698
url: https://stackoverflow.com/q/75044698
asked: 2023-01-08T00:19:34Z
asked_by: "Shattered"
asked_by_url: https://stackoverflow.com/users/20954937
last_edited: 2023-01-09T01:23:47Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, pandas, dataframe, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 57
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1b75be60c46f153b7086446fe213d62daf2d46906dd08c4a1671c3a112157342
---

# How can I update my Dataframe with new columns and rows while webscraping?

Asked by [Shattered](https://stackoverflow.com/users/20954937) on Stack Overflow, <https://stackoverflow.com/q/75044698>, 2023-01-08, last edited 2023-01-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to create a webscraping tool that will update a Dataframe with data from multiple tables.
The page I'm working on has a base table in which every row has a link that directs you to a new URL that has a secondary table with the data I'm looking for. 
My objective is to create a unique Dataframe comprehensive of all the data present on all secondary tables of the site. 
Problem is, every secondary table can have different sets of columns from the previous one, depending on whether that secondary table has a value for that specific column or not, and I cannot know all the possibile column types


I tried multiple solutions. What I'm working on at the moment is to create a for loop that constantly create a new Dataframe out of the new tables and merge them to the previous one.
But I'm stuck on trying to merge the two Dataframes on all the columns they have in common.
Please forgive me if I made amateur mistakes, I've been using python only for a week.

```

#create the main DataFrame
link1= links[0]
url_linked = url_l + link1
page_linked = requests.get (url_linked)
soup_linked = BeautifulSoup(page_linked.text,'lxml')
table_linked= soup_linked.find('table', class_="XXXXX")

headers_link=[]
headers_unique=[]
for i in table_linked.find_all('th'):
    title_link=i.text
    title_link=map(str,title_link)
    headers_link.append(title_link)

headers_unique=headers_link
mydata_link = pd.DataFrame(columns=headers_link)


count = 1

for link in links:
    url_linked = url_l + link
    page_linked = requests.get (url_linked)
    soup_linked = BeautifulSoup(page_linked.text,'lxml')
    table_linked= soup_linked.find('table', class_="table table-directory-responsive")

    row2=[]
    n_columns =len(table_linked.find_all('th'))

    #populating the main dataframe

    if count == 1:
        for j in table_linked.find_all('tr'):
            row_data=j.find_all('td')
            row=[i.text for i in row_data]
            row2.append(row)
        
        lenght_link= len(mydata_link)
        row2.remove(['']) #To get rid of empty rows that have no th
        mydata_link.loc[lenght_link]=row2 
        print(mydata_link)

        print('Completato link '+ str(count))
        count= count+1


    #creating the secondary Dataframe
    else:      
        headers_test=[]
        for i in table_linked.find_all('th'):
            title_test=i.text
            title_test=map(str,title_test)
            headers_test.append(title_test)

        mydata_temp=pd.DataFrame(columns=headers_test)

        for j in table_linked.find_all('tr'):
            row_data=j.find_all('td')
            row=[i.text for i in row_data]
            row2.append(row)
        
        lenght_link= len(mydata_link)
        row2.remove(['']) #To get rid of empty rows that have no th
        mydata_temp.loc[lenght_link]=row2
        print(mydata_temp)
        

        #merge the two DataFrames based on the unique set of columns they both have

        headers_unique= set(headers_unique).intersection(headers_test)
        mydata_link=mydata_link.merge(mydata_temp, on=[headers_unique], how='outer')
        print(mydata_link)
        print('Completed link '+ str(count))
        count= count+1

```

What I need is basically a function that, given these sample dataFrames:

| A     | B    | C    |
|:----: |:----:|:----:|
| 1     | 2    |  3   |   

| C    | A    |    D | E    |
|:----:|:----:|:----:|:----:|
| 4    | 5    |    6 | 7    |

Will return the following dataframe:

| A    | B    |    C | D    | E     |
|:----:|:----:|:----:|:----:|:-----:|
| 1    | 2    |    3 | Nan  | Nan   |
| 5    | Nan  | 4    | 6    | 7     |

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-01-08): could you include some of the tables for example and a sample of how you would like the merged table to look based on those?
- **[gregV](https://stackoverflow.com/users/8115653)** (2023-01-08): [https://stackoverflow.com/questions/20109391/how-to-make-good-reproducible-pandas-examples]

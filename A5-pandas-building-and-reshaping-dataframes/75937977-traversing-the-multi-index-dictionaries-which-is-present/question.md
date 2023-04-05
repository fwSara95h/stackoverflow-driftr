---
title: "traversing the multi index dictionaries which is present in dataframe & store the values in a list"
site: stackoverflow
question_id: 75937977
url: https://stackoverflow.com/q/75937977
asked: 2023-04-05T09:49:01Z
asked_by: "lifo"
asked_by_url: https://stackoverflow.com/users/10484786
last_edited: 2023-04-06T20:36:50Z
tags: [python, dataframe, csv, dictionary]
score: -1
views_at_snapshot: 96
answer_count: 2
accepted_answer_id: 75943895
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7ef7f341983d502cfd1c384c908bbc342146b67483aa4417023e0104182ef5b9
---

# traversing the multi index dictionaries which is present in dataframe & store the values in a list

Asked by [lifo](https://stackoverflow.com/users/10484786) on Stack Overflow, <https://stackoverflow.com/q/75937977>, 2023-04-05, last edited 2023-04-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.




**The above link contains the data frame, it has 2 columns [CREATEDAT, RESPONSE], the objective is to traverse the response column and in that response column there is an estimate key, in that key, I have to fetch the provider&storeexternalid**

adding the sample row in a snippet, the location is ['store-boundary-dsp']['estimates']

I have written a function, it might require some modification adding in the snippet

```py
def traverse_dsp(data_frame,column):
    provider = []
    store_id= []

    #Iterate over each row in Dataframe
    for index, row in data_frame.iterrows():
        
        # Iterate over each json object in each row in DataFrame
        for i in range(0,len(row[column])):

            for k,v in row[column]['store-boundary-dsp']['estimates'][i].items():

                if k=="storeExternalId":

                    store_val=v
                    store.append(store_val)

                if k=="provider":

                    provider_val=v
                    provider.append(provider_val)

               

    return provider,store_id
```


```py

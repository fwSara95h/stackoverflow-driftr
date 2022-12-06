---
title: "Getting Error here in web scraping using python"
site: stackoverflow
question_id: 74701159
url: https://stackoverflow.com/q/74701159
asked: 2022-12-06T10:46:16Z
asked_by: "Binod Binod"
asked_by_url: https://stackoverflow.com/users/20701404
last_edited: never
tags: [python-3.x, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 176
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d1c6b3f41882ddfaefbfbc721eb79b8f2c419a7c4f6d3148636b624471289f55
---

# Getting Error here in web scraping using python

Asked by [Binod Binod](https://stackoverflow.com/users/20701404) on Stack Overflow, <https://stackoverflow.com/q/74701159>, 2022-12-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Running this code but dont know why its shoeing error??

```
#extracting text from all the url
url_id=1
for i in range(0,len(df)):
 
   j=df.iloc[i].values
   
   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}#giving user access
   page=requests.get(j[0],headers=headers)#loading text in url
   soup=BeautifulSoup(page.content,'html.parser')#parsing url text
   content=soup.findAll(attrs={'class':'td-post-content'})#extracting only text part
   content=content[0].text.replace('\xa0',"  ").replace('\n',"  ")#replace end line symbol with space 
   title=soup.findAll(attrs={'class':'entry-title'})#extracting title of website
   title=title[16].text.replace('\n',"  ").replace('/',"")
   text=title+ '.' +content#merging title and content text
   text=np.array(text)#converting to array form
   text.reshape(1,-1)#changing shape to 1d 
   df1=pd.Series(text)#creating series data frame
   b=str(url_id)+"."+'txt'#name of the text file
  # with open(b, 'a') as f:#creating text file 
   # df1.to_csv(f, line_terminator=',', index=False, header=False)
  # files.download(b)#downloading text file
   url_id+=1
```


here its showing as



```
IndexError                                Traceback (most recent call last)
Input In [36], in <cell line: 3>()
      9 soup=BeautifulSoup(page.content,'html.parser')#parsing url text
     10 content=soup.findAll(attrs={'class':'td-post-content'})#extracting only text part
---> 11 content=content[0].text.replace('\xa0',"  ").replace('\n',"  ")#replace end line symbol with space 
     12 title=soup.findAll(attrs={'class':'entry-title'})#extracting title of website
     13 title=title[16].text.replace('\n',"  ").replace('/',"")

IndexError: list index out of range
```

not able to understand why???
help with this problem..

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-06): Your list is empty and you can't use `[0]` on `content`.
- **[Community](https://stackoverflow.com/users/-1)** (2022-12-06): Please edit the question to limit it to a specific problem with enough detail to identify an adequate answer.

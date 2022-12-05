---
title: "How to create proper formatted JSON file with BeautifulSoup scraped information?"
site: stackoverflow
question_id: 74682012
answer_id: 74693810
url: https://stackoverflow.com/a/74693810
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-05T20:05:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74693810/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0182db296bb9bb9926ee6cd44899a11d82fac12f9d4267fb0010a6811f8031d7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74693810>, 2022-12-05; score 0. Text as retrieved 2026-10-12.

<sub>**Note: you shouldn't write to a json file in parts like your code is doing - that's not valid json.**</sub>

> I've tried moving the j variable outside the loop and writing the title, but can't seem to figure out how to combine the looped variable with the other one

<br>
 
Method 1: combine title and images after the loop

```python
title = soup.find('em', class_='gravel-text').text

imgLinks = []
for images in soup.find_all('div', class_='thumb-frame'):
    imgLinks.append(images.a['href']) 

j = [{'title':title, 'image':imgLinks}]
# dump j, write to and close jfile #
```

<br>
 
Method 2: initiate `j` before loop

```python
j = [{'title':soup.find('em', class_='gravel-text').text, 'image':[]}] 
for images in soup.find_all('div', class_='thumb-frame'):
    j['image'].append(images.a['href']) 

# dump j, write to and close jfile
``` 

<br>
 
Method 3: all in one statement

```python
url = "https://stock.adobe.com/search?k=interstellar%20movie"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")


with open('images.json', 'w') as jfile:
    json.dump([{'title': soup.find('em', class_='gravel-text').text, 'image': [
        image.a['href'] for image in soup.find_all('div', class_='thumb-frame')
    ]}], jfile)
```

<br>
 
Method 4: what I consider the safes way to avoid raising errors [but don't use this if you *want* to raise errors when the site is in an unexpected/inconsistent format]

```python
url = "https://stock.adobe.com/search?k=interstellar%20movie"
page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")


title = soup.find('em', class_='gravel-text')
title = '! MISSING TITLE !' if title is None else title.text

imgLinks = [
    image.select_one('a[href]').get('href') for image in 
    soup.select('div[class="thumb-frame"]:has(a[href])')
]

with open('images.json', 'w') as jfile:
    json.dump([{'title':title, 'image':imgLinks}], jfile)
```

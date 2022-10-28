---
title: "How to download image from URL using beautiful soup in high quality?"
site: stackoverflow
question_id: 74236926
answer_id: 74237830
url: https://stackoverflow.com/a/74237830
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T15:49:17Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74237830/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a5796aa1f4eecb1cf5c442782654b10454b49223f721a681c0bf406d044a11de
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74237830>, 2022-10-28; score 0. Text as retrieved 2026-10-12.

You might try this:

```python
with open('cat.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        imagesname = ' '.join(row)
        r = requests.get(imagesname)

        soup = bs(r.content, 'html.parser') 
        tables = soup.find_all('img', class_='pick')

        inParsed = urllib.parse.urlparse(imagesname) # break down url
        rootUrl = f'{inParsed.scheme}://{inParsed.netloc}' # to get root
  
        for image in tables:
            imageUrl = urllib.parse.urljoin(rootUrl, imageUrl.get('src')) # add root to src
            saveImgAs = [u for u in imageUrl.split('/') if u][-1] # get name from link

            with open(saveImgAs, "wb") as f:
                f.write(requests.get(imageUrl).content) # download
                f.close()
            
            print(saveImgAs, image)
```

I'm not entirely sure about the formation of `imageUrl` nor of how consistent your image `src` values might be - if I had a few of your `row` values, I would have been able to run a few tests first, but hopefully this works

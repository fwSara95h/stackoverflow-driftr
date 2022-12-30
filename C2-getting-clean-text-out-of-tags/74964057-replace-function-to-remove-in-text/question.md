---
title: "replace function to remove \"\\\" in text"
site: stackoverflow
question_id: 74964057
url: https://stackoverflow.com/q/74964057
asked: 2022-12-30T17:07:16Z
asked_by: "Digiprisme Digi"
asked_by_url: https://stackoverflow.com/users/20216073
last_edited: 2022-12-30T17:13:22Z
tags: [python, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 96
answer_count: 2
accepted_answer_id: none
closed: 2026-08-12T10:35:56Z (Not suitable for this site)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f9b08d5933734c880767566aab8fcfc7a61fa3ea69e530b7e05a2d6365931716
---

# replace function to remove "\" in text

Asked by [Digiprisme Digi](https://stackoverflow.com/users/20216073) on Stack Overflow, <https://stackoverflow.com/q/74964057>, 2022-12-30, last edited 2022-12-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

hello i hope someone  can help me with this issue 
so i trying to scrapp iframe tag in a web page but i get some backslashes which i want to remove



i select the element 
```
video=soup_product.select_one("div.col-lg-6:nth-of-type(3)>iframe")

```
and this is printing result :
```
<iframe allowfullscreen=\"\" frameborder=\"0\" height=\"170\" src=\"https://www.youtube.com/embed/JwG10b9HtZQ\" width=\"305\"></iframe>
```

 i tried too replace the backslash with replace function
```
str(video).replace('\', '')
```
but it show error

File "<string>", line 2
    videoiframe = str(video).replace("\", "")
                                ^
SyntaxError: EOL while scanning string literal

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2022-12-30): _but it show error on syntax_ Show us the error.  Otherwise we can only guess what it is.
- **[Digiprisme Digi](https://stackoverflow.com/users/20216073)** (2022-12-30): sorry i forgot to mention the error i updated the question
- **[John Gordon](https://stackoverflow.com/users/494134)** (2022-12-30): You need one more backslash.  `str(video).replace('\\', '')`
- **[kaispace30098](https://stackoverflow.com/users/19854159)** (2022-12-30): https://stackoverflow.com/questions/10585349/python-how-to-replace-backslash-with-re-sub

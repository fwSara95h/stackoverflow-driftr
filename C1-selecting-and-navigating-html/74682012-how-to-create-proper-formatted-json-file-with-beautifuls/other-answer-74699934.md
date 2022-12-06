---
title: "How to create proper formatted JSON file with BeautifulSoup scraped information?"
site: stackoverflow
question_id: 74682012
answer_id: 74699934
url: https://stackoverflow.com/a/74699934
author: "Tejas Pendse"
author_url: https://stackoverflow.com/users/1197425
posted: 2022-12-06T09:15:12Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4ba001a1b6a0a5a891d312e719a22121e5fb35992e16084d3bc83fa8afb5f622
role: another answer on the same question, kept as context; not my work
---

# Answer by [Tejas Pendse](https://stackoverflow.com/users/1197425) — 2022-12-06

Posted on Stack Overflow, <https://stackoverflow.com/a/74699934>, 2022-12-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The problem is this part `j = [{'title':title, 'image':image}]` in each for loop iteration. You are trying to write merged data without parsing over entire list

What you need to do is to merge state on each iteration & write once everything is parsed. For your desired output you want mapping between `title` and multiple `image`s - so you can use a [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

    data = {}
    for images in soup.find_all('div', class_='thumb-frame'):
        image = images.a['href']
        if title in data:
            data[title].append(image)
        else
            data[title] = [image]

    # Once all data is collated, format and write it out
    # Using list and dict comprehension together to do the heavy lifting for you
    formatted = [ {'title':title, 'image':images} for title,images in data.items() ]

    with open('images.json', 'w') as out_json:
        json.dump(data, out_json)

Check out [list & dict comprehension](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement), as well as the [with statement to handle file I/O](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

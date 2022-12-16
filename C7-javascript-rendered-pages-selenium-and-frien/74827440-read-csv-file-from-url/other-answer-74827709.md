---
title: "Read csv file from url"
site: stackoverflow
question_id: 74827440
answer_id: 74827709
url: https://stackoverflow.com/a/74827709
author: "Je Je"
author_url: https://stackoverflow.com/users/1536343
posted: 2022-12-16T17:15:08Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e7890d1e5afbf8aa69cbc942860416c0a2d87201b52bf13069fdb1bd1006a05
role: another answer on the same question, kept as context; not my work
---

# Answer by [Je Je](https://stackoverflow.com/users/1536343) — 2022-12-16

Posted on Stack Overflow, <https://stackoverflow.com/a/74827709>, 2022-12-16. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

you could rewrite your code using functions to deal with each step of your code.

```

def read_file(has_header:bool=True):
    with open("data.csv") as file:
        start_urls = [line.strip() for line in file]

    # assumes there is a header
    if has_header:
        return start_urls[1:]
    else:
        return start_urls

def scrap_urls():
    urls = read_file(has_header=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for url in urls:
        driver.get(url)

if __name__ == '__main__':
    
    scrap_urls()

```

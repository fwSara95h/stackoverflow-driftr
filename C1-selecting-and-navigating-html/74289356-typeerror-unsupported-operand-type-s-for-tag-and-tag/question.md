---
title: "TypeError: unsupported operand type(s) for +=: 'Tag' and 'Tag'"
site: stackoverflow
question_id: 74289356
url: https://stackoverflow.com/q/74289356
asked: 2022-11-02T12:44:13Z
asked_by: "ArshiyaZandi"
asked_by_url: https://stackoverflow.com/users/14927169
last_edited: 2022-11-04T13:31:22Z
tags: [python, html, web-scraping, beautifulsoup, type-conversion]
score: -1
views_at_snapshot: 242
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 91c222d340a97850c7e42527ab40ccc5ca538abcf703013f2908885632bff7c7
---

# TypeError: unsupported operand type(s) for +=: 'Tag' and 'Tag'

Asked by [ArshiyaZandi](https://stackoverflow.com/users/14927169) on Stack Overflow, <https://stackoverflow.com/q/74289356>, 2022-11-02, last edited 2022-11-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrap HTML data from a website and then add my own CSS style to the code. I'm using Beautiful soup to scrap the data and convert my own <style> tag to HTML.

This is the code
```
        word = t.clipboard_get()

        # Web Scrapping
        url="https://www.vajehyab.com/?q="

        response = requests.get(f"{url}{word}")
        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find(["div", "style"], attrs={"id": "wordbox"},)


        # Style
        style = """<style>
            #wordbox{
                width: 500px;
            }
        </style>"""

        css_to_tag = BeautifulSoup(style, 'html.parser')
        css = css_to_tag.find("style")

        meaning += css
```


But in the last line, when I try to combine them I get this error: 
      TypeError: unsupported operand type(s) for +=: 'Tag' and 'Tag'

Is there any way to add HTML tags inside another in beautiful soup

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[LLaP](https://stackoverflow.com/users/2758414)** (2022-11-02): Please provide what {word} is.

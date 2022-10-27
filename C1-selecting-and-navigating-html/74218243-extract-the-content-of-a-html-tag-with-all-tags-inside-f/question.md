---
title: "extract the content of a html tag with all tags inside from beautifulsoup"
site: stackoverflow
question_id: 74218243
url: https://stackoverflow.com/q/74218243
asked: 2022-10-27T07:25:45Z
asked_by: "Mangiafoco"
asked_by_url: https://stackoverflow.com/users/17987787
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 116
answer_count: 2
accepted_answer_id: 74218376
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ebca3bdcafd4c9b45c39573215cc8cae3de8700f64d776c669297bb6bfdafb5c
---

# extract the content of a html tag with all tags inside from beautifulsoup

Asked by [Mangiafoco](https://stackoverflow.com/users/17987787) on Stack Overflow, <https://stackoverflow.com/q/74218243>, 2022-10-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I would like to extract the content of a tag without this tag itself and keeping all the tags inside.

```
html_text = "<TD WIDTH=60%>Portsmouth - Cherbourg<BR/>Portsmouth - Santander<BR/></TD>"
soup = BeautifulSoup(html_text, 'html.parser')
soup_list = soup.find_all("td")
soup_object = soup_list[0]
text = soup_object.getText()
print(soup_object)
```

I get:

> \<td width="60%"\>Portsmouth - Cherbourg\<br/\>Portsmouth - Santander\<br/\>\</td\>

But I want:

> Portsmouth - Cherbourg\<br/\>Portsmouth - Santander\<br/\>

Using :

`soup_object.getText()`

... return:

> Portsmouth - CherbourgPortsmouth - Santander

But it is not what I want.

I know I can get the full content of the tag from a regex:

```
re.search("<td.?>(.)</td>", str(soup_object)).group(1)
```

... but I use BeautifulSoup so I don't have to type this kind of code.

A last thing:

```
soup_object.contents
```

... does not return what i want:

> \['Portsmouth - Cherbourg', \<br/\>, 'Portsmouth - Santander', \<br/\>\]

Am I missing out on a Beautifulsoup feature?

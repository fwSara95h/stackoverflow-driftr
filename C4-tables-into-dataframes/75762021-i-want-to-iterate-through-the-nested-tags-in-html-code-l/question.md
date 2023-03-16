---
title: "i want to iterate through the nested tags in html code like a list or json file"
site: stackoverflow
question_id: 75762021
url: https://stackoverflow.com/q/75762021
asked: 2023-03-16T22:03:33Z
asked_by: "ddd ddd"
asked_by_url: https://stackoverflow.com/users/17535847
last_edited: 2023-03-16T22:07:46Z
last_editor: "Andrej Kesely"
last_editor_url: https://stackoverflow.com/users/10035985
tags: [python, beautifulsoup, html-parsing]
score: -1
views_at_snapshot: 368
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f4c0f2257cf3d3f428d769669490a12fd9b6c1cb43b81963c3c7ac18de130fad
---

# i want to iterate through the nested tags in html code like a list or json file

Asked by [ddd ddd](https://stackoverflow.com/users/17535847) on Stack Overflow, <https://stackoverflow.com/q/75762021>, 2023-03-16, last edited 2023-03-16 by [Andrej Kesely](https://stackoverflow.com/users/10035985). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i have this code for example:

```

<div class = "las">
	<div class = "asas">
      <table style="width:100%">
        <tr>
          <th>Firstname</th>
          <th>Lastname</th> 
          <th>Age</th>
        </tr>
        <tr>
          <td>Jill</td>
          <td>Smith</td>
          <td>50</td>
        </tr>
        <tr>
          <td>Eve</td>
          <td>Jackson</td>
          <td>94</td>
        </tr>
        <tr>
          <td>John</td>
          <td>Doe</td>
          <td>80</td>
        </tr>
      </table>
	</div class = "las">
</div class = "asas">
```
i have saved it in variable called "code", how can i acces the `<td>Smith</td>` tag for example like that: code[0][0][1][1]. i use Beautiful Soup and the only way i know to iterate through the nested tags is with .parents and .children which becomes pretty confusing

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-03-16): Maybe you can convert the table into `pandas` dataframe and select the data from it.

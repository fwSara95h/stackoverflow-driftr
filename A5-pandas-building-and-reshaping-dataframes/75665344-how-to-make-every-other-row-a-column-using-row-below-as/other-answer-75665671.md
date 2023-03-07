---
title: "How to make every other row a column using row below as the value in Pandas?"
site: stackoverflow
question_id: 75665344
answer_id: 75665671
url: https://stackoverflow.com/a/75665671
author: "Serge Ballesta"
author_url: https://stackoverflow.com/users/3545273
posted: 2023-03-07T18:04:46Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1fd066f65b9fd2f4f2c190f260ff8bfd4fdd482475af532b8a906351c305e0ba
role: another answer on the same question, kept as context; not my work
---

# Answer by [Serge Ballesta](https://stackoverflow.com/users/3545273) — 2023-03-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75665671>, 2023-03-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could try to join the dataframe with a shift of it, and pivot the result:

    temp = df.join(df.shift(), rsuffix='_2').rename_axis(index='ix').reset_index()
    temp = temp.drop(columns=['id_2'])[temp.index % 2 == 1].set_index('ix')
    result = temp.pivot('id', 'type_2', 'type').rename_axis(
        index='cust', columns=None).reset_index()

It gives:

        cust First Product Second Product
    0  cust1         chair          table
    1  cust2         chair           desk

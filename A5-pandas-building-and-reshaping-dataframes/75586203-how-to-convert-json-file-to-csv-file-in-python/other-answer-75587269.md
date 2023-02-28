---
title: "How to convert json file to csv file in python"
site: stackoverflow
question_id: 75586203
answer_id: 75587269
url: https://stackoverflow.com/a/75587269
author: "AltKrypto"
author_url: https://stackoverflow.com/users/21301042
posted: 2023-02-28T02:08:50Z
last_edited: 2023-02-28T02:19:44Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8feee7046bf6a13c45ac8cb3ebd19ba835f996476ed437ca60ac57b742eb37ad
role: another answer on the same question, kept as context; not my work
---

# Answer by [AltKrypto](https://stackoverflow.com/users/21301042) — 2023-02-28

Posted on Stack Overflow, <https://stackoverflow.com/a/75587269>, 2023-02-28, last edited 2023-02-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I ran into a similar issue with a recent project. I used the built in csv module

    def generate_csv(records):
    field_names = [&#39;Ticker&#39;, &#39;Quantity&#39;, &#39;Cost Per Share&#39;,         &quot;Date&quot;]
    with open(&#39;positions.csv&#39;, &#39;w&#39;) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(records)

this assumes you already have your data in the format you need, in my case, a list of dictionaries that I pass into the function. It reads through one dictionary at a time placing each record in its corresponding column based on the key names that are defined in field_names. 

Im brand new to this so I&#39;ve probably done this in a terribly inefficient way but it worked for me.

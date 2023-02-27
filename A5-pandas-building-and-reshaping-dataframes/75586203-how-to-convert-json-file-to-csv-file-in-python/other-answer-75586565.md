---
title: "How to convert json file to csv file in python"
site: stackoverflow
question_id: 75586203
answer_id: 75586565
url: https://stackoverflow.com/a/75586565
author: "Rockkley"
author_url: https://stackoverflow.com/users/18461470
posted: 2023-02-27T23:36:36Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c69b8c5a9cc312583349a7f9c148582a6c4d4a6bcc1f92fbb4eff7d1f404a348
role: another answer on the same question, kept as context; not my work
---

# Answer by [Rockkley](https://stackoverflow.com/users/18461470) — 2023-02-27

Posted on Stack Overflow, <https://stackoverflow.com/a/75586565>, 2023-02-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Python has a module called "csv" that has methods for reading and writing CSV files. You can use the csv.DictReader() method to read a JSON file into a CSV file. The method takes in a JSON object, converts it into a csv file, and returns a reader object that can be used to iterate over the rows of the resulting csv file.

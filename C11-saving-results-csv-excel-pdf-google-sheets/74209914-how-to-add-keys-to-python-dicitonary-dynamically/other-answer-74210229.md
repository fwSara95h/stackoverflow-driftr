---
title: "How to Add keys to python dicitonary dynamically?"
site: stackoverflow
question_id: 74209914
answer_id: 74210229
url: https://stackoverflow.com/a/74210229
author: "mlokos"
author_url: https://stackoverflow.com/users/19570235
posted: 2022-10-26T15:19:49Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 960efbbc9d752cb45095ed5c48c3ce1e15b70f06e6234e4b65616878ba1d4889
role: another answer on the same question, kept as context; not my work
---

# Answer by [mlokos](https://stackoverflow.com/users/19570235) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74210229>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You were creating csv header based only upon the first result, which didn't contained whole set of unique keys.

Change to_csv function to this to resolve your problem:

    def to_csv(self):
        key_list = list()
        for key_list_for_one_element in [list(x.keys()) for x in self.results]:
              key_list.extend(key_list_for_one_element)
        key_list = set(key_list)
        with open('ziwi_pets_2.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=key_list)
            writer.writeheader()

            for row in self.results:
                writer.writerow(row)

            print('Stored results to "ziwi_pets_2.csv"')

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-10-26): It worked but not as I expected. For example: as you can see in the csv https://docs.google.com/spreadsheets/d/1c_LmEmORhS-E66zBuKFmi72txIU-Zb32dIQhGF5zKH4/edit?usp=sharing generated from your code snippet it is including all the entries but title and other fields are duplicating and I'd like to have only one title row per entry. Something like this https://docs.google.com/spreadsheets/d/1tuDgx53XA7s4I0ByBnFELVCaS-EKRvPLNUB4G2Vz1JU/edit?usp=sharing it is a different dataset but only to reference.
- **[mlokos](https://stackoverflow.com/users/19570235)** (2022-10-26): In parser function you can change this line: **f'lowest_price_{idx}':  detail_1[idx],** into this: **f'lowest_price':  detail_1[idx],**  That way you will not have multiple 'lowest_price' columns with a different postfix
- **[X-somtheing](https://stackoverflow.com/users/18183763)** (2022-10-26): Which line you are referring to?

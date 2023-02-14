---
title: "Remove redundant tuples from dictionary based on the score"
site: stackoverflow
question_id: 75448227
url: https://stackoverflow.com/q/75448227
asked: 2023-02-14T13:01:53Z
asked_by: "Erwin"
asked_by_url: https://stackoverflow.com/users/14471688
last_edited: never
tags: [python, dictionary, tuples, redundancy]
score: 0
views_at_snapshot: 61
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f512191a7cbff3fc8eb939570453da9fa11b764e937cdd67373170eeb1269601
---

# Remove redundant tuples from dictionary based on the score

Asked by [Erwin](https://stackoverflow.com/users/14471688) on Stack Overflow, <https://stackoverflow.com/q/75448227>, 2023-02-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I wonder if there is a fast way to remove redundant tuples from dictionary. Suppose I have a dictionary as below:

```
a = {
    'trans': [('pickup', 1.0), ('boat', 1.0), ('plane', 1.0), ('walking', 1.0), ('foot', 1.0), ('train', 0.7455259731472191), ('trailer', 0.7227749512667475), ('car', 0.7759192750865143)],

    'actor': {
    'autori': [('smug', 1.0), ('pol', 1.0), ('traff', 1.0), ('local authori', 0.6894454471465952), ('driv', 0.6121365092485745), ('car', 0.6297345748705596)],

    'fam': [('fa', 1.0), ('mo', 1.0), ('bro', 1.0), ('son', 0.9925431812951816), ('sis', 0.9789254869156859), ('fami', 0.8392597243422916)],

    'fri': [('fri', 1.0), ('compats', 1.0), ('mo', 0.814126196299157), ('neighbor', 0.7433986938516075), ('parent', 0.32202418215134565), ('bro', 0.8496284151715676),  ('fami', 0.6375584385858655), ('best fri', 0.807654599975373)]
            }
    }
```
In this dictionary for example we have tuples like: ('car', 0.7759192750865143) for key 'trans' and ('car', 0.6297345748705596) for key 'autori'. I want to remove the tuple ('car', 0.6297345748705596) because it has a lower score.

My desired output is:

```
new_a = {
    'trans': [('pickup', 1.0), ('boat', 1.0), ('plane', 1.0), ('walking', 1.0), ('foot', 1.0), ('train', 0.7455259731472191), ('trailer', 0.7227749512667475), ('car', 0.7759192750865143)],

    'actor': {
    'autori': [('smug', 1.0), ('pol', 1.0), ('traff', 1.0), ('local authori', 0.6894454471465952), ('driv', 0.6121365092485745)],

    'fam': [('fa', 1.0), ('mo', 1.0), ('bro', 1.0), ('son', 0.9925431812951816), ('sis', 0.9789254869156859), ('fami', 0.8392597243422916)],

    'fri': [('fri', 1.0), ('compats', 1.0), ('neighbor', 0.7433986938516075), ('parent', 0.32202418215134565), ('best fri', 0.807654599975373)]
            }
    }
```

Is there a fast way to do this or we still need to loop through all values for each key?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[cards](https://stackoverflow.com/users/16462878)** (2023-02-14): Flat the iterator and reorganize it to remove the lowest multivalued term then update the original data
- **[Erwin](https://stackoverflow.com/users/14471688)** (2023-02-14): @cards can you propose a solution?

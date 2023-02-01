---
title: "Search for item in list of dictionary"
site: stackoverflow
question_id: 75309015
url: https://stackoverflow.com/q/75309015
asked: 2023-02-01T10:44:28Z
asked_by: "Ran Pol"
asked_by_url: https://stackoverflow.com/users/18339800
last_edited: 2023-02-01T10:54:40Z
last_editor: "Kelly Bundy"
last_editor_url: https://stackoverflow.com/users/12671057
tags: [python, dictionary, search]
score: 0
views_at_snapshot: 100
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d199a6f42453e69dc56901ebe150e22e0912cc1c1336f747e6c6b44e2ec95c8f
---

# Search for item in list of dictionary

Asked by [Ran Pol](https://stackoverflow.com/users/18339800) on Stack Overflow, <https://stackoverflow.com/q/75309015>, 2023-02-01, last edited 2023-02-01 by [Kelly Bundy](https://stackoverflow.com/users/12671057). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

So I have this `params`:

    p = [{'quantity': 1}, {'args': {'id': 12345678, 'age': 12}}]

And I want to be able to search for `quantity` and get the value `1` or the `args` key and get its `doctionary` (`{'id': 12345678, 'age: 12}`)

This is what I have try:

    def search(name: str, params: list[dict]):
        try:
            return next((x[name] for x in params if x), None)
        except KeyError:
            return None

I case I search for the value of `quantity`:

    search(name='quantity', params=p)


This return `1`

But in case I want to value of `args`:

    search(name='args', params=p)

This return `None`

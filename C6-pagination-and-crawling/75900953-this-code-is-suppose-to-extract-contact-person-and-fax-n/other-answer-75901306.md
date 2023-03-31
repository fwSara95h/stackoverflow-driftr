---
title: "This code is suppose to extract contact person and fax number looks okay but does not work"
site: stackoverflow
question_id: 75900953
answer_id: 75901306
url: https://stackoverflow.com/a/75901306
author: "Doc Kaos"
author_url: https://stackoverflow.com/users/740635
posted: 2023-03-31T17:40:35Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a2ae77d7758e608a206214d2145290e5a6c5a3c50fab14f34b32db414315c51f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Doc Kaos](https://stackoverflow.com/users/740635) — 2023-03-31

Posted on Stack Overflow, <https://stackoverflow.com/a/75901306>, 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This section seems to be the problem to me. Once the contact_div is set, there isn't another div of the same class inside ... in fact, looking at the site, this isn't how it's set up anymore. Did it change since you started this?

    contact_div = link_soup.find("div", {"class": "info-gen-box clearfix"})
    if contact_div:
        contact_person = contact_div.find("div", {"class": "info-gen-box clearfix"})
        if contact_person:
            contact_person = contact_person.text.strip()
        fax_number = contact_div.find("div", {"class": "info-fax info-mar"})
        if fax_number:
            fax_number = fax_number.text.strip()
I see only one `<div class="info-gen-box clearfix">` and it closes before the `info-fax info-mar` div that you are trying to access inside it.

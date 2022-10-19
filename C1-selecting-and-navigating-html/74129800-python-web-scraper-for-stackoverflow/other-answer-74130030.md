---
title: "Python Web scraper for Stackoverflow"
site: stackoverflow
question_id: 74129800
answer_id: 74130030
url: https://stackoverflow.com/a/74130030
author: "Rahul K P"
author_url: https://stackoverflow.com/users/4407666
posted: 2022-10-19T18:07:51Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0a8287d728b9e19ab9e006d25a91a6dd16c1bf7aa53b9a960f6e9316af429387
role: another answer on the same question, kept as context; not my work
---

# Answer by [Rahul K P](https://stackoverflow.com/users/4407666) — 2022-10-19

Posted on Stack Overflow, <https://stackoverflow.com/a/74130030>, 2022-10-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can find each question block using `data-post-type-id` attributes

    questions = soup.find_all('div',attrs={'data-post-type-id': 1})
    for question in questions:
        print(question.find('a', attrs={'class': 's-link'}).get('href')

Results will be:

    questions/74129840/how-to-keep-audio-driver-busy-with-no-sound-output-using-powershell-or-command-p
    /questions/74129837/vuejs-how-to-set-value-of-fecolormatrix
    /questions/74129835/please-show-me-example-of-software-architecture
    /questions/74129833/problem-getting-global-styles-includes-in-storybook-with-nx-and-angular-12
    /questions/74129831/not-able-to-figure-out-common-expression-language-conditional-statement
    /questions/74129830/why-can-i-successfully-assign-a-ref-to-a-string
    ....

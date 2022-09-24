---
title: "How to trigger the google chrome website translation popup?"
site: stackoverflow
question_id: 73828471
answer_id: 73834660
url: https://stackoverflow.com/a/73834660
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-24T04:07:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73834660/revisions
accepted: false
score: 2
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b460ef2d8a2e43184da6e5495e6c25a95c0de3d109441ba3c4ef46d2a9af21fe
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73834660>, 2022-09-24; score 2. Text as retrieved 2026-10-12.

Perhaps because of the `lang="de"` meta, it's not bothering to look for other languages (and it looks like your settings are to offer to translate *non*-German languages to German), but I think that is unlikely since [according to Google documentation][1], they don't use the `lang` attribute, and using a single language is the best way to help detect page language.

You could use the [Google Translate API][2] and add extra buttons or something to offer the translation, if you're willing to either do some extra work figuring how to detect user's language preferences (maybe using something like [`Navigator.language`][3]) or always showing [Google Translate button/drop-down][4] near that section regardless of user preferences. 


  [1]: https://support.google.com/webmasters/answer/182192?hl=en#1
  [2]: https://www.folkstalk.com/2022/09/google-translate-translateelement-part-of-page-with-code-examples.html
  [3]: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language
  [4]: https://www.w3schools.com/howto/howto_google_translate.asp

---
title: "how to change boolean value thats another file"
site: stackoverflow
question_id: 74334979
answer_id: 74335067
url: https://stackoverflow.com/a/74335067
author: "Kutay Kılıç"
author_url: https://stackoverflow.com/users/19274851
posted: 2022-11-06T10:38:10Z
last_edited: never
accepted: false
score: -1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b778b13823f3c88e6fd58d04866f015c34b4b825f13fb860f43eefc29313dc46
role: another answer on the same question, kept as context; not my work
---

# Answer by [Kutay Kılıç](https://stackoverflow.com/users/19274851) — 2022-11-06

Posted on Stack Overflow, <https://stackoverflow.com/a/74335067>, 2022-11-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You are changing the value inside the runtime, meaning you can actually change it. Meaning if you are ever trying to print out the value inside the if condition like this:

       booleans.storepass = True
       print(booleans.storepass)#This should return True

But your problem is that you are not actually changing the file. In order to change the file you should do it like this( This is the general way to write to a file with python from my research it should work in your case as well. 

   

    f = open("booleans.py", "w")
    f.write("booleans.storepass = True")
    f.close()

In short what you are doing is actually true for runtime, but if you want to store the result in a file this is the way to do it.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Marcus Müller](https://stackoverflow.com/users/4433386)** (2022-11-06): Note that your `open` will completely remove all contents from the current `booleans.py`. Which is probably not what katie had in mind.
- **[Kutay Kılıç](https://stackoverflow.com/users/19274851)** (2022-11-06): It seemed like the OP just meant to do that so yeah you are right! And from the other answers storing as json seemed better!

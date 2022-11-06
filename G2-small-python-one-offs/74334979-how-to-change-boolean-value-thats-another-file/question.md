---
title: "how to change boolean value thats another file"
site: stackoverflow
question_id: 74334979
url: https://stackoverflow.com/q/74334979
asked: 2022-11-06T10:26:47Z
asked_by: "user20226026"
asked_by_url: (account no longer exists)
last_edited: never
tags: [python]
score: 0
views_at_snapshot: 555
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dd1bcc261b97f8491ea2b9b76c956e9ea08c336784d468830955ba56fea8bc21
---

# how to change boolean value thats another file

Asked by user20226026 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/74334979>, 2022-11-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Im trying to make a thing that can detect whether or not a user wants their password stored for next time they run the program, The reason im using a boolean for this is so in the files that need to use the password they can check to see if storepass is True then get the pass/user from a .env if not they can get the password from the storepasswordquestion file amd use that and it wont get stored when the user closes the program.

I have a file called booleans that im using to store booleans, in it is this:
```
storepass = False
```
In a other file called storepasswordquestion i have:
```
import booleans

username = 'username'
password = 'password'

question = input('Would you like your password to be stored for use next time?') # enter y
if question == 'y':
    booleans.storepass = True
    # store password/username in .env
```
As i understand it import booleans loads the booleans file, Then i think booleans.storepass is like a variable but like a copy of the one in booleans? Because when i go on the booleans file again its still False.

Im needing to change storepass to True in the booleans file and then save it.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Marcus Müller](https://stackoverflow.com/users/4433386)** (2022-11-06): *Im needing to change storepass to True in the booleans file and then save it.* Exactly. Where are you stuck there?
- **user20226026 (account no longer exists)** (2022-11-06): When i run the program and enter y, then i look at the booleans file it is still False not True. Im wondering why is it not showing up in the booleans file
- **[Nikolaj Š.](https://stackoverflow.com/users/9288580)** (2022-11-06): Source code isn't supposed to be modified by the program.  What you need here is basically a configuration file, so switch to something like [configparser](https://docs.python.org/3/library/configparser.html)

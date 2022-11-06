---
title: "how to change boolean value thats another file"
site: stackoverflow
question_id: 74334979
answer_id: 74335545
url: https://stackoverflow.com/a/74335545
author: "Marcus Müller"
author_url: https://stackoverflow.com/users/4433386
posted: 2022-11-06T11:41:55Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 12ebd8cd08e0f62aecd979ece60ca87bbf220edf825fb12d99cddee064962922
role: another answer on the same question, kept as context; not my work
---

# Answer by [Marcus Müller](https://stackoverflow.com/users/4433386) — 2022-11-06

Posted on Stack Overflow, <https://stackoverflow.com/a/74335545>, 2022-11-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You're expecting changing a variable's value to change source code. Luckily, that's not how this works!

You need to make a mental distinction between the source code that the python interpreter reads, and the values of variables.

What you need is indeed, as you say,

> Im needing to change storepass to True in the booleans file and then save it.

So, you would need to open that boooleans.py as a text file, not as a python program, read and interpret it as pairs of keys and values, modify the right one (so, `storepass` in this case), write the result back to the file. Then, the next time someone `import`s it, they would see the different setting.

This is a bad approach you've chosen:

1. Reading and parsing python files is very hard in general, because, well, Python is a programming language and can do much more than just store settings
2. The change only takes effect the next time the program is run and the settings are imported *anew*. This has no effect on other parts of an already running program. So, that's bad.

Things get a lot easier if you do two things:

1. Get rid of the idea to store settings in a Python source code file. Instead, use one of the multiple ways that python has to read structured data from a file. For your use case, usage of the `configparser` [module](https://docs.python.org/3/library/configparser.html) might be easiest – a `ConfigParser` has a `read` and a `write` method, with which you can, you guessed it, read and write your config file. <br>There's multiple other modules that Python brings that can do similar things. The `json` module, for example, is a sensible way to store especially logically hierarchically structured settings. And of course, the place where you store passwords **might** also be a place where you could store settings – depending on what that is.
2. The approach of having a single module that you import (your `booleans`) is a good one, as it ensures that there's a single `booleans` that is the "source of truth" about these settings. I propose you put the configuration loading into such a single module:

```python
# this is settings.py
import json

SETTINGSFILE = "settings.json"

# when this is loaded the first time, load things from the settings file
try:
    with open(SETTINGSFILE) as sfile:
        _settings = json.load(sfile)
except FileNotFoundError:
    # no settings file yet. We'll just have empty settings
    # Saving these will create a file
    _settings = {}


def __getattr__(settingname):
    try:
        return _settings[settingname]
    except KeyError as e:
        # you could implement "default settings" by checking
        # in a default settings dictionary that you create above
        # but here, we simply say: nay, that setting doesn't yet
        # exist. Which is as good as your code would have done!
        raise AttributeError(*e.args) from e


def save():
    with open(SETTINGSFILE, "w") as sfile:
        json.dump(_settings, sfile)


def update_setting(settingname, value):
    _settings[settingname] = value
    save()


```

which you can then use like this:

```python
import settings

…

if settings.storepass:
    "Do what you want here"

…

# User said they want to change the setting:

should_we_store = (input("should we store the password? ").upper == "Y")
# this updates the setting, i.e. it's instantly visible
# in other parts of the program, and also stores the changed config
# to the settings.json file
settings.update_setting("storepass", should_we_store)
```

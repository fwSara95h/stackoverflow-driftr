---
title: "How to remove or ignore an entry in a JSON file using python?"
site: stackoverflow
question_id: 75598088
answer_id: 75598450
url: https://stackoverflow.com/a/75598450
author: "Eric Grunzke"
author_url: https://stackoverflow.com/users/596242
posted: 2023-03-01T00:04:51Z
last_edited: 2023-03-01T00:20:51Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e7399dc11a73beb8198efc0462d4fd06e8c571a1f8b00f524e583ebeadfed312
role: another answer on the same question, kept as context; not my work
---

# Answer by [Eric Grunzke](https://stackoverflow.com/users/596242) — 2023-03-01

Posted on Stack Overflow, <https://stackoverflow.com/a/75598450>, 2023-03-01, last edited 2023-03-01; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You have two choices: [Look Before You Leap or Easier to Ask Forgiveness than Permission][1].  In short:
* **LBYL**: Do an `if` check to make sure `ipv4Prefix` exists
* **EAFP**: Assume that `ipv4Prefix` exists but catch the exception (a `KeyError` in this case)

Here is some code that demonstrates both approaches. It does not include writing out the results.

    import json
    
    
    def lbyl(data: dict):
        """Look before you leap"""
        ipv4s = []
    
        for prefix in data["prefixes"]:
            # Ensure that "ipv4Prefix" exists
            if "ipv4Prefix" in prefix:
                ipv4s.append(prefix["ipv4Prefix"])
        return ipv4s
    
    
    def eafp(data: dict):
        """Easier to Ask Forgiveness than Permission"""
        ipv4s = []
    
        for prefix in data["prefixes"]:
            try:
                ipv4s.append(prefix["ipv4Prefix"])
            except KeyError:
                # This happens when "ipv4Prefix" is not in prefix
                pass
    
        return ipv4s
    
    
    def get_data(path) -> dict:
        with open(path) as f:
            return json.load(f)
    
    
    if __name__ == "__main__":
        data = get_data("cloud.json")
        print(lbyl(data))
        print(eafp(data))

Which style to use is subjective. Python has a reputation for preferring EAFP, but I prefer to use LYBL if errors are expected as part of normal operation. In your case you know that some objects will _not_ have `ipv4Prefix`, so I contend that LBYL is more suitable here.

  [1]: https://realpython.com/python-lbyl-vs-eafp/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Hosein Nikkhah](https://stackoverflow.com/users/21258013)** (2023-03-01): Both approaches are amazing didn't know LBYL is that handy
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-03-01): IMHO you should use LBYL when the difference is expected, while EAFP is for unexpected missing data. Python also has `dict.get()`, which can be a simple form of LBYL.

---
title: "Find and Update Dictionary Value Using Key List"
site: stackoverflow
question_id: 75903026
url: https://stackoverflow.com/q/75903026
asked: 2023-03-31T21:55:55Z
asked_by: "Scott"
asked_by_url: https://stackoverflow.com/users/7496567
last_edited: 2023-03-31T23:15:21Z
last_editor: "wjandrea"
last_editor_url: https://stackoverflow.com/users/4518341
tags: [python, dictionary, mqtt]
score: 0
views_at_snapshot: 102
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 07351df3e5648395626be5d97a225ad6cf496d5ef78218f2f2ef58742baaf7b3
---

# Find and Update Dictionary Value Using Key List

Asked by [Scott](https://stackoverflow.com/users/7496567) on Stack Overflow, <https://stackoverflow.com/q/75903026>, 2023-03-31, last edited 2023-03-31 by [wjandrea](https://stackoverflow.com/users/4518341). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

This might be difficult to explain (which is part of the reason I haven't figured out how to google it properly) but I'll do my best.

I'm using MQTT and I subscribe to a topic (say "generic_topic/#")

If any publish is made to this, I update a dictionary in memory (and in a file).

So, if I get an update at "general_topic/born/to/fly" with a value of 100.  I want to check if the dictionary (say gen_dict) has that value stored at that location and if not, update it.
```
topics = message.topic.split('/') # topic = ['general_topic', 'born', 'to', 'fly']
try:
    if (gen_dict[topics[1]][topics[2]][topics[3]] != 100):
        gen_dict[topics[1]][topics[2]][topics[3]] = 100
except:
    gen_dict[topics[1]][topics[2]][topics[3]] = 100
```
Problem is that there could be any number of elements in the topics list so I'm not sure how to do this recursively (or if I even need to do it recursively).
Also, if there was no 'born' key in the dictionary, is there a clean way to go through the topic_list to accomplish what is being done in the "except" section of the code (because obviously that will fail since those keys do not exist)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Mark](https://stackoverflow.com/users/3874623)** (2023-03-31): So as you are going through the topics, if any are not in the dict, you want to add them at that level of nesting. Then the last one you want to set to some number?
- **[Scott](https://stackoverflow.com/users/7496567)** (2023-03-31): Conceptually, I am right there with you and that is why I thought it was going to be straight forward.  But when I started putting it to code, I didn't know how to do it.  It's really easy if I know the "topics" list will always be a particular length.
- **[Mark](https://stackoverflow.com/users/3874623)** (2023-03-31): I'm not sure that answered my question. So you have a `gen_dict = {}` then you get `['general_topic', 'born', 'to', 'fly']` you then want `gen_dict` to be turned into something like `{'general_topic': {'born': {'to': {'fly': 100}}}}`?
- **[Scott](https://stackoverflow.com/users/7496567)** (2023-03-31): My mistake, I somehow missed the question.  gen_dict is a dictionary and it could have a bunch of other data in it before I get an update from the broker (it very likely will).  You are correct in what you assumed but it would add it to gen_dict if it doesn't already exist in the dictionary or update the value if it is there but has a different value.  For example the dictionary could be the following before getting the update from the broker.   { 'other':      'blah', 'general_topic': {     'born': {         'to': {             'fly': 30}}}, 'another': 324}
- **[Scott](https://stackoverflow.com/users/7496567)** (2023-03-31): The dictionary could also be this:  gen_dict = {'some': {'thing': 23, 'one': 393}}  Technically, I'm actually not using the 'general_topic' as part of the dictionary so if it was ONLY that topic that came in and I updated an empty gen_dict ... it would be:  gen_dict = {'born': {'to': {'fly': 100}}}
- **[wjandrea](https://stackoverflow.com/users/4518341)** (2023-03-31): Beside the point, but [a bare `except` is bad practice](/q/54948548/4518341). Instead, use the specific exception you're expecting like `except KeyError`, or at least `except Exception`.
- **[Scott](https://stackoverflow.com/users/7496567)** (2023-03-31): @wjandrea ... yes, I know ... this isn't my actual code, it was just a quick example.  There are several things here I wouldn't do but they didn't relate to the question so I wasn't worried about it.
- **[wjandrea](https://stackoverflow.com/users/4518341)** (2023-03-31): Related: [Update value of a nested dictionary of varying depth](/q/3232943/4518341). If you search for "nested dict", you'll probably find some other useful stuff.

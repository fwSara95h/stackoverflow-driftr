---
title: "Group JSON in order for it to be more readable"
site: stackoverflow
question_id: 75208675
url: https://stackoverflow.com/q/75208675
asked: 2023-01-23T11:11:32Z
asked_by: "Idkwhatywantmed"
asked_by_url: https://stackoverflow.com/users/18542427
last_edited: 2023-01-23T14:05:24Z
tags: [python, python-3.x, dictionary, nlp, huggingface-transformers]
score: 0
views_at_snapshot: 53
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5dd394696554b4257b3c9eafe2f6c29970bdaf2762a041644432d98b3c8d3ad4
---

# Group JSON in order for it to be more readable

Asked by [Idkwhatywantmed](https://stackoverflow.com/users/18542427) on Stack Overflow, <https://stackoverflow.com/q/75208675>, 2023-01-23, last edited 2023-01-23. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have this file (`MYFILE.txt`) that is the output of a list of lists with dictionaries inside:

    [{'entity_group': 'literal', 'score': 0.99999213, 'word': 'DNA', 'start': 0, 'end': 3}, {'entity_group': 'metaphoric', 'score': 0.9768174, 'word': 'loop', 'start': 4, 'end': 8}, {'entity_group': 'literal', 'score': 0.9039155, 'word': 'ing,', 'start': 8, 'end': 12}, {'entity_group': 'metaphoric', 'score': 0.99962616, 'word': 'in', 'start': 13, 'end': 15}, {'entity_group': 'literal', 'score': 0.9949911, 'word': 'which a protein or protein complex interacts simultaneously', 'start': 16, 'end': 75}, {'entity_group': 'metaphoric', 'score': 0.59057885, 'word': 'with', 'start': 76, 'end': 80}, {'entity_group': 'literal', 'score': 0.9983214, 'word': 'two separated sites on a DNA molecule, is a recurring theme', 'start': 81, 'end': 140}, {'entity_group': 'metaphoric', 'score': 0.9998679, 'word': 'in', 'start': 141, 'end': 143}, {'entity_group': 'literal', 'score': 0.9997542, 'word': 'transcription', 'start': 144, 'end': 157}, {'entity_group': 'metaphoric', 'score': 0.7964442, 'word': 'regula', 'start': 158, 'end': 164}, {'entity_group': 'literal', 'score': 0.99982435, 'word': 'tion [', 'start': 164, 'end': 170}]

I want to group the "literal" in order to get the text only, and leave the metaphoric as it is. I tried with this code below but it says `string indices must be integers`, and I also think that I could make it HTML and color it to visualize better the result, but I'm sure there's a quicker solution.

    with open(r'MYFILE.txt', 'r') as res:
      texty = res.read()
      for group in texty[::-1]:
          ent = group["entity_group"]
          if ent != 'literal': 
          text2 = replace_at(ent, group['end'], group['end'], text)
    print(text2)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[atinjanki](https://stackoverflow.com/users/11631110)** (2023-01-23): What are the contents of 'MYFILE.txt'?
- **[Guy](https://stackoverflow.com/users/5168011)** (2023-01-23): What do you expect to get in the end?
- **[Idkwhatywantmed](https://stackoverflow.com/users/18542427)** (2023-01-23): The content is what I put before, the json
- **[Idkwhatywantmed](https://stackoverflow.com/users/18542427)** (2023-01-23): I expect to get sth like "hello how are you {entoty group metaphoric etc.} I'm fine", so the literal ones are text and the rest stays the same
- **me** (2023-01-24): @Idkwhatywantmed there is no JSON in your q. the first snippet is a python dictionary, but JSON standards require double quotes https://stackoverflow.com/questions/36038454/parsing-string-as-json-with-single-quotes ...also, `.read()` (generally) returns a string and if it *was* json, you'd need [`json.loads`](https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/) to parse it into a python object

---
title: "Delete nodes in singly linked list javascript"
site: stackoverflow
question_id: 74201752
url: https://stackoverflow.com/q/74201752
asked: 2022-10-26T01:27:33Z
asked_by: "Aquiles Bailo"
asked_by_url: https://stackoverflow.com/users/19222504
last_edited: 2022-10-26T01:37:43Z
last_editor: "morganney"
last_editor_url: https://stackoverflow.com/users/258174
tags: [javascript, algorithm, singly-linked-list]
score: 2
views_at_snapshot: 658
answer_count: 4
accepted_answer_id: 74202062
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 52c17b983666a4a93b7e41446cebc691ef61688c0130d9a3015e34fcf97085b2
---

# Delete nodes in singly linked list javascript

Asked by [Aquiles Bailo](https://stackoverflow.com/users/19222504) on Stack Overflow, <https://stackoverflow.com/q/74201752>, 2022-10-26, last edited 2022-10-26 by [morganney](https://stackoverflow.com/users/258174). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of x numbers that I need to evaluate which are higher than 50 and delete those from the list and then print out the new list. I can't figure out how to add the condition  >50 because it renders a blank array.  Also, is there a more time efficient way to write this? Appreciate all the help. I'm very confused.

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    class Node {
      constructor(d) {
          this.data = d;
          this.next = null;
      }
    }

    class LinkedList {
      constructor(head = null) {
        this.head = head
      }
    }

    let firstNode = new Node(38);
    let list = new LinkedList(firstNode);

    let secondNode = new Node(74);
    firstNode.next = secondNode;

    let thirdNode = new Node(87);
    secondNode.next = thirdNode;

    let fourthNode = new Node(21);
    thirdNode.next = fourthNode;

    let fithNode = new Node(91);
    fourthNode.next = fithNode;

    let sixthNode = new Node(98);
    fithNode.next = sixthNode;

    let seventhNode = new Node(73);
    sixthNode.next = seventhNode;

    let eigthNode = new Node(41);
    seventhNode.next = eigthNode;

    let nithNode = new Node(29);
    eigthNode.next = nithNode;

    let tenthNode = new Node(3);
    nithNode.next = tenthNode

    let eleventhNode = new Node(72);
    tenthNode.next = eleventhNode;

    let twelthNode = new Node(94);
    eleventhNode.next = twelthNode;

    let thirteenthNode = new Node(12);
    twelthNode.next = thirteenthNode;

    let fourteenthNode = new Node(13);
    thirteenthNode.next = fourteenthNode;

    let fiftheenthNode = new Node(16);
    fourteenthNode.next = fiftheenthNode;

    let currentNode = list.head;

    while (currentNode != null && currentNode > 50) {
      console.log(currentNode.data);
      currentNode = currentNode.next;
    }

<!-- end snippet -->

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Hunter McMillen](https://stackoverflow.com/users/702638)** (2022-10-26): I don't see a condition at all. What have you tried in your while loop that didn't work? In what way did it not work?
- **[Aquiles Bailo](https://stackoverflow.com/users/19222504)** (2022-10-26): @HunterMcMillen I added the code I had tried before. It does not display anything at all.
- **[Hunter McMillen](https://stackoverflow.com/users/702638)** (2022-10-26): You are stopping your loop when you encounter any element <= 50. Your first node is 38 which is <= 50 so your while loop does not execute.

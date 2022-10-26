---
title: "Delete nodes in singly linked list javascript"
site: stackoverflow
question_id: 74201752
answer_id: 74201974
url: https://stackoverflow.com/a/74201974
author: "Chintan Trivedi"
author_url: https://stackoverflow.com/users/17791486
posted: 2022-10-26T02:11:11Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c750f60f2ce2fe63d672142086d9004eee271caacaa4102414de5569107b0e05
role: another answer on the same question, kept as context; not my work
---

# Answer by [Chintan Trivedi](https://stackoverflow.com/users/17791486) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74201974>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This can be done with looping on the created Linkedlist and if the value is less than equal 50 than put it into new linkedlist and map it. The last console is to print out the actual linkedlist, because intially we created dummyHead with Infinity value so our result starts from the next of resultHead.



<!-- begin snippet: js hide: false console: true babel: null -->

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
    let resultNode = new Node(-Infinity);
    let resultHead = resultNode;
    while (currentNode != null) {
      //console.log(currentNode.data);
      if(currentNode.data <= 50){
        resultNode.next = new Node(currentNode.data);
        resultNode = resultNode.next;
      }
      currentNode = currentNode.next;     
    }
    console.log(resultHead.next);

<!-- end snippet -->

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Aquiles Bailo](https://stackoverflow.com/users/19222504)** (2022-10-26): thank you so much!! I got the results I was looking for, in the console it displays   next: Node { data: 38, next: Node { data: 21, next: [Node] } }... how can I access the contents of the node? I need to display the list as 38, 21, 41, 29 etc... Thank you once again!!!
- **[Chintan Trivedi](https://stackoverflow.com/users/17791486)** (2022-10-26): If your problem says return head then this will work and if problem says returning array then you need to create resultArr and have to use push method if condition meets. You can remove resultNode, resultHead. At the end, you can direcy print it or loop through and do console.

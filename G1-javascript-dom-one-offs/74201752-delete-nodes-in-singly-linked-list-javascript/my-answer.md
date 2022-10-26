---
title: "Delete nodes in singly linked list javascript"
site: stackoverflow
question_id: 74201752
answer_id: 74202062
url: https://stackoverflow.com/a/74202062
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T02:26:45Z
last_edited: 2022-10-26T03:26:24Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74202062/revisions
accepted: true
score: 2
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ed835ace7d205c75338d15f6c3e1f47a3acc6d98ca7eee408c9344caf0ef5453
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74202062>, 2022-10-26, last edited 2022-10-26; **accepted**; score 2. Text as retrieved 2026-10-12.

You need to make exceptions for the head, and the loop you're using should actually be used *for deleting* inside another loop that goes through *all* the nodes (so the outer loop cannot filter by `currentNode.data > 50`).

I've edited your code so that it should behave more as you were asking for:

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

            //for printing
            printable(sll) {
                if (this.head == null) {
                    return 'Empty list';
                }
                let sll_str = `${this.head.data}`;
                let cNode = this.head.next;
                while (cNode != null) {
                    sll_str += `, ${cNode.data}`;
                    cNode = cNode.next;
                }
                return sll_str;
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

        console.log("old list: ", list.printable());
        while (currentNode != null) {
            if (list.head == currentNode && currentNode.data > 50) {
                list.head = currentNode.next;
                console.log("deleting ", currentNode.data);
                let toDel = currentNode;
                delete (toDel);
            } else {
                console.log(currentNode.data);
                let newNext = currentNode.next;
                while (newNext != null && newNext.data > 50) {
                    let toDel = newNext;
                    newNext = newNext.next;
                    console.log("deleting ", toDel.data);
                    delete(toDel);
                }
                currentNode.next = newNext;
            }
            currentNode = currentNode.next;
        }
        console.log("\nnew list: ", list.printable());

<!-- end snippet -->

(I also added a function to the `LinkedList` class to make it easier to print.)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Aquiles Bailo](https://stackoverflow.com/users/19222504)** (2022-10-26): thank you so much!!! It works as intended now. I really appreciate your help!!!
- **me** (2022-10-26): @AquilesBailo actually, I'm really sorry, but I forgot a crucial part - linking the previous to the next acceptable node after skipping the deleted ones [I'm new to this too 😅]. I've edited to correct that, and also added a print function to the LinkedList class so you can clearly check what the lists look like before and after

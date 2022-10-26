---
title: "Delete nodes in singly linked list javascript"
site: stackoverflow
question_id: 74201752
answer_id: 74209665
url: https://stackoverflow.com/a/74209665
author: "Hunter McMillen"
author_url: https://stackoverflow.com/users/702638
posted: 2022-10-26T14:41:25Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9e1dd716938d0b8166f56c9ef8a122572de72c1acdf002d2aa2b861f0986f763
role: another answer on the same question, kept as context; not my work
---

# Answer by [Hunter McMillen](https://stackoverflow.com/users/702638) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74209665>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Another solution would be to keep track of the `previous` node. This allows to efficiently _skip_ nodes:



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
      
      static fromArray(numbers) {
        if (numbers.length === 0) { 
          return null; 
        }
      
        const [first, ...rest] = numbers;
        const head = new Node(first);

        let current = head;
        rest.forEach(n => {
          const newNode = new Node(n);
          current.next = newNode;
          current = newNode;
        });

        return new LinkedList(head); 
      }
      
      toString() {
        let current = this.head;
        let repr = "";
        while (current != null) {
          repr += current.data + ' -> '
          current = current.next;
        }
        
        repr += 'null';
        return repr;
      }
    }

    let list = LinkedList.fromArray(
      [38, 74, 87, 21, 91, 98, 73, 41, 29, 3, 72, 94, 12, 13, 16]
    );

    console.log("BEFORE: ", list.toString());

    let current = list.head;
    let previous = null;
    while (current != null) {  
      if (current.data <= 50) {
        // value is in the valid range, update pointers
        previous = current;
        current = current.next;
        
        // skip to next loop iteration
        continue;
      } 
      
      if (current === list.head) {
        // if we are at the head of the list there is no previous value
        // overwrite the head
        list.head = current.next;
      }
      else {
        // if we are past the head of the list there is a previous value
        // skip the current value by updating the previous node's 'next' to the
        // current node's next
        previous.next = current.next; 
      }
      
      // advance to the next element
      current = current.next;
    }

    console.log("AFTER: ", list.toString());

<!-- end snippet -->

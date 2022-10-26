---
title: "Delete nodes in singly linked list javascript"
site: stackoverflow
question_id: 74201752
answer_id: 74201931
url: https://stackoverflow.com/a/74201931
author: "Jagroop"
author_url: https://stackoverflow.com/users/18431570
posted: 2022-10-26T02:02:53Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 56747115db106b34de8f2119de8c618471dc26b0eb4c01413be563efe9ec8f06
role: another answer on the same question, kept as context; not my work
---

# Answer by [Jagroop](https://stackoverflow.com/users/18431570) — 2022-10-26

Posted on Stack Overflow, <https://stackoverflow.com/a/74201931>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I am happy that you choose Javascript for LinkedList like me.
I will provide you with the Solution, please refer to this :


<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->


    function deleteNode(position)
    {
         
        // If linked list is empty
        if (head == null)
            return;
         
        // Store head node
        var temp = head;
         
        // If head needs to be removed
        if (position == 0)
        {
             
            // Change head
            head = temp.next;
            return;
        }
         
        // Find previous node of the node to be deleted
        for(i = 0; temp != null && i < position - 1; i++)
            temp = temp.next;
         
        // If position is more than number of nodes
        if (temp == null || temp.next == null)
        return;
         
        // Node temp->next is the node to be deleted
        // Store pointer to the next of node to be deleted
        var next = temp.next.next;
         
        // Unlink the deleted node from the list
        temp.next = next;
    }

<!-- end snippet -->



Here you can pass position  = position of the linked list element you want to delete.

Just implement the below code firstly with paper and pen after that you will understand this.

For any confusion, please let me know by commenting here.

Happy Coding !!

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Aquiles Bailo](https://stackoverflow.com/users/19222504)** (2022-10-26): thanks for your detailed answer! I still get the same result, the condition of > 50 is not applied. I need to use the traverse and then delete the data. Any hints with that?

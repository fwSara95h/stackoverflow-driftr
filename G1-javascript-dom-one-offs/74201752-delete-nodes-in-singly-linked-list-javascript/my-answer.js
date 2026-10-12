// Code from my Stack Overflow answer https://stackoverflow.com/a/74202062 (posted 2022-10-26), extracted verbatim; may need the question's context to run.

// --- block 1 ---
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

// --- block 2 ---
let firstNode = new Node(38);
let list = new LinkedList(firstNode);

// --- block 3 ---
let secondNode = new Node(74);
firstNode.next = secondNode;

// --- block 4 ---
let thirdNode = new Node(87);
secondNode.next = thirdNode;

// --- block 5 ---
let fourthNode = new Node(21);
thirdNode.next = fourthNode;

// --- block 6 ---
let fithNode = new Node(91);
fourthNode.next = fithNode;

// --- block 7 ---
let sixthNode = new Node(98);
fithNode.next = sixthNode;

// --- block 8 ---
let seventhNode = new Node(73);
sixthNode.next = seventhNode;

// --- block 9 ---
let eigthNode = new Node(41);
seventhNode.next = eigthNode;

// --- block 10 ---
let nithNode = new Node(29);
eigthNode.next = nithNode;

// --- block 11 ---
let tenthNode = new Node(3);
nithNode.next = tenthNode

// --- block 12 ---
let eleventhNode = new Node(72);
tenthNode.next = eleventhNode;

// --- block 13 ---
let twelthNode = new Node(94);
eleventhNode.next = twelthNode;

// --- block 14 ---
let thirteenthNode = new Node(12);
twelthNode.next = thirteenthNode;

// --- block 15 ---
let fourteenthNode = new Node(13);
thirteenthNode.next = fourteenthNode;

// --- block 16 ---
let fiftheenthNode = new Node(16);
fourteenthNode.next = fiftheenthNode;

// --- block 17 ---
let currentNode = list.head;

// --- block 18 ---
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

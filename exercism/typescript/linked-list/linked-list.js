//REFACTOR: some boilerplate added for debugging. Think of simplifying some functions.
class Node {
    data;
    next = null;
    prev = null;
    constructor(data) {
        this.data = data;
    }
}
export class LinkedList {
    head = null;
    getLast(node) {
        return node.next ? this.getLast(node.next) : node;
    }
    ;
    push(element) {
        const node = new Node(element);
        if (!this.head) {
            this.head = node;
        }
        else {
            const lastNode = this.getLast(this.head);
            node.prev = lastNode;
            lastNode.next = node;
        }
        return node;
    }
    pop() {
        let nodeToReturn;
        if (this.head) {
            nodeToReturn = this.getLast(this.head);
            if (nodeToReturn.prev) {
                nodeToReturn.prev.next = null;
            }
        }
        else {
            throw new Error("List is empty");
        }
        if (this.head === nodeToReturn) {
            this.head = null;
        }
        return nodeToReturn.data;
    }
    shift() {
        let nodeToReturn;
        if (this.head) {
            nodeToReturn = this.head;
        }
        else {
            throw new Error("List is empty");
        }
        if (nodeToReturn.next) {
            nodeToReturn.next.prev = null;
            this.head = nodeToReturn.next;
        }
        if (this.head === nodeToReturn) {
            this.head = null;
        }
        return nodeToReturn.data;
    }
    unshift(element) {
        const node = new Node(element);
        if (!this.head) {
            this.head = node;
        }
        else {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        }
        return node;
    }
    delete(element) {
        let node;
        if (this.head) {
            node = this.head;
        }
        else {
            throw new Error("List is empty");
        }
        while (node) {
            if (node.data === element) {
                let prevNode = node.prev;
                let nextNode = node.next;
                if (prevNode) {
                    prevNode.next = nextNode;
                }
                if (nextNode) {
                    nextNode.prev = prevNode;
                }
                break;
            }
            node = node.next;
        }
        if (this.head === node) {
            this.head = null;
        }
        return node;
    }
    count() {
        let sum = 0;
        let node;
        if (this.head) {
            node = this.head;
        }
        else {
            return 0;
        }
        while (node) {
            node = node.next;
            sum += 1;
        }
        return sum;
    }
}

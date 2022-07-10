//REFACTOR: some boilerplate added for debugging. Think of simplifying some functions.
class Node<T> {
  public next: Node<T> | null = null;
  public prev: Node<T> | null = null;

  constructor(public data: T) {
  }
}


export class LinkedList<T> {
  private head: Node<T> | null = null;

  private getLast(node: Node<T>): Node<T> {
    return node.next ? this.getLast(node.next) : node;
  };

  public push(element: T): Node<T> {
    const node = new Node(element);
    if (!this.head) {
      this.head = node
    } else {
      const lastNode = this.getLast(this.head);
      node.prev = lastNode;
      lastNode.next = node;
    }

    return node;
  }

  public pop(): T {
    let nodeToReturn: Node<T>;
    if (this.head) {
      nodeToReturn = this.getLast(this.head);
      if (nodeToReturn.prev) {
        nodeToReturn.prev.next = null;
      }
    } else {
      throw new Error("List is empty");
    }
    if (this.head === nodeToReturn) {
      this.head = null;
    }

    return nodeToReturn.data;
  }

  public shift(): T {
    let nodeToReturn: Node<T>;
    if (this.head) {
      nodeToReturn = this.head;
    } else {
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

  public unshift(element: T): Node<T> {
    const node = new Node(element);

    if (!this.head) {
      this.head = node;
    } else {
      this.head.prev = node;
      node.next = this.head;
      this.head = node;
    }
    return node;
  }

  public delete(element: T): Node<T> | null {
    let node: Node<T> | null;
    if (this.head) {
      node = this.head;
    } else {
      throw new Error("List is empty");
    }
    while (node) {
      if (node.data === element) {
        let prevNode: Node<T> | null = node.prev;
        let nextNode: Node<T> | null = node.next;
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

  public count(): number {
    let sum: number = 0;
    let node: Node<T> | null;
    if (this.head) {
      node = this.head;
    } else {
      return 0;
    }
    while (node) {
      node = node.next;
      sum += 1;
    }
    return sum;
  }
}

"""Doubly linked list implementation used by the Exercism linked-list exercise."""

from __future__ import annotations

from collections.abc import Iterator


class Node:
    """Single linked-list node storing value and neighbor references."""

    # pylint: disable=too-few-public-methods
    def __init__(
        self,
        value: int,
        succeeding: Node | None = None,
        previous: Node | None = None,
    ) -> None:
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    """Doubly linked list with push/pop and shift/unshift operations."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator[int]:
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.succeeding

    def push(self, value: int) -> None:
        """Append a value to the tail of the list."""
        new_node = Node(value=value, succeeding=None, previous=self.tail)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> int:
        """Remove and return the value at the tail of the list."""
        if self.tail is None:
            raise IndexError("List is empty")

        removed_node = self.tail
        if (new_tail := removed_node.previous) is None:
            self.head = None
            self.tail = None
        else:
            new_tail.succeeding = None
            self.tail = new_tail
        self.length -= 1
        return removed_node.value

    def unshift(self, value: int) -> None:
        """Insert a value at the head of the list."""
        new_node = Node(value=value, succeeding=self.head, previous=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def shift(self) -> int:
        """Remove and return the value at the head of the list."""
        if self.head is None:
            raise IndexError("List is empty")

        removed_node = self.head
        if (new_head := removed_node.succeeding) is None:
            self.head = None
            self.tail = None
        else:
            new_head.previous = None
            self.head = new_head
        self.length -= 1
        return removed_node.value

    def delete(self, value: int) -> None:
        """Delete the first node containing the requested value."""
        current_node = self.head
        while current_node is not None and current_node.value != value:
            current_node = current_node.succeeding

        if current_node is None:
            raise ValueError("Value not found")

        previous_node = current_node.previous
        succeeding_node = current_node.succeeding

        if previous_node is None:
            self.head = succeeding_node
        else:
            previous_node.succeeding = succeeding_node

        if succeeding_node is None:
            self.tail = previous_node
        else:
            succeeding_node.previous = previous_node

        self.length -= 1

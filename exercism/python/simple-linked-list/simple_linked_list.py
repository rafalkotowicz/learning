"""Simple singly linked list implementation used by Exercism tests."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any


class EmptyListException(Exception):
    """Raised when an operation requires at least one list element."""

    def __init__(self) -> None:
        super().__init__("The list is empty.")


class Node:
    """Represent one linked-list element with a value and next pointer."""

    def __init__(self, value: Any, next_node: Node | None = None) -> None:
        self._value = value
        self._next_node = next_node

    def value(self) -> Any:
        """Return the value stored in the node."""
        return self._value

    def next(self) -> Node | None:
        """Return the next node in the list or None."""
        return self._next_node


class LinkedList:
    """LIFO-style linked list supporting push, pop and iteration."""

    def __init__(self, values: Iterable[Any] | None = None) -> None:
        self._head_node: Node | None = None
        self._length: int = 0

        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self) -> Iterator[Any]:
        """Iterate from the list head to the tail, yielding stored values."""
        current_node = self._head_node
        while current_node is not None:
            yield current_node.value()
            current_node = current_node.next()

    def __len__(self) -> int:
        """Return the number of elements currently stored in the list."""
        return self._length

    def head(self) -> Node:
        """Return the head node or raise when the list has no elements."""
        if self._head_node is None:
            raise EmptyListException()
        return self._head_node

    def push(self, value: Any) -> None:
        """Insert a value at the list head."""
        self._head_node = Node(value=value, next_node=self._head_node)
        self._length += 1

    def pop(self) -> Any:
        """Remove and return the value at the list head."""
        head_node = self.head()
        self._head_node = head_node.next()
        self._length -= 1
        return head_node.value()

    def reversed(self) -> LinkedList:
        """Create a new linked list with reverse traversal order."""
        reversed_list = LinkedList()
        for value in self:
            reversed_list.push(value)
        return reversed_list

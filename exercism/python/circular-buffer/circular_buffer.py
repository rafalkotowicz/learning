"""Circular buffer implementation for fixed-capacity FIFO data."""

from typing import Any


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class CircularBuffer:
    """Store values in a fixed-size ring and read them in FIFO order."""

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self._items: list[Any | None] = [None] * capacity
        self._read_index: int = 0
        self._write_index: int = 0
        self._item_count: int = 0

    def read(self) -> Any:
        """Remove and return the oldest stored value."""
        if not self._item_count:
            raise BufferEmptyException("Circular buffer is empty")

        value = self._items[self._read_index]
        self._items[self._read_index] = None
        self._read_index = self._advance_index(self._read_index)
        self._item_count -= 1
        return value

    def write(self, data: Any) -> None:
        """Add a value when free capacity is available."""
        if self._item_count == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self._write_value(data)

    def overwrite(self, data: Any) -> None:
        """Add a value and drop the oldest item if the buffer is full."""
        if self._item_count == self.capacity:
            self._read_index = self._advance_index(self._read_index)
            self._item_count -= 1
        self._write_value(data)

    def clear(self) -> None:
        """Reset the buffer to its initial empty state."""
        self._items = [None] * self.capacity
        self._read_index = 0
        self._write_index = 0
        self._item_count = 0

    def _write_value(self, data: Any) -> None:
        """Write a value into the current write slot and advance the pointer."""
        self._items[self._write_index] = data
        self._write_index = self._advance_index(self._write_index)
        self._item_count += 1

    def _advance_index(self, index_value: int) -> int:
        """Move an index one step forward in the ring."""
        return (index_value + 1) % self.capacity

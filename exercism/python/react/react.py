"""Reactive cells implementation for the Exercism React exercise."""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Sequence
from itertools import count

CREATION_COUNTER = count()


class Cell:
    """Common behavior shared by input and compute cells."""

    def __init__(self, initial_value: object) -> None:
        self._value = initial_value
        self._dependent_cells: set[ComputeCell] = set()

    @property
    def value(self) -> object:
        """Return the current cell value."""
        return self._value

    def add_dependent(self, dependent_cell: ComputeCell) -> None:
        """Register a compute cell that depends on this cell."""
        self._dependent_cells.add(dependent_cell)

    def dependent_cells(self) -> set[ComputeCell]:
        """Expose downstream compute cells."""
        return self._dependent_cells


class InputCell(Cell):
    """A mutable source cell that notifies downstream compute cells."""

    @property
    def value(self) -> object:
        """Return the current input value."""
        return super().value

    @value.setter
    def value(self, new_value: object) -> None:
        """Set a new value and propagate updates when it changes."""
        if self._value == new_value:
            return

        self._value = new_value
        _propagate_updates(self.dependent_cells())


class ComputeCell(Cell):
    """A cell whose value is derived from input and compute dependencies."""

    def __init__(
        self,
        inputs: Sequence[InputCell | ComputeCell],
        compute_function: Callable[[list[object]], object],
    ) -> None:
        """Create a compute cell connected to dependency inputs."""
        self._inputs = list(inputs)
        self._compute_function = compute_function
        self._callbacks: list[Callable[[object], None]] = []
        self._creation_order = next(CREATION_COUNTER)

        for input_cell in self._inputs:
            input_cell.add_dependent(self)

        super().__init__(self._compute_value())

    def add_callback(self, callback: Callable[[object], None]) -> None:
        """Register a callback to be fired after stable value changes."""
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def remove_callback(self, callback: Callable[[object], None]) -> None:
        """Unregister a callback if present."""
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def creation_order(self) -> int:
        """Expose creation order used for deterministic graph traversal."""
        return self._creation_order

    def callbacks(self) -> list[Callable[[object], None]]:
        """Expose registered callbacks."""
        return self._callbacks

    def input_cells(self) -> list[InputCell | ComputeCell]:
        """Expose dependencies used to compute the cell value."""
        return self._inputs

    def recompute(self) -> None:
        """Recalculate and store the value from current dependency values."""
        self._value = self._compute_value()

    def _compute_value(self) -> object:
        input_values = [input_cell.value for input_cell in self._inputs]
        return self._compute_function(input_values)


def _propagate_updates(starting_cells: set[ComputeCell]) -> None:
    if not starting_cells:
        return

    ordered_cells = _topological_order(starting_cells)
    previous_values = {compute_cell: compute_cell.value for compute_cell in ordered_cells}

    for compute_cell in ordered_cells:
        compute_cell.recompute()

    for compute_cell in ordered_cells:
        if previous_values[compute_cell] != compute_cell.value:
            for callback_function in compute_cell.callbacks():
                callback_function(compute_cell.value)


def _topological_order(starting_cells: set[ComputeCell]) -> list[ComputeCell]:
    reachable_cells: set[ComputeCell] = set()
    stack: list[ComputeCell] = list(starting_cells)

    while stack:
        if (current_cell := stack.pop()) in reachable_cells:
            continue

        reachable_cells.add(current_cell)
        stack.extend(current_cell.dependent_cells())

    incoming_edges: dict[ComputeCell, int] = {compute_cell: 0 for compute_cell in reachable_cells}
    for compute_cell in reachable_cells:
        for input_cell in compute_cell.input_cells():
            if isinstance(input_cell, ComputeCell) and input_cell in reachable_cells:
                incoming_edges[compute_cell] += 1

    ready_cells = deque(
        sorted(
            [compute_cell for compute_cell, edge_count in incoming_edges.items() if not edge_count],
            key=lambda compute_cell: compute_cell.creation_order(),
        )
    )
    sorted_cells: list[ComputeCell] = []

    while ready_cells:
        current_cell = ready_cells.popleft()
        sorted_cells.append(current_cell)

        for dependent_cell in sorted(
            current_cell.dependent_cells(),
            key=lambda compute_cell: compute_cell.creation_order(),
        ):
            if dependent_cell not in incoming_edges:
                continue

            incoming_edges[dependent_cell] -= 1
            if not incoming_edges[dependent_cell]:
                ready_cells.append(dependent_cell)

    return sorted_cells

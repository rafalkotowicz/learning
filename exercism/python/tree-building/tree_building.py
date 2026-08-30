"""Build a tree from flat record definitions."""

from __future__ import annotations


class Record:  # pylint: disable=too-few-public-methods
    """Input record containing node id and its parent id."""

    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id


class Node:  # pylint: disable=too-few-public-methods
    """Node in the resulting tree."""

    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children: list[Node] = []


def BuildTree(records: list[Record]) -> Node | None:  # pylint: disable=invalid-name
    """Validate records and build a rooted tree, returning root or None."""
    if not records:
        return None

    ordered_records = sorted(records, key=lambda record: record.record_id)
    _validate_record_ids(ordered_records)
    _validate_parent_rules(ordered_records)

    node_by_id: dict[int, Node] = {
        record.record_id: Node(record.record_id) for record in ordered_records
    }

    for record in ordered_records[1:]:
        parent_node = node_by_id[record.parent_id]
        child_node = node_by_id[record.record_id]
        parent_node.children.append(child_node)

    return node_by_id[0]


def _validate_record_ids(ordered_records: list[Record]) -> None:
    """Ensure record ids are contiguous and start at zero."""
    for expected_id, record in enumerate(ordered_records):
        if record.record_id != expected_id:
            raise ValueError("Record id is invalid or out of order.")


def _validate_parent_rules(ordered_records: list[Record]) -> None:
    """Ensure parent relationships do not create invalid trees."""
    for record in ordered_records:
        if record.parent_id > record.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")

        if record.record_id == record.parent_id and record.record_id:
            raise ValueError("Only root should have equal record and parent id.")

"""Zipper implementation for immutable navigation and updates on binary trees."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

TreeNode = dict[str, Any]
LEFT_DIRECTION = "left"
RIGHT_DIRECTION = "right"


@dataclass(frozen=True)
class Breadcrumb:
    """Stores enough context to rebuild the parent node when moving up."""

    direction: str
    parent_value: Any
    sibling_subtree: TreeNode | None


class Zipper:
    """Navigates and updates a binary tree while keeping focus and path context."""

    def __init__(self, focus_tree: TreeNode, breadcrumbs: list[Breadcrumb]) -> None:
        self._focus_tree = focus_tree
        self._breadcrumbs = breadcrumbs

    @staticmethod
    def from_tree(tree: TreeNode) -> Zipper:
        """Create a zipper focused on the root of the provided tree."""
        return Zipper(deepcopy(tree), [])

    def value(self) -> Any:
        """Return value at the current focus."""
        return self._focus_tree["value"]

    def set_value(self, value: Any) -> Zipper:
        """Return a new zipper with updated value at current focus."""
        updated_focus = deepcopy(self._focus_tree)
        updated_focus["value"] = value
        return Zipper(updated_focus, self._breadcrumbs.copy())

    def left(self) -> Zipper | None:
        """Move focus to the left child if it exists."""
        if (left_child := self._focus_tree[LEFT_DIRECTION]) is None:
            return None

        updated_breadcrumbs = self._breadcrumbs.copy()
        updated_breadcrumbs.append(
            Breadcrumb(
                direction=LEFT_DIRECTION,
                parent_value=self._focus_tree["value"],
                sibling_subtree=deepcopy(self._focus_tree[RIGHT_DIRECTION]),
            )
        )
        return Zipper(deepcopy(left_child), updated_breadcrumbs)

    def set_left(self, left_subtree: TreeNode | None) -> Zipper:
        """Return a new zipper with replaced left subtree at current focus."""
        updated_focus = deepcopy(self._focus_tree)
        updated_focus["left"] = deepcopy(left_subtree)
        return Zipper(updated_focus, self._breadcrumbs.copy())

    def right(self) -> Zipper | None:
        """Move focus to the right child if it exists."""
        if (right_child := self._focus_tree[RIGHT_DIRECTION]) is None:
            return None

        updated_breadcrumbs = self._breadcrumbs.copy()
        updated_breadcrumbs.append(
            Breadcrumb(
                direction=RIGHT_DIRECTION,
                parent_value=self._focus_tree["value"],
                sibling_subtree=deepcopy(self._focus_tree[LEFT_DIRECTION]),
            )
        )
        return Zipper(deepcopy(right_child), updated_breadcrumbs)

    def set_right(self, right_subtree: TreeNode | None) -> Zipper:
        """Return a new zipper with replaced right subtree at current focus."""
        updated_focus = deepcopy(self._focus_tree)
        updated_focus["right"] = deepcopy(right_subtree)
        return Zipper(updated_focus, self._breadcrumbs.copy())

    def up(self) -> Zipper | None:  # pylint: disable=disallowed-name,useless-suppression
        """Move focus to parent node if there is one."""
        if not self._breadcrumbs:
            return None

        last_breadcrumb = self._breadcrumbs[-1]
        remaining_breadcrumbs = self._breadcrumbs[:-1]

        is_left_child = last_breadcrumb.direction == LEFT_DIRECTION
        rebuilt_parent = {
            "value": last_breadcrumb.parent_value,
            "left": deepcopy(self._focus_tree)
            if is_left_child
            else deepcopy(last_breadcrumb.sibling_subtree),
            "right": deepcopy(last_breadcrumb.sibling_subtree)
            if is_left_child
            else deepcopy(self._focus_tree),
        }

        return Zipper(rebuilt_parent, remaining_breadcrumbs)

    def to_tree(self) -> TreeNode:
        """Return the full tree represented by this zipper."""
        if (parent_zipper := self.up()) is None:
            return deepcopy(self._focus_tree)
        return parent_zipper.to_tree()

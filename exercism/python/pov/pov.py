"""Tree re-rooting and path-finding utilities for the POV exercise."""

from json import dumps


class Tree:
    """Node-based tree representation used by the POV exercise."""

    __hash__ = None

    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def to_dict(self):
        """Return a stable dictionary form used by tests and string output."""
        return {self.label: [child.to_dict() for child in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    @staticmethod
    def _clone_subtree(node):
        return Tree(node.label, [Tree._clone_subtree(child) for child in node.children])

    def path_from_root(self, target_label):
        """Return node objects on the path from this root to target_label."""
        if self.label == target_label:
            return [self]

        for child in self.children:
            if (child_path := child.path_from_root(target_label)) is not None:
                return [self] + child_path

        return None

    def from_pov(self, from_node):
        """Return a new tree re-rooted from the perspective of from_node."""
        if (path := self.path_from_root(from_node)) is None:
            raise ValueError("Tree could not be reoriented")

        new_root = Tree._clone_subtree(path[-1])
        current = new_root

        for index in range(len(path) - 2, -1, -1):
            ancestor = path[index]
            child_on_path = path[index + 1]
            siblings = [
                Tree._clone_subtree(child)
                for child in ancestor.children
                if child is not child_on_path
            ]
            parent_from_current_pov = Tree(ancestor.label, siblings)
            current.children.append(parent_from_current_pov)
            current = parent_from_current_pov

        return new_root

    def path_to(self, from_node, to_node):
        """Return labels on the path from from_node to to_node."""
        reoriented = self.from_pov(from_node)
        if (path := reoriented.path_from_root(to_node)) is None:
            raise ValueError("No path found")

        return [node.label for node in path]

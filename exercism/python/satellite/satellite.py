"""Satellite exercise solution: rebuild a binary tree from traversals."""

from collections import Counter


def tree_from_traversals(preorder, inorder):
    """Rebuild a binary tree from preorder and inorder traversals."""
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    preorder_counts = Counter(preorder)
    inorder_counts = Counter(inorder)

    if preorder_counts != inorder_counts:
        raise ValueError("traversals must have the same elements")

    if len(preorder_counts) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder:
        return {}

    inorder_indexes = {
        node_value: node_index for node_index, node_value in enumerate(inorder)
    }

    def build_subtree(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start >= preorder_end:
            return {}

        root_value = preorder[preorder_start]
        root_inorder_index = inorder_indexes[root_value]

        if root_inorder_index < inorder_start or root_inorder_index >= inorder_end:
            raise ValueError("traversals must have the same elements")

        left_size = root_inorder_index - inorder_start
        left_subtree = build_subtree(
            preorder_start + 1,
            preorder_start + 1 + left_size,
            inorder_start,
            root_inorder_index,
        )
        right_subtree = build_subtree(
            preorder_start + 1 + left_size,
            preorder_end,
            root_inorder_index + 1,
            inorder_end,
        )

        return {"v": root_value, "l": left_subtree, "r": right_subtree}

    return build_subtree(0, len(preorder), 0, len(inorder))

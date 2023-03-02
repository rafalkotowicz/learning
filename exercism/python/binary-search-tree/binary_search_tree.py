class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data: [str]):
        self.root: TreeNode = None
        self.sorted: [str] = list()
        for data in tree_data:
            self.root = self.create_leaf(self.root, TreeNode(data))

    def create_leaf(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if root is None:
            root = node
            return root
        elif int(node.data) <= int(root.data):
            root.left = self.create_leaf(root.left, node)
        else:
            root.right = self.create_leaf(root.right, node)

        return root

    def data(self) -> TreeNode:
        return self.root

    def sorted_data(self) -> [str]:
        self.sorted_helper(self.root)
        return self.sorted

    def sorted_helper(self, root: TreeNode):
        if root is not None:
            self.sorted_helper(root.left)
            self.sorted.append(root.data)
            self.sorted_helper(root.right)

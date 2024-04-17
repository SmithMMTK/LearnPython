class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, parent_node, value):
        new_node = BTNode(value)
        parent_node.left = new_node

    def insert_right(self, parent_node, value):
        new_node = BTNode(value)
        parent_node.right = new_node

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

# Example usage:
binary_tree = BinaryTree()
binary_tree.root = BTNode(30)  # Manually set the root node
binary_tree.insert_left(binary_tree.root, 15)  # Manually insert 15 as left child of 30
binary_tree.insert_right(binary_tree.root, 7)  # Manually insert 7 as right child of 30

binary_tree.print_tree(binary_tree.root)

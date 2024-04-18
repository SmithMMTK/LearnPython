class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BTNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:  # Handles value >= current_node.value
            if current_node.right is None:
                current_node.right = BTNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def find(self, value):
        return "Found" if self._find_recursive(self.root, value) else "Not Found"

    def _find_recursive(self, current_node, value):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._find_recursive(current_node.left, value)
        else:
            return self._find_recursive(current_node.right, value)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

# Example usage:
data = [15,10,20,5,12,17,25,3,7,11,13,16,18,23,27]
binary_tree = BinaryTree()
for num in data:
    binary_tree.insert(num)


binary_tree.print_tree(binary_tree.root)

print("Find 10: ", binary_tree.find(7))  # Test finding an existing number
print("Find 22: ", binary_tree.find(22))  # Test finding a non-existing number

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1
 
class AVLTree:
    def __init__(self):
        self.root = None
 
    def insert(self, value):
        self.root = self._insert_helper(self.root, value)
 
    def _insert_helper(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left_child = self._insert_helper(node.left_child, value)
        else:
            node.right_child = self._insert_helper(node.right_child, value)
 
        node.height = 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))
 
        balance_factor = self._get_balance_factor(node)
 
        if balance_factor > 1 and value < node.left_child.value:
            return self._right_rotate(node)
 
        if balance_factor < -1 and value > node.right_child.value:
            return self._left_rotate(node)
 
        if balance_factor > 1 and value > node.left_child.value:
            node.left_child = self._left_rotate(node.left_child)
            return self._right_rotate(node)
 
        if balance_factor < -1 and value < node.right_child.value:
            node.right_child = self._right_rotate(node.right_child)
            return self._left_rotate(node)
 
        return node
 
    def _get_height(self, node):
        if not node:
            return 0
 
        return node.height
 
    def _get_balance_factor(self, node):
        if not node:
            return 0
 
        return self._get_height(node.left_child) - self._get_height(node.right_child)
 
    def _left_rotate(self, node):
        temp_right_child = node


# Create an empty AVL tree
avl_tree = AVLTree()

# Insert some values into the tree
avl_tree.insert(5)
avl_tree.insert(3)
avl_tree.insert(7)
avl_tree.insert(2)
avl_tree.insert(4)
avl_tree.insert(6)
avl_tree.insert(8)

# Print the contents of the tree
print("AVL tree contents:")
print(avl_tree.root.value)
print(avl_tree.root.left_child.value, avl_tree.root.right_child.value)
print(avl_tree.root.left_child.left_child.value, avl_tree.root.left_child.right_child.value, 
      avl_tree.root.right_child.left_child.value, avl_tree.root.right_child.right_child.value)

# Delete some values from the tree
avl_tree.delete(4)
avl_tree.delete(7)

# Print the contents of the tree again
print("AVL tree contents after deleting 4 and 7:")
print(avl_tree.root.value)
print(avl_tree.root.left_child.value, avl_tree.root.right_child.value)
print(avl_tree.root.left_child.left_child.value, avl_tree.root.left_child.right_child.value, 
      avl_tree.root.right_child.right_child.value)
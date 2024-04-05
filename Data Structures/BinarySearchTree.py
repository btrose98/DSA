"""
    Binary Search Tree:
    - Each node has up to 2 children.
    - All nodes in the left subtree are smaller than the current node. All nodes in the right subtree are greater than
        the current node.
    - Provides rapid traversal and comparison of elements.
    - Time Complexity:
        > Best case: O(log n)
        > Worst case (unbalanced): o(n)
    - Used where efficient searching, insertion and deletion operations are required:
        > Database indexing
        > Symbol Tables
        > Implementing Set and Map data structures

    Steps:
    1. Start at root.
    2. Compare target to root.
    3. If target is:
        a) == to root, return the current node.
        b) < root, move to the left child. Repeat recursively.
        c) > root, move to the right child. Repeat recursively.
    4. Repeat until target value (3a) is found or until a leaf node is reached. Insert node as a new leaf.

    .. image:: ../assets/bst_image.png
        :align: center
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, x):
        if not self.data:
            self.data = x
            return

        # Case: already in the tree, don't add
        if x == self.data:
            print(f"{x} already in the tree")
            return

        elif x < self.data:
            if self.left:
                self.left.insert(x)
                return

            # reached the end of the tree, add as a leaf
            self.left = Node(x)
            return

        elif x > self.data:
            if self.right:
                self.right.insert(x)
                return

            # reached end of the tree, add as leaf
            self.right = Node(x)
            return

    def exists(self, x):
        if x == self.data:
            return True
        elif x < self.data and self.left:
            return self.left.exists(x)
        elif x > self.data and self.right:
            return self.right.exists(x)
        return False

    # TODO
    def delete(self, x):
        pass

    def get_min(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right
        return current_node

    def inorder(self, vals):
        """
        Left-Current-Right
        :param vals:
        :return:
        """
        if self.left:
            self.left.inorder(vals)
        if self.data:
            vals.append(self.data)
        if self.right:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        """
        Current-left-right
        :param vals:
        :return:
        """
        vals.append(self.data)
        if self.left:
            self.left.preorder(vals)
        if self.right:
            self.right.preorder(vals)

    def postorder(self, vals):
        """
        Left-Right-Current
        :param vals:
        :return:
        """
        if self.left:
            self.left.postorder(vals)
        if self.right:
            self.right.postorder(vals)
        vals.append(self.data)



test_data = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
bst = Node()
for num in test_data:
    bst.insert(num)

# min = bst.get_min()
# print(min.data)

# print(bst.search(40))

# print(bst.inorder([]))
print(bst.preorder([]))
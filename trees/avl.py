__author__ = 'kingofspace0wzz'

import bst
# implemetation of AVL tree
# AVL tree is a balanced binary search tree, the heights of the subtrees of whose nodes differ at most by 1
# Each node stores its height
# Since the height is balanced, all operations run in O(nlogn)

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(node.left.height, node.right.height) + 1


class AVL(bst.BST):

    def left_rotation(self, node):
        '''left rotation around current node'''
        y = node.right
        y.parent = node.parent
        if y.parent is None:
            self.root = y
        else:
            if node is y.parent.left:
                y.parent.left = y
            elif node is y.parent.right:
                y.parent.right = y

        node.right = y.left
        if node.right is not None:
            node.right.parent = node

        y.left = node
        node.parent = y
        update_height(node)
        update_height(y)

    def right_rotation(self, node):
        '''right rotation around current node'''
        x = node.left
        x.parent = node.parent
        if x.parent is None:
            self.root = x
        else:
            if node is x.parent.left:
                x.parent.left = x
            elif node is x.parent.right:
                x.parent.right = x

        node.left = x.right
        if node.left is not None:
            node.left.parent = node

        node.parent = x
        x.right = node
        update_height(node)
        update_height(x)


    def balance(self, node):
        '''rebalance the tree iteratively to make the heights of each node balanced'''
        update_height(node)
        while node is not None:

            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotation(node)
                else:
                    self.left_rotation(node.left)
                    self.right_rotation(node)       # double rotation
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotation(node)
                else:
                    self.right_rotation(node.right)
                    self.left_rotation(node)

            node = node.parent

    def insert(self, k):
        '''Insert a node into the subtrees of the current node

        Args:
            k: key of the node to be inserted

        Returns:
            node inserted
        '''

        node = super(AVL, self).insert(k)
        self.balance(node)
        return node

    def delete(self, k):
        '''Delete a node from the subtrees of the current node

        Args:
            k: key of the node to be deleted

        Returns:
            node deleted
        '''

        node = super(AVL, self).delete(k)
        self.balance(node.parent)
        return node

__author__ = 'kingofspace0wzz'

import bst

# implemetation of Red Black tree
# Red Black tree is a Binary Search Tree with an extra bit of storage about Color per node

# Every node is either red or Black
# The root is Black
# Every leaf(None) is Black
# If a node is red, then both its children are Black
# For each node, all simple paths from the node to descendant leaves contain the same number of black nodes

# A red-black tree with n internal nodes has height at most 2lg(n+1)

def color(node):
    if node is None:
        return 'black'
    else:
        return node.color



class red_black(bst.BST):
    '''red black tree'''

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


    def rb_balance(self, node):

        while node.parent.color is 'red':
            if node.parent is node.parent.parent.left:
                y = node.parent.parent.right
                if y.color is 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                elif node is node.parent.right:
                    node = node.parent
                    left_rotation(self, node)

                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    right_rotation(self, node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color is 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                elif node is node.parent.left:
                    node = node.parent
                    right_rotation(self, node)

                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    left_rotation(self, node.parent.parent)

        self.root.color = 'black'


    def insert(self, k):

        node = super(red_black, self).insert(k)
        node.color = 'red'
        self.rb_balance(node)

        return node

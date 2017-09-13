__author__ = 'kingofspace0wzz'

# implemetation of Binary Search Tree


class BSTNode(object):
    '''Node of Binary Search tree'''

    def __init__(self, parent, k):
        '''Create a BST node

        Args:
            parent: node's parent
            k: node's key

        '''
        self.parent = parent
        self.key = k
        self.left = None
        self.right = None

    def __str__(self):
        '''Print the subtree of the current node'''
        if self is not None:
            self.left.__str__()
            print self.key
            self.right.__str__()

    def search(self, k):
        '''Search and return the node with key k from the subtrees of the current node
        Use iterative method rather than recursion

        Args:
            k: key

        Returns:
            node with key k
        '''
        #---Iteration---
        if self.key == k:
            return self

        x = self
        while k != x.key:
            if k < x.key:
                if x.left is None:
                    return None
                else:
                    x = x.left

            if k > x.key:
                if x.right is None:
                    return None
                else:
                    x =x.right

        return x

        # ---Recursion---
        # if self.key == k
        #   return self
        # elif k < self.key:
        #    if self.left is None:
        #        return None
        #    else:
        #        return self.left.search(k)
        # else:
        #    if self.right is None:
        #        return None
        #    else:
        #        return self.right.search(k)



    def search_min(self):
        '''find the node with minimum key from the subtrees of the current node

        Returns:
            node with minimum key
        '''
        x = self
        while self.left is not None:
            x = x.left
        return x

    def search_max(self):
        '''find the node with minimum key from the subtrees of the current node

        Returns:
            node with minimum key
        '''
        x = self
        while self.right is not None:
            x = x.right
        return x

    def successor(self):
        '''find the node with the smallest key greater than self.key

        Returns:
            node with the smallest key greater than self.key
        '''

        if self.right is not None:
            return search_min(self.right)

        y = self.parent
        x = self
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y


    def predecessor(self):
        '''find the node with the largest key smaller than self.key

        Returns:
            node with the largest key smaller than self.key
        '''

        if self.left is not None:
            return search_max(self.left)

        y = self.parent
        x = self
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def insert(self, node):
        '''Insert a node into the subtrees of the current node

        Args:
            node: the node that needs to be inserted
        '''

        if node is None:
            return

        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)



    def delete(self):
        '''Delete a node from the subtrees of the current node

        Args:
            node: the node to be deleted

        Returns:
            node deleted
        '''

        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            y = successor(self)
            self.key = y.key
            y.parent.left = y.right
            y.right.parent = y.parent
            return self


class BST(object):
    '''Binary Search Tree'''

    def __init__(self):
        '''Create a Binary Search Tree'''

        self.root = None

    def __print__(self):
        '''Print the tree'''
        self.root.__print__()

    def search(self, k):
        '''Search and return the node with key k from the subtrees of the current node
        Use iterative method rather than recursion

        Args:
            k: key

        Returns:
            node with key k
        '''
        if self.root is None:
            return None     # empty tree
        else:
            return self.root.search(k)

    def search_min(self):
        '''find the node with minimum key from the subtrees of the current node

        Returns:
            node with minimum key
        '''
        if self.root is None:
            return None   # empty tree
        else:
            self.root.search_min()

    def search_max(self):
        '''find the node with minimum key from the subtrees of the current node

        Returns:
            node with minimum key
        '''
        if self.root is None:
            return None
        else:
            self.root.search_max()

    def successor(self, k):
        '''find the node with the smallest key greater than self.key

        Args:
            k: key of the current node

        Returns:
            node with the smallest key greater than self.key
        '''
        node = self.search(k)
        return node.successor()


    def predecessor(self, k):
        '''find the node with the largest key smaller than self.key

        Args:
            k: key of the current node

        Returns:
            node with the largest key smaller than self.key
        '''
        node = self.search(k)
        return node.predecessor()

    def insert(self, k):
        '''Insert a node into the subtrees of the current node

        Args:
            k: key of the node to be inserted

        Returns:
            node inserted
        '''

        node = BSTNode(None, k)

        if self.root is None:   # empty tree
            self.root = node
        else:
            self.root.insert(node)

        return node

    def delete(self, k):
        '''Delete a node from the subtrees of the current node

        Args:
            k: key of the node to be deleted

        Returns:
            node deleted
        '''

        node = self.search(k)

        if node is None:
            return None
        elif node is self.root:
            temproot = BSTNode(None, 0)
            temproot.left = self.root
            self.root.parent = temproot
            deleted_node = self.root.delete()
            self.root = temproot.left
            if self.root is not None:
                self.root.parent = None
            return deleted_node
        else:
            return node.delete()

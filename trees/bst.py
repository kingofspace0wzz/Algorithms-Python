__author__ = 'kingofspace0wzz'

# implemetation of Binary Search Tree


class BSTNode(object):


    def __init__(self, parent, k):

        self.parent = parent
        self.key = k
        self.left = None
        self.right = None


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



        def delete(self, node):
            '''Delete a node into the subtrees of the current node

            Args:
                node: the node to be deleted
            '''

            

# BST file for task 2:
# Write a class BSTToHeapTransformer that takes the root node of a 
# BST and converts it into a Min-Heap and Max-Heap. To write this 
# BSTToHeapTransformer class, You must utilize your implemented BST class. 
# Write sample test cases to validate your implementation.

from collections import deque
# Comes from our created bst class
class BSTNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None

# Better understanding for BST:
# GeeksforGeeks. (2026h, September 21). Binary search tree in python. https://www.geeksforgeeks.org/python/binary-search-tree-in-python/ 
# AlgoMonster. (n.d.). 285. inorder successor in BST. https://algo.monster/liteproblems/285 

class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):
        ''' Inserts/attach the node in the tree. it creates the node and then
        assigns the node to the tree, then connects it'''
        new_node = BSTNode(value)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.data < current.data:
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right

    def search(self, key):
        ''' Search for nodes in the tree '''
        current = self.root
        
        while current is not None:
            if key == current.data:
                return current
            if key < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def delete(self, key):
        ''' Delete a node in the tree '''
        node = self.search(key)

        if node is None:
            print(f"Warning {key} not found")
            return
        
        # delete a leaf
        if node.left is None and node.right is None:
            parent = node.parent
            if parent is None:
                self.root = None
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

        # delete a node w/ child 
        elif node.left is None or node.right is None:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            parent = node.parent

            if parent is None:
                root = child
            elif parent.left is node:
                parent.left = child
            else:
                parent.right = parent
            
            child.parent = parent

        # delete with two children
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.data = successor.data

            # Removing the successor 
            child = successor.right
            parent = successor.parent

            if parent.left is successor:
                parent.left = child
            else:
                parent.right = child
            
            if child is not None:
                child.parent = parent
    
    # Needed a better understanding of traversal techniques:
    # GeeksforGeeks. (2025f, December 6). Tree traversal techniques. https://www.geeksforgeeks.org/dsa/tree-traversals-inorder-preorder-and-postorder/ 
    def inOrderTraversal(self):
        """ Visits node in order of left-root-right """
        traverse = []
        self.inOrderHelper(self.root, traverse)
        return traverse
    
    def inOrderHelper(self, node, traverse):
        if node is None:
            return
        self.inOrderHelper(node.left, traverse) 
        traverse.append(node)
        self.inOrderHelper(node.right, traverse)

    # From the skeleton provided in the assignments note
    # PreOrder
    def preOrder(self):
        """ Visits node root-left-right """
        traverse = []
        self.preOrder(self.root, traverse)
        return traverse
    
    def preOrderHelper(self, node, traverse):
        if node is None:
            return
        traverse.append(node)
        self.preOrderHelper(node.left, traverse) 
        self.preOrderHelper(node.right, traverse)

    #postOrder
    def postOrder(self):
        """ node visits in order left-right-root """
        traverse = []
        self.postOrder(self.root, traverse)
        return traverse
    
    def postOrderHelper(self, node, traverse):
        if node is None:
            return
        self.postOrderHelper(node.left, traverse) 
        self.postOrderHelper(node.right, traverse)
        traverse.append(node)

    # I am using dequeue from pythons standard library as the queue
    def levelOrderTraversal(self):
        result_list = []
        if self.root is None:
            return result_list
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result_list.append(node)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return result_list
    
tree = BST()

tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)




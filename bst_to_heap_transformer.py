# Continuation of task 2

from heap import Node


class BSTToHeapTransformer:
    
    def bstToMinHeap(self, bst):
        """ Turns a BST into a min-heap returning a list of linked heap Nodes.
         Root/ first node holds the smallest value"""
        bst_nodes = bst.inOrderTraversal()
        values = []

        # pull nums out of the BST nodes
        for node in bst_nodes:
            values.append(node.data)
        heap_nodes = self._build_heap_nodes(values)
        return heap_nodes

    def bstToMaxHeap(self, bst):
        """ Takes a BST and produces max-heap nodes. Root/ first node holds the largest value """
        bst_nodes = bst.inOrderTraversal()
        values = []

        # pull nums out of the BST nodes
        for node in bst_nodes:
            values.append(node.data)
        values.reverse()
        heap_nodes = self._build_heap_nodes(values)
        return heap_nodes


    # Helper method
    def _build_heap_nodes(self, values):
        """ Turns a list of nums into a list of linked heap Nodes """
        if not values:
            return values
        
        # disconnected nodes
        nodes = []
        for value in values:
            new_node = Node(value)
            nodes.append(new_node)

        # Wiring: takes a flat list of the separates nodes and links them into a tree
        for i in range(len(nodes)):
            left_index = 2 * i + 1
            # check left position
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            right_index = 2 * i + 2
            # check right position
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
        return nodes
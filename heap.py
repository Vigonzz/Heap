# Violet Gonzalez, october 26, 2026

# Task 1:
# Given a list of integers, write a class HeapBuilder that 
# takes the integer list, creates a heap, and returns that 
# heap as a binary tree. You have to implement both Max-Heap 
# and Min-Heap. Write sample test cases to validate your implementation.

class Node:
    ''' Creates the node '''
    def __init__(self, data):
        self.data  = data
        self.right = None
        self.left = None

class HeapBuilder:

    def createMinHeap(self, values):
        # Build the list and tree
        heap_list = self._build_array(values, True)
        root = self._array_to_tree(heap_list)
        return root

    def createMaxHeap(self, values):
        # Build the list and tree
        heap_list = self._build_array(values, False)
        root = self._array_to_tree(heap_list)
        return root

    # Helper methods:
    def _sift_up(self, heap_list, start_index, is_min_heap):
        ''' takes the value at start index  and moves it up towards 
        root until it find the right spot '''

        tracker = start_index
        while tracker > 0:
            parent = (tracker - 1) // 2
 
            if is_min_heap:
                should_swap = heap_list[tracker] < heap_list[parent]
            else:
                should_swap = heap_list[tracker] > heap_list[parent]
            
            # Example and additional reading for swapping vars on one line:
            # GeeksforGeeks. (2025e, July 23). Swap two variables in one line. https://www.geeksforgeeks.org/dsa/swap-two-variables-in-one-line-in-c-c-python-php-and-java/ 
            if should_swap:
                heap_list[tracker], heap_list[parent] = heap_list[parent], heap_list[tracker]
                tracker = parent
            else:
                break


    def _build_array(self, values, is_min_heap):
        ''' builds the array that is used in our heap. Inserts each value one at
         a time with sift-up, true (is_min_heap) means that its min heap and false would be
          max. Return a new list in heap order '''
        heap_list = []
        for value in values:
            heap_list.append(value)
            self._sift_up(heap_list, len(heap_list) - 1, is_min_heap)
        return heap_list

    def _array_to_tree(self, heap_list):
        ''' converts the array to the tree, by calculating the node position to change
         the heap list into linked nodes, by creating a node for each value '''
        if not heap_list:
            return None
        
        nodes = []
        for value in heap_list:
            new_node = Node(value)
            nodes.append(new_node)
        
        for i in range(len(nodes)):
            left_index = 2 * i + 1
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
        return nodes[0]

        

#test_node = Node(5)
#print(test_node.data, test_node.left, test_node.right)
#print(min_heap_test)

# Testing the heap
builder = HeapBuilder()
#test_list = [3,5,8,1]
#builder._sift_up(test_list, 3, True)
#print(test_list)

# TESTING break and that it stays true 
#build = HeapBuilder()
#test_list = [3,5,8,4]
#build._sift_up(test_list, 3, True)
#print(test_list)

# Testin false, max heap max branch and multi level climbing 
#build = HeapBuilder()
#test_list = [3,5,8,9]
#build._sift_up(test_list, 3, True)
#print(test_list)

# Testing the build_array (helper method)
test = builder._build_array([5, 3, 8, 1, 4], False)
print(test)


# Testing the build of min heap 
#min_heap = builder.createMinHeap([5, 3, 8, 1, 4])
#print(min_heap.data)

# Testing the build of max heap 
max_heap = builder.createMinHeap([5, 3, 8, 1, 4])
print(max_heap.data)
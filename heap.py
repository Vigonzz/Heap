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
        pass 

    def createMaxHeap(self, values):
        pass

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
        pass

    def _array_to_tree(self, heap_list):
        pass

#test_node = Node(5)
#print(test_node.data, test_node.left, test_node.right)
#print(min_heap_test)

builder = HeapBuilder()
test_list = [3,5,8,9]
builder._sift_up(test_list, 3, False)
print(test_list)
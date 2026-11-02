# Test file for heap.py this will cover the test cases required from the assignment
from heap import HeapBuilder
from bst import BST
from bst_to_heap_transformer import BSTToHeapTransformer

def is_valid_heap(node, is_min_heap):
    ''' Checks to see if the head is valid '''
    if node is None:
        return True 
    if node.left is not None:
        if is_min_heap:
            if node.data > node.left.data:
                return False
        else:
            if node.data < node.left.data:
                return False
            
    if node.right is not None:
        if is_min_heap:
            if node.data > node.right.data:
                return False
        else:
            if node.data < node.right.data:
                return False
    return is_valid_heap(node.left, is_min_heap) and is_valid_heap(node.right, is_min_heap) 


# Task 1:

# Is_valid_heap test 
print("\n---Is a valid heap---")
builder = HeapBuilder()
root = builder.createMinHeap([5, 3, 8, 1, 4])
print(is_valid_heap(root, True))
print(root.data)
root = builder.createMaxHeap([5, 3, 8, 1, 4])
print(is_valid_heap(root, False))
print(root.data)

print("-----------------")

# Single Value, i expect a return of the same value 
print("\n---Single Value---")
building = HeapBuilder()
single_min = building.createMinHeap([7])
print(is_valid_heap(single_min, True))
print(single_min.data)
single = building.createMaxHeap([7])
print(is_valid_heap(single, False))
print(single.data)


print("--------------")

# Duplicates Test 
print("\n--Duplicate Test--")
dupe_heap = HeapBuilder()
dupe = dupe_heap.createMinHeap([5,5,5])
print(is_valid_heap(dupe, True))
print(dupe.data)
dupe = dupe_heap.createMaxHeap([5,5,5])
print(is_valid_heap(dupe, False))
print(dupe.data)

print("--------------")

# Mixed Dupe test
print("\n---Mixed Duplicate Test---")
mixed = HeapBuilder()
mixed_dupe = mixed.createMinHeap([3,1,3,1])
print(is_valid_heap(mixed_dupe, True))
print(mixed_dupe.data)
mixed_dupe = mixed.createMaxHeap([3,1,3,1])
print(is_valid_heap(mixed_dupe, False))
print(mixed_dupe.data)

print("--------------")

# Test Already Sorted test
print("\n---Already Sorted---")
sort = HeapBuilder()
sorted_heap = sort.createMinHeap([1,2,3,4,5])
print(is_valid_heap(sorted_heap, True))
print(sorted_heap.data)
sorted_heap = sort.createMaxHeap([1,2,3,4,5])
print(is_valid_heap(sorted_heap, False))
print(sorted_heap.data)

print("--------------")

# Test for reverse sorted
print("\n---Reverse Sorted---")
rev = HeapBuilder()
rev_sorted = rev.createMinHeap([5,4,3,2,1])
print(is_valid_heap(rev_sorted, True))
print(rev_sorted.data)
rev_sorted = rev.createMaxHeap([5,4,3,2,1])
print(is_valid_heap(rev_sorted, False))
print(rev_sorted.data)

print("--------------")

# Test for negatives
print("\n---Test for Negatives---")
neg = HeapBuilder()
negative = neg.createMinHeap([-2,0,-7,4])
print(is_valid_heap(negative, True))
print(negative.data)
negative = neg.createMaxHeap([-2,0,-7,4])
print(is_valid_heap(negative, False))
print(negative.data)


print("--------------")

# Test for empty
print("\n---Empty Heap---")
em = HeapBuilder()
empty_heap_min = em.createMinHeap([])
print(is_valid_heap(empty_heap_min, True))
print(empty_heap_min)
empty_heap = em.createMaxHeap([])
print(is_valid_heap(empty_heap, False))
print(empty_heap)

# Task 2 test
print("\n---Task 2---")
tree = BST()
for value in [5,3,8,1,4]:
    tree.insert(value)
transformer = BSTToHeapTransformer()

# Min test
print("\n---BST to min-heap---")
min_nodes = transformer.bstToMinHeap(tree)
for node in min_nodes:
    print(node.data)
print(is_valid_heap(min_nodes[0], True))

# Max test
print("\n---BST to max-heap---")
max_nodes = transformer.bstToMaxHeap(tree)
for node in max_nodes:
    print(node.data)
print(is_valid_heap(max_nodes[0], False))

# BST unchange
print("\n---BST unchanged---")
unchanged = tree.inOrderTraversal()
for node in unchanged:
    print(node.data)
print("--root--")
print(tree.root.data)

# Empty BST
print("\n---Empty BST---")
empty_tree = BST()
print(transformer.bstToMinHeap(empty_tree))

# Skewed BST
print("\n---Skewed BST---")
skewed_tree = BST()
for node in [1, 2, 3, 4, 5]:
    skewed_tree.insert(node)

# converting to min-heap
print("\n--Skewed min--")
skew_min = transformer.bstToMinHeap(skewed_tree)
for node in skew_min:
    print(node.data)
print(is_valid_heap(skew_min[0], True))

# convert to max_heap
print("\n--Skewed Max")
skew_max = transformer.bstToMaxHeap(skewed_tree)
for node in skew_max:
    print(node.data)
print(is_valid_heap(skew_max[0], False))
# Test file for heap.py this will cover the test cases required from the assignment
from heap import HeapBuilder

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



# Is_valid_heap test 
builder = HeapBuilder()
root = builder.createMinHeap([5, 3, 8, 1, 4])
print(is_valid_heap(root, True))
print(root.data)
root = builder.createMaxHeap([5, 3, 8, 1, 4])
print(is_valid_heap(root, False))
print(root.data)

print("-----------------")

# Single Value, i expect a return of the same value 
building = HeapBuilder()
single = building.createMinHeap([7])
print(is_valid_heap(single, True))
single = building.createMaxHeap([7])
print(is_valid_heap(single, False))
print(single.data)


print("--------------")

# Duplicates Test 
dupe_heap = HeapBuilder()
dupe = dupe_heap.createMinHeap([5,5,5])
print(is_valid_heap(dupe, True))
print(dupe.data)
dupe = dupe_heap.createMaxHeap([5,5,5])
print(is_valid_heap(dupe, False))
print(dupe.data)

print("--------------")

# Mixed Dupe test
mixed = HeapBuilder()
mixed_dupe = mixed.createMinHeap([3,1,3,1])
print(is_valid_heap(mixed_dupe, True))
print(mixed_dupe.data)
mixed_dupe = mixed.createMaxHeap([3,1,3,1])
print(is_valid_heap(mixed_dupe, False))
print(mixed_dupe.data)

print("--------------")

# Test Already Sorted test
sort = HeapBuilder()
sorted_heap = sort.createMinHeap([1,2,3,4,5])
print(is_valid_heap(sorted_heap, True))
print(sorted_heap.data)
sorted_heap = sort.createMaxHeap([1,2,3,4,5])
print(is_valid_heap(sorted_heap, False))
print(sorted_heap.data)

print("--------------")

# Test for reverse sorted
rev = HeapBuilder()
rev_sorted = rev.createMinHeap([5,4,3,2,1])
print(is_valid_heap(rev_sorted, True))
print(rev_sorted.data)
rev_sorted = rev.createMaxHeap([5,4,3,2,1])
print(is_valid_heap(rev_sorted, False))
print(rev_sorted.data)

print("--------------")

# Test for negatives
neg = HeapBuilder()
negative = neg.createMinHeap([-2,0,-7,4])
print(is_valid_heap(negative, True))
print(negative.data)
negative = neg.createMaxHeap([-2,0,-7,4])
print(is_valid_heap(negative, False))
print(negative.data)


print("--------------")

# Test for empty
em = HeapBuilder()
empty_heap = em.createMinHeap([])
print(is_valid_heap(empty_heap, True))
print(empty_heap)
empty_heap = em.createMaxHeap([])
print(is_valid_heap(empty_heap, False))
print(empty_heap)

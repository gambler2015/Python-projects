#Write a Python program to push an item on the heap, then pop and return
#the smallest item from the heap.
"""
Expected Output:
Items in the heap:
('V', 1)
('V', 3)
('V', 2)
----------------------
Using heappushpop push item on the heap and return the smallest item.
('V', 2)
('V', 3)
('V', 6)
"""
import heapq
heap=[]
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
for i in heap:
    print(i)
print("pop items")
heapq.heappushpop(heap, ('V', 8))
print("Using heappushpop push item on the heap and return the smallest item.")
for a in heap:
    print(a)

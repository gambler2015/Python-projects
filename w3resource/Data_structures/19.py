#Write a Python program to push three items into the heap and print the 
#items from the heap.
#Expected Output:
#('V', 1)
#('V', 2)
#('V', 3)
import heapq
heap=[]
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 3))
for i in heap:
    print(i)

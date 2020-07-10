#Write a Python program to create a heapsort, pushing all values
#onto a heap and then popping off the smallest values one at a time.
#Expected Output:
#[10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100]
import heapq
def heapsort(h):
    heap=[]
    for i in h:
        heapq.heappush(heap, i)
    return [heapq.heappop(heap) for i in range(len(heap))] #pop smallest element
#and stored in list
k=[30,7,10,60,100,20,40,1,9,8,2,1,0,3,11,3]
print(heapsort(k)) #sorted elements

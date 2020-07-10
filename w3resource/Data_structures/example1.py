import heapq
li=[1,6,9,10,50,20,40,26,48]
heapq.heapify(li) #using heapify to convert list into heap
print(list(li))
for i in range(51, 59):
    heapq.heappush(li, i) #using heappush() to push element into heap
print(li)#print modified heap
heapq.heappop(li) #pop smalleaasat element
print(li)
print("smallest element popped is {}".format(heapq.heappop(li)))
heapq.heappushpop(li, 101) #this will first push 101 and then pop smallest ele
print(li)
print(heapq.heapreplace(li, 7)) #first pop will takes place and then push.
print(li)
print("the three largest number are: {}".format(heapq.nlargest(3, li))) #returns lagest
print("the three smallest number are: {}".format(heapq.nsmallest(3, li)))

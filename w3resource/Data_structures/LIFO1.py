import queue
q=queue.LifoQueue()
n=int(input("total Number want to put:"))
for i in range(0, n):
    q.put(input())
print("........After LIFO.........")
while not q.empty():
    print(q.get())
print()

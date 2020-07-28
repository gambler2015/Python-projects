import queue
q=queue.LifoQueue()
for i in range(4):
    q.put(i)
while not q.empty():
    print(q.get())
print()

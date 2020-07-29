#Write a Python program to create a FIFO queue.
import queue
q=queue.Queue()
for i in range(17, 22):
    q.put(i)
t=1
while not q.empty():
    print("{}-Element out".format(t))
    print(q.get())
    t=t+1


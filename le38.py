import queue
q=queue.Queue()
#put insert items at the end of the queue
for i in range(1,(int(input("Enter no of items in Queue:"))+1)):
    q.put(str(input("Enter values:")))
while not q.empty():
    print(q.get(),end="  ")

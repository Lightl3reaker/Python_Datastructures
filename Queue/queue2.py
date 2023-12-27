from queue import Queue
q=Queue()
for i in range(0,11):
    q.put(i)
print("Size of queue:",q.qsize())
for i in range(q.qsize()):
    print(q.get())

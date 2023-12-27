import collections
from collections import deque
##Queue-->first in(append left),first out(pop)
list1=[1,2,3]
list1=deque(list1)
queue=deque([1,2,3])
print("attributes of deque-->",dir(deque))
print("Type of list1 after converting to dequeue->",type(list1))
print("Items of list1:",list(list1))
print("Items of queue:",list(queue))
print("Making a Queue")
print("Adding items to a queue")
queue.appendleft(6)
queue.appendleft(8)
print("Queue",list(queue))
print("Removing items to a queue")
queue.pop()
queue.pop()
print("Queue",list(queue))


class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, *elements):
        self.queue.extend(elements)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return "Queue is empty"
        
    
    # The insert method can also be used
        
    # def enqueue(self, elements):
        # self.queue.insert(0, elements)
    # def dequeue(self):
    #     if self.queue:
    #         return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()

queue.enqueue("10")
queue.enqueue("20")
queue.enqueue("30")

print(queue.queue)

queue.dequeue()

print(queue.queue)
print(queue.isEmpty())

# The queue is implemented using the "collections" library 
# import collections
# q = collections.deque()
# q.appendleft(10)   The appending element method
# q.pop()   The popped element method

# appendleft goes with pop. append goes with popleft
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)
    print(f"{item} pushed into stack")

  def safe_pop(self):
    if len(self.stack) == 0:
      print("Stack is empty, nothing to pop.")
      return None
    else:
      return self.stack.pop()

  def display(self):
    print("Stack:", self.stack)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Popped element:", s.safe_pop())
print("Popped element:", s.safe_pop())
print("Popped element:", s.safe_pop())
print("Popped element:", s.safe_pop())




from collections import deque

class Queue:
  def __init__(self):
    self.queue = deque()

  def enqueue(self, item):
    self.queue.append(item)
    print(f"{item} added to queue")

  def safe_dequeue(self):
    if len(self.queue) == 0:
      print("Queue is empty, cannot dequeue.")
      return None
    else:
      return self.queue.popleft()

  def display(self):
    print("Queue:", list(self.queue))


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())


print("Dequeued element:", q.safe_dequeue())

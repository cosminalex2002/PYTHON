class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.items[0]
        else:
            return None

    def empty(self):
        return len(self.items) == 0

    def printQueue(self):
        return self.items


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(67)

print(queue.printQueue())

print("peek:", queue.peek())

pop = queue.pop()
print("pop:", pop)

print("peek again:", queue.peek())

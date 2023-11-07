class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def empty(self):
        return len(self.items) == 0

    def printStack(self):
        return self.items


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(67)


print(stack.printStack())

print("peek:", stack.peek())

pop = stack.pop()
print("pop:", pop)

print("peek again", stack.peek())

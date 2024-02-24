class Stack:

    def __init__(self):
        self.stack = []

    def push(self, *elements):
        self.stack.extend(elements)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return 0

    def getTop(self):
        if self.stack:
            return self.stack[-1]
        
        # Extra Functions By me

    def reverseWord(self):
        self.stack.reverse()

    
    def isEmpty(self):
        return not bool(self.stack)


stack = Stack()

stack.push("a", "h", "m", "e", "d", " ", "a", "z", "z", "a", "m")

print(stack.stack)

stack.reverseWord()

print(stack.stack)

print(stack.getTop())

print(stack.isEmpty())

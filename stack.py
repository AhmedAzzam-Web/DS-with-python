class Stack:

    stack = []

    def push(self, *elements):
        for element in elements:
            Stack.stack.append(element)

    def pop(self):
        Stack.stack.pop()

    def getTop(self):
        print(Stack.stack[-1])
        return Stack.stack[-1]
    
    def isEmpty(self):
        if len(Stack.stack):
            print('There are elements in stack')
            return True
        else:
            print('Stack is empty')
            return False


stack = Stack()

stack.push(1,2,3)

print(stack.stack)

stack.pop()

print(stack.stack)

stack.getTop()

stack.isEmpty()
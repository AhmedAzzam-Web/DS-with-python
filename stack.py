class Stack:

    stack = []

    def push(self, *elements):
        for element in elements:
            Stack.stack.append(element)

    
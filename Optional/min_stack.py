class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.non_empty(self.stack):
            self.stack.pop(-1)

    def top(self):
        if self.non_empty(self.stack):
            return self.stack[-1]

    def get_min(self):
        if self.non_empty(self.stack):
            return min(self.stack)

    @staticmethod
    def non_empty(value):
        if len(value) > 0:
            return True
        return False


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.get_min())  # // return -3
minStack.pop()
print(minStack.top())    # // return 0
print(minStack.get_min())  # // return -2


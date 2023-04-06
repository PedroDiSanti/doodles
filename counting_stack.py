class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counting = 0

    def get_counter(self):
        return self.__counting

    def pop(self):
        self.__counting += 1


if __name__ == '__main__':
    stack = CountingStack()
    for i in range(100):
        stack.push(i)
        stack.pop()
    print(stack.get_counter())

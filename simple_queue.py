# A queue is a data model characterized by the term FIFO (First In – First Out).
# FIFO is easily exemplify as a line. The first person that enters the line is the first person that leaves the line.
# So, the first item that is appended in the list is the first item that is popped out of the list.

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, val):
        self.__queue.append(val)

    def get(self):
        return self.__queue.pop(0)

    def show(self):
        print(f'{self.__queue}')


if __name__ == '__main__':
    queue = Queue()

    queue.put(1)
    queue.put("dog")
    queue.put(False)

    queue.show()

    try:
        for i in range(4):
            print(queue.get())
    except Exception as queue_error:
        print(f'Error: {queue_error}')

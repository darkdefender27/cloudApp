__author__ = 'shubham'


class Empty(Exception):
    pass


class ArrayStack:
    """
        LIFO Implementation.
    """

    def __init__(self):
        self._data = []
        # Current number of elements in Stack
        self._cur = 0

    def __len__(self):
        #return len(self._data)
        return self._cur

    def is_empty(self):
        return self._cur == 0

    def push(self, e):
        self._data.append(e)
        self._cur += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        self._cur -= 1
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def _min(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        min_element = self._data[0]
        for i in self._data:
            if i < min_element:
                min_element = i
        return min_element
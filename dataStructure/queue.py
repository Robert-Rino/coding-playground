from collections import deque


class Queue(object):

    def __init__(self):
        self.data = deque()

    def inqueue(self, value):
        self.data.appendleft(value)

    def dequeue(self):
        self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


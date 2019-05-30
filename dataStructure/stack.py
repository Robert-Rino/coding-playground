class Stack(object):

    def __init__(self):
        self.data = []
        self.max =[]

    def push(self, val):
        self.data.append(val)
        if len(self.max) == 0:
            self.max.append(val)
        else:
            self.max.append(max(self.max[-1], val))

    def pop(self):
        self.max.pop()
        return self.data.pop()

    def maximun(self):
        return self.max[-1]

    def minimun(self):
        pass
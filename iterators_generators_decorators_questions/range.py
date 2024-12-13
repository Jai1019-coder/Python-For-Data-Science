class range:
    def __init__(self, start, stop = 0):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<= self.stop-1:
            raise ValueError
        else:
            current_value = self.start
            self.start-=1
            return current_value
for i in range(5,0):
    print(i)
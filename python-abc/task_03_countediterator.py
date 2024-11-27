class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        r = next(self.iterator)
        self.count += 1
        return r
    
    def get_count(self):
        return self.count
    
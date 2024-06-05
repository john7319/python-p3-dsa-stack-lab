class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0 

    def push(self, item):
        if self.size() >= self.limit:
            return False 
        self.items.append(item)
        return True 

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1

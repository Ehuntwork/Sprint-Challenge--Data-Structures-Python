
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = []
        self.oldest_node = 0

    def append(self, item):
        if len(self.value) >= self.capacity:
            if self.oldest_node == self.capacity:
                self.oldest_node = 0
            self.value.pop(self.oldest_node)
            self.value.insert(self.oldest_node, item)
            self.oldest_node +=1
        else:
            self.value.append(item)

    def get(self):
        return self.value
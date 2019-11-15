class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # Check buffer capacity, if at capacity, reset self current
        if self.current is self.capacity:
            self.current = 0

        # Increment current amount of items in buffer
        self.current += 1
        # Replace item in current buffer position
        self.storage[self.current - 1] = item

    def get(self):
        items = []

        for i in self.storage:
            if i is not None:
                items.append(i)

        return items


buffer2 = RingBuffer(5)
for i in range(50):
    buffer2.append(i)
    print(buffer2.get())

print("last", buffer2.get())

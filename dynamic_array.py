# a dynamic array class
class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    # insert


    # append
    def append(self, value):
        # check count exceeding capacity
        if self.count >= self.capacity:
            # TODO: Make array dynamic with resizing
            print("ERROR: Array is full")
            return
        # add value to storage at index
        self.storage[self.count] = value
        # increment count
        self.count += 1


    # resize (private) __resize__()
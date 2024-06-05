class DynamicArray:
    # known as resizeable array
    # initilaize array
    # O(n) because allocating that much memory, n = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        # even if you we do not populate the array
        self.size = 0

# constant time complexity, O(1)
    def get(self, i: int) -> int:
        return self.arr[i]

# constant time complexity, O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
# size increase becasue adding to length of array
# doubling capacity, so calling instructor again
# O(n), with resize have loop, how often will resize execute
# in worst cae O(n), but average case will be O(1)
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
# soft delete, just changed size, didtn actually delete the value
# O(1)
    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]
 
# need to copy all values from old array to new array
# need to set the self.arr to new array
# that is syntax for making an array of certain length
# O(n), always, but won't run often, bc of size or capacity
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
# O(1)
    def getSize(self) -> int:
        return self.size
        
# O(1)
    def getCapacity(self) -> int:
        return self.capacity

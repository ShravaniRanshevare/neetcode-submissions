class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None]*capacity
        self.capacity=capacity
        self.count=0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if ( self.count == self.capacity):
            self.resize()
        self.array[self.count]=n
        self.count +=1

    def popback(self) -> int:
        self.count -=1
        elem= self.array[self.count]
        self.array.pop()
        return elem

    def resize(self) -> None:
        self.capacity *=2
        new = [None]*self.capacity
        for i in range(self.count):
            new[i] = self.array[i]
        self.array=new

    def getSize(self) -> int:
        return self.count
    
    def getCapacity(self) -> int:
        return self.capacity

class MyCircularQueue:

    def __init__(self, k: int):
        self.ring = [None]*k #first is the last 
        self.tail=0
        self.size=k
        self.num=0
        self.head = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.ring[self.tail] = value 
        self.tail = (self.tail + 1) % self.size
        self.num = self.num+1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head += 1
        self.head %= self.size
        self.num -=1
        return True


    def Front(self) -> int:
        if self.num == 0:
            return -1
        front = self.ring[self.head]
        return front

    def Rear(self) -> int:
        if self.num == 0:
            return -1
        return self.ring[(self.tail - 1 % self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.num == 0

    def isFull(self) -> bool:
        if self.num == self.size:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
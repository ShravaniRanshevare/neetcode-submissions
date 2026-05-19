class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        index = len(self.arr)//2
        if len(self.arr)%2 != 0:
            median =  self.arr[index]
        else:
            median = (self.arr[index-1]+self.arr[index])/2
            
        return float(median)
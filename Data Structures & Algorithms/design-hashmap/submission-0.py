class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for t in self.hashmap:
            if t[0]==key:
                self.remove(key)
                break
        
        self.hashmap.append((key,value))
    def get(self, key: int) -> int:
        for t in self.hashmap:
            if t[0]==key:
                return t[1]
        return -1

    def remove(self, key: int) -> None:
        for t in self.hashmap:
            if t[0]==key:
                self.hashmap.remove((t[0],t[1]))
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
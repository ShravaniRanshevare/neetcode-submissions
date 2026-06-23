from collections import defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.cache= dict()
        self.capacity = capacity
        self.count = 0
        self.freq = dict()
        self.least = []
        self.timestamps=defaultdict(list)
        self.time = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.freq[key] += 1
            self.time += 1
            self.timestamps[key] = self.time
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache:
            if self.count == self.capacity:
                min_freq = min(self.freq.values())
                self.least = [k for k,v in self.freq.items() if v == min_freq]
                if len(self.least) > 1:
                    # pick LRU among candidates
                    remove = min(self.least, key=lambda k: self.timestamps[k])
                else:
                    remove = self.least[0]
                del self.cache[remove]
                del self.freq[remove]
                del self.timestamps[remove]
                self.count -=1
            self.cache[key] = value
            self.freq[key] = 1
            self.count += 1
        else:
            self.cache[key] = value
            self.freq[key] += 1
        self.time += 1
        self.timestamps[key]= self.time

        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
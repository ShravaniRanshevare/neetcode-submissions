from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap=defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key][timestamp]= value
        else:
            self.timeMap[key].update({timestamp: value})
        

    def get(self, key: str, timestamp: int) -> str:
        res = list(self.timeMap.get(key,{}).items())
        main = [i for i in res if i[0]<= timestamp]
        if not main:
            return ""
        if len(main)==1:
            return main[0][1]
        if len(main)>1:
            key,value=max(main,key=lambda x: x[0])
            return value
        

        
        

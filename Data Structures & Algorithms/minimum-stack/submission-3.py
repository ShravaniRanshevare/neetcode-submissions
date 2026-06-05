class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini= "#"

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == "#" :
            self.mini = val
        elif self.mini >= val:
            self.mini = val
        
    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.mini:
            self.mini="#"
            if self.stack:
                mini=self.stack[0]
                for elem in self.stack[1:]:
                    if elem<mini:
                        mini = elem
                self.mini = mini
  
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
        

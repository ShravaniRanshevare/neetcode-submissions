class CountSquares:

    def __init__(self):
        self.data=dict()


    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.data[p] = self.data.get(p, 0) + 1

    def count(self, point: List[int]) -> int:
        # i did this all on my own
        px, py = point
        total = 0
        
        for (x, y) in self.data:
            if (x, y) != (px,py):
                freq = self.data[(x,y)]
                # vertical partner
                if x == px and y != py:
                    side = abs(y - py)
                    r1 = (px + side, py)
                    r2 = (px + side, y)
                    r3 = (px - side, py)
                    r4 = (px - side, y)
                    if r1 in self.data and r2 in self.data:
                        total += freq * self.data[r1] * self.data[r2]
                    if r3 in self.data and r4 in self.data:
                        total += freq * self.data[r3] * self.data[r4]
                
        return total
        
            

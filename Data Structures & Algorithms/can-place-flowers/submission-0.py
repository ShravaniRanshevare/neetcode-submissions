class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 1 if flowerbed[0] == 0 else 0
        for cell in flowerbed:
            if cell == 1:
                n -= int((empty-1)/2)
                empty = 0
            else:
                empty += 1
        n -= empty//2
        return n<=0
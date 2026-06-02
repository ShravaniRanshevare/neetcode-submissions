from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        hand.sort()
        for h in hand:
            while count[h]>0:
                for i in range(groupSize):
                    next_card= h + i
                    if count[next_card]<=0:
                        return False
                    count[next_card] -= 1
                    
        return True



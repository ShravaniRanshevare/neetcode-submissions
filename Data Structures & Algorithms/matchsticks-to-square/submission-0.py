class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #imp square has all equal sides so u choose the max ad thtas gotta be ur side measure for all
        #so i said we need a dict to keep track of and they said  4 groups 
        matchsticks.sort(reverse=True) #bigger sticks if fail we find out soon
        total_length = sum(matchsticks)
        if total_length%4 != 0:
            return False
        sides = [0]*4
        length = total_length // 4 #max a side can be litreally my maxlength inshort perimeter
        def dfs(i):
            if i == len(matchsticks):
                return True
            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= matchsticks[i]
                if sides[side] == 0:
                    break
            return False
        return dfs(0)


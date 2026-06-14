class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[]
        #two tricks they did not tell u the pairing sorting based on position
        #two car can form fleet when time of prev is >= time of curr
        #only with cars ahead tho 
        for i in range(len(position)):
            res.append([position[i],speed[i]])
        stack=[]
        res.sort(reverse=True,key= lambda s: s[0])
        time = (target-res[0][0])/res[0][1]
        stack.append(time)
        for i in range(1,len(res)):
            time = (target- res[i][0])/res[i][1]
            if stack[-1] < time:
                stack.append(time)
        return len(stack)
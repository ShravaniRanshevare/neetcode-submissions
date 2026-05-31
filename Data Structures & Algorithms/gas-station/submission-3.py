class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #i think we can have a bool recursive cz we just need to return index
        #the next station from last index == 0 as its a circuit
        #index conditions and whats the break point ? visited set?
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        
        for i in range(n):
            tank += gas[i] - cost[i]
            # If tank drops below 0, reset start to next station
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if start < n else -1
        
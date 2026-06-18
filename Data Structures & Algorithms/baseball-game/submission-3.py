class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        #not a variable stack bcz in alot of the ones u need the record at each stage
        for n in operations:
            if n == "+":
                prev1,prev2 = record[-1],record[-2]
                record.append(prev1+prev2)
            elif n == "C":
                record.pop()
            elif n == "D":
                record.append(record[-1]*2)
            elif -30000<=int(n)<=30000:
                n = int(n)
                record.append(n)
            print(record)
                
        
        return sum(record)
            
        
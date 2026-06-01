class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            temp=num2
            num2=num1
            num1=temp
        array=[]
        #i think the process is u multiply num1 with each digit no zeroes as single digit multiplication but long run ke liye padding
        #helper function
        def helper(num1,num,zeroes):
            res= int(num1)*num 
            res = res * (10**zeroes)
            return res

        count = 0
        for num in num2[::-1]:
            #number of 0s for ex for first it its 0  
            res = helper(num1,int(num),count)
            array.append(res)
            count += 1
        final=0
        for v in array:
            final += v
        final = str(final)
        return final 
        
        



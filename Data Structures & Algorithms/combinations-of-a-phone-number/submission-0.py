class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #for every 3 ka elem permuation with all of 4 ke elems
        if digits == "":
            return []
        hashmap = {
            "2": ["a","b","c"],
            "3" : ["d","e","f"],
            "4": ["g","h","i"],
            "5" : ["j","k","l"],
            "6": ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8": ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        
        sub=""
        res=[]
        def backtrack(i,sub):
            if len(sub) == len(digits):
                res.append(sub)
                return
            for n in hashmap[digits[i]]:
                backtrack(i+1,sub+n) #litreally what i did for each of first ones go thru second ones

        
        backtrack(0,sub)
        return res 

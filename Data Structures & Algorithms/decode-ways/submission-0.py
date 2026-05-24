class Solution:
    def numDecodings(self, s: str) -> int:
        num_to_letter = {
        "1": "A", "2": "B", "3": "C", "4": "D", "5": "E",
         "6": "F", "7": "G", "8": "H", "9": "I", "10": "J",
        "11": "K", "12": "L", "13": "M", "14": "N", "15": "O",
        "16": "P", "17": "Q", "18": "R", "19": "S", "20": "T",
        "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y",
        "26": "Z"
        }
        memo=dict()
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            res = dp(i+1) 
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dp(i+2)
            
            memo[i] = res
            return res
        return dp(0)
            
            
            


        
            


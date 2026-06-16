class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        first = strs[0]
        for i in range(len(first)):
            for word in strs[1:]:
                if i>=len(word) or first[i] != word[i]:
                    return prefix
            prefix += first[i]
        return prefix 
                    
                
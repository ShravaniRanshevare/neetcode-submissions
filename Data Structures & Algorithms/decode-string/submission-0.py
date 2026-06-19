class Solution:
    def decodeString(self, s: str) -> str:
        
        #maybe u iterate thru the string and till u dont encounter a ] u keep on adding in the stack?
        #def recurse(st):
            #if st[0] == "]":
                #return 
            #elif st[0] == "[":
                #return st[1]+recurse(st[2:])
            #elif "1"<= st[0] "300":
                #n = int(st[0])
                #return n*(recurse(st[1:]))

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)
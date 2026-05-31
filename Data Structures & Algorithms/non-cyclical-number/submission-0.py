class Solution:
    def isHappy(self, n: int) -> bool:
        def recurse(n,processed):
            if n in processed:
                return False
            num = str(n)
            val=0
            for nu in num:
                val += int(nu)**2
            processed.add(n)
            if val == 1:
                return True
            else:
                return recurse(val,processed)
        return recurse(n,processed=set())
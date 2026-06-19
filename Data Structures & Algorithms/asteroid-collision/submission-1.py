class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #suppose u maintain a stack to keep track
        #ok only add to stack if no preve elem, or collision condition satisfied
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
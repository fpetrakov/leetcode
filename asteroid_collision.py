class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for curr in asteroids:
            while stack and curr < 0 and stack[-1] >= 0:
                diff = curr + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    curr = 0
                else:
                    curr = 0
                    stack.pop()
            if curr != 0:
                stack.append(curr)
        return stack


sol = Solution()
res = sol.asteroidCollision([10, 2, -5])
print(res)

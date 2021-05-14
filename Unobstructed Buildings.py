class Solution:
    def solve(self, heights):
        stack = []
        for idx, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(idx)
        return stack
ob=Solution()
print(ob.solve([1, 5, 5, 2, 3]))
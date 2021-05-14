class Solution:
    def solve(self, nums):
        s=set(nums)
        return len(s)
ob=Solution()
print(ob.solve([2, 2, 2, 3, 4, 6, 6]))
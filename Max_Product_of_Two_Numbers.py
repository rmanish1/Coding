class Solution:
    def solve(self, nums):
        nums.sort()
        sum1=nums[0]*nums[1]
        sum2=nums[-1]*nums[-2]
        if sum1>sum2:
            return sum1
        else:
            return sum2
ob=Solution()
print(ob.solve([5, 1, 7]))
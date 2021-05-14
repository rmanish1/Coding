class Solution:
    def solve(self, num):
        sum=0
        while num>0:
            sum=sum+num%10
            num=num//10
        return sum
ob=Solution()
print(ob.solve(123))
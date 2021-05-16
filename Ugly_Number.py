class Solution:
    def solve(self, n):
        if n==1:
            return True
        if n<=0:
            return False
        if n%2==0:
            return self.solve(n//2)
        if n%3==0:
            return self.solve(n//3)
        if n%5==0:
            return self.solve(n//5)
        return False
ob=Solution()
print(ob.solve(10))

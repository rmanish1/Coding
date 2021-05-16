class Solution:
    def solve(self, n):
        lst=list()
        while True:
            if n==1:
                lst.append(n)
                break
            elif n%2==0:
                lst.append(n)
                n=n/2
            else:
                lst.append(n)
                n=3*n+1
        return len(lst)
ob=Solution()
print(ob.solve(11))

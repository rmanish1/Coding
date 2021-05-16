class Solution:
    def Sum_dig(self,m):
        x=0
        while m>0:
            x=x+(m%10)**2
            m=m//10
        return x

    def solve(self,a):
        lst=list()
        s=0
        while True:
            if a==1:
                break
            if lst.count(a)>1:
                break
            s=self.Sum_dig(a)
            lst.append(s)
            a=s
        if a==1:
            return True
        else:
            return False
ob=Solution()
print(ob.solve(7))

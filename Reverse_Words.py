class Solution:
    def solve(self, sentence):
        lst=sentence.split()
        lst.reverse()
        sen=""
        for i in lst:
            sen+=i+" "
        return sen.rstrip()
ob=Solution()
print(ob.solve())

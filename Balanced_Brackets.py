class Solution:
    def solve(self, s):
        count = 0
        for i in s:
            if i == "(":
                count+=1
            if i == ")":
                count-=1
                if count < 0:
                    return False
        return count == 0
ob=Soultion()
print(ob.solve("()()"))

class Solution:
    def solve(self, s):
        temp = "0"
        Sum = 0
        for ch in s:
            if (ch.isdigit()):
                temp += ch
            else:
                Sum += int(temp)
                temp = "0"
        return Sum + int(temp)
ob=Solution()
print(ob.solve("11aa32bbb5"))
class Solution:
    def solve(self,s):
        chars = list(s)
        prev = None
        k = 0
        for c in s:
            if prev != c:
                chars[k] = c
                prev = c
                k = k + 1
        return ''.join(chars[:k])
ob=Solution()
print(ob.solve("aaaaaabbbccccaaaaddf"))
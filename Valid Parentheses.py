def solve(s):
    count = 0
    for i in s:
        if i == "(" or i == "[" or i == "{":
            count+=1
        if i == ")" or i == "]" or i == "}":
            count-=1
            if count < 0:
                return False
    return count == 0

inp = input("Enter a String of Parentheses:\n>>> ")
print(solve(inp))
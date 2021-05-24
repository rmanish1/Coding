def long_sub(s):
    count = 0
    max_count = 0
    prev = set()
    for i in range(len(s)):
        if s[i] not in prev:
            prev.add(s[i])
            count += 1
        else:
            prev.clear()
            count = 0
        max_count = max(max_count, count)
    return max_count

inp = input("Enter a String:\n>>> ")
print(long_sub(inp))
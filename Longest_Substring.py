def long_sub(s):
    count = 0
    max_count = 0
    prev = set()
    for char in s:
        if char not in prev:
            prev.add(char)
            count += 1
        else:
            prev = set()
            count = 1
        max_count = max(max_count, count)
    return max_count

print(long_sub("abcabcbb"))
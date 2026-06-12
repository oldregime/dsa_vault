s = "abcabcbba"

l = 0
res = 0

for r in range(len(s)):
    while s[r] in s[l:r]:
        l += 1
    length = r - l + 1
    if length > res:
        res = length

print(res)

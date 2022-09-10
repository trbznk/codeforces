s = input()
l, u = 0, 0
for c in s:
    if c.isupper():
        u += 1
    elif c.islower():
        l += 1

if u > l:
    print(s.upper())
else:
    print(s.lower())

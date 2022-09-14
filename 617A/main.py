x = int(input())
p = 0
steps = 0
while p != x:
    diff = x-p
    if diff <= 5:
        p += diff
    else:
        p += 5
    steps += 1
print(steps)

n = int(input())

caps = [0]
for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    caps.append(caps[-1]-a+b)

print(max(caps))

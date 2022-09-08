from math import log, floor

a, b = input().split()
a, b = int(a), int(b)

x = log(b/a)/log(3/2)
x = floor(x+1)
print(x)

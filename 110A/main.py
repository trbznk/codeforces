n = input()
l = [4, 7]
n = [c for c in n if int(c) in l]
if len(n) in l:
    print("YES")
else:
    print("NO")

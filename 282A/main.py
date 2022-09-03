n = int(input())
x = 0

for _ in range(n):
    cmd = input()
    if cmd == "X++" or cmd == "++X":
        x += 1
    elif cmd == "X--" or cmd == "--X":
        x -= 1

print(x)


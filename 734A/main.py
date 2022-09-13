n = int(input())
games = input()
a, d = 0, 0
for game in games:
    if game == "A":
        a += 1
    elif game == "D":
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")

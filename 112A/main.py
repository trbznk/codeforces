left = input()
right = input()

for lc, rc in zip(left, right):
    lc, rc = lc.lower(), rc.lower()
    if lc > rc:
        print(1)
        exit(0)
    elif lc < rc:
        print(-1)
        exit(0)

print(0)


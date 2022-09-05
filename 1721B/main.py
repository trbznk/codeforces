t = int(input())


def distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


for _ in range(t):
    s = input()
    n, m, sx, sy, d = s.split()
    n, m, sx, sy, d = int(n), int(m), int(sx), int(sy), int(d)
    steps = n+m-2
    
    top = True if distance(sx, sy, sx, m) <= d else False
    right = True if distance(sx, sy, n, sy) <= d else False
    bottom = True if distance(sx, sy, sx, 1) <= d else False
    left = True if distance(sx, sy, 1, sy) <= d else False

    if distance(sx, sy, n, m) <= d: # laser touches goal
        print(-1)
    elif (not left and not top) or (not bottom and not right): # laser touches edges
        print(steps)
    else:
        print(-1)

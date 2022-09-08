n = int(input())
stones = input()
stack = []

for stone in stones:
    if len(stack) > 0:
        last_stone = stack[-1]
        if stone != last_stone:
            stack.append(stone)
    else:
        stack.append(stone)

print(len(stones)-len(stack))

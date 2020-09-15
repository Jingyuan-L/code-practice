import sys
pos = list(map(int, input().strip().split()))
actions = input().strip()
for act in actions:
    if act == 'U':
        pos[1] += 1
    elif act == 'D':
        pos[1] -= 1
    elif act == 'L':
        pos[0] -= 1
    elif act == 'R':
        pos[0] += 1
sys.stdout.write(" ".join(map(str, pos)))
def next_step(c_pos, c_dir, lr):
    if lr == 'L':
        if c_dir == 'N':
            return (c_pos[0] - 1, c_pos[1]), 'W'
        elif c_dir == 'E':
            return (c_pos[0], c_pos[1] - 1), 'N'
        elif c_dir == 'S':
            return (c_pos[0] + 1, c_pos[1]), 'E'
        else:
            return (c_pos[0], c_pos[1] + 1), 'S'
    else:
        if c_dir == 'N':
            return (c_pos[0] + 1, c_pos[1]), 'E'
        elif c_dir == 'E':
            return (c_pos[0], c_pos[1] + 1), 'S'
        elif c_dir == 'S':
            return (c_pos[0] - 1, c_pos[1]), 'W'
        else:
            return (c_pos[0], c_pos[1] - 1), 'N'


inp = open("../input.txt").read().split(', ')

curr_pos = (0,0)
pos_cache = set()
pos_cache.add(curr_pos)
curr_dir = 'N'
p2 = []
for i in inp:
    if 'L' in i:
        steps = int(i.split('L')[1])
        curr_lr = 'L'
    else:
        steps = int(i.split('R')[1])
        curr_lr = 'R'
    next_dir = curr_dir
    for s in range(steps):
        curr_pos, next_dir = next_step(curr_pos, curr_dir, curr_lr)
        if curr_pos in pos_cache:
            p2.append(abs(curr_pos[0]) + abs(curr_pos[1]))
        pos_cache.add(curr_pos)
    curr_dir = next_dir
p1 = abs(curr_pos[0]) + abs(curr_pos[1])

print(p1)
print(p2[0])

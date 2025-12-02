from collections import deque
inp = open("../input.txt").read().splitlines()

q_list = deque(range(100))

q_list.rotate(50)
p1 = 0
p2 = 0
for inst in inp:
    before = q_list[0]
    if 'R' in inst:
        step = int(inst.split('R')[1])
        q_list.rotate(-1*step)
    else:
        step = int(inst.split('L')[1])
        q_list.rotate(step)
    zero_rotations = step // len(q_list)
    after = q_list[0]
    p2 += zero_rotations
    if after == 0:
        p1 += 1
    if after == 0 or 'R' in inst and after < before != 0 or 'L' in inst and after > before != 0:
        p2 += 1

print(p1)
print(p2)

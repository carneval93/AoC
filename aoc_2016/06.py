from collections import defaultdict

inp = open("../input.txt").read().splitlines()

p1 = []
p2 = []
for i in range(len(inp[0])):
    c = defaultdict(int)
    for l in inp:
        c[l[i]] += 1
    p1.append(sorted(c.items(), key=lambda x: x[1], reverse=True)[0][0])
    p2.append(sorted(c.items(), key=lambda x: x[1])[0][0])

print(''.join(p1))
print(''.join(p2))

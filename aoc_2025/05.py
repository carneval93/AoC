inp = open("../input.txt").read().split('\n\n')

ranges = inp[0].splitlines()
ingreds = list(map(int, inp[1].splitlines()))

curr_ranges = set()
for r in ranges:
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    curr_ranges.add((start, end))

p1 = 0
for ing in ingreds:
    found = False
    for start, end in curr_ranges:
        if start <= ing <= end:
            found = True
            break
    if found:
        p1 += 1

while True:
    new_ranges = set()
    for start, end in curr_ranges:
        found = False
        for cmp_start, cmp_end in curr_ranges:
            if (start,end) == (cmp_start, cmp_end):
                continue
            if (start <= cmp_start <= end) or (cmp_start <= start <= cmp_end):
                new_ranges.add((min(start, cmp_start), max(end, cmp_end)))
                found = True
        if not found:
            new_ranges.add((start, end))
    if new_ranges == curr_ranges:
        curr_ranges = new_ranges
        break
    curr_ranges = new_ranges

p2 = 0
for s, e in curr_ranges:
    p2 += e - s + 1
print(p1)
print(p2)




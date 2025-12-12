import textwrap
inp = open("../input.txt").read().split(',')

p1 = 0
p2 = 0
for i in inp:
    for num_range in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
        num_range_str = str(num_range)
        pat_len = len(num_range_str)
        for pat_len in range(1,len(num_range_str)):
            split_pat = textwrap.wrap(num_range_str, pat_len)
            if split_pat.count(split_pat[0]) == len(split_pat):
                if len(split_pat) == 2:
                    p1 += num_range
                p2 += num_range
                break
print(p1)
print(p2)
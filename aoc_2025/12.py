inp = open("../input.txt").read().split('\n\n')

presents_dict = {}
presents = inp[:-1]
for p in presents:
    presents_dict[int(p.split(':')[0])] = p.split(':')[1].split('\n')[1:]
grid_list = inp[-1].split('\n')

result = 0
for g in grid_list:
    dimension = g.split(': ')[0].split('x')
    col_dim = int(dimension[0])
    row_dim = int(dimension[1])
    presents_to_fit = []
    index = 0
    for present in g.split(': ')[1].split(' '):
        times = int(present)
        presents_to_fit.append((presents_dict[index], times))
        index += 1

    grid_num = col_dim * row_dim
    present_num = 0
    for pr in presents_to_fit:
        pr_present_num = 0
        for pr_row in pr[0]:
            pr_present_num += pr_row.count('#')
        present_num += pr_present_num * pr[1]
    # skip if all presents cannot fit, just tried without turning and flipping and worked :)
    if grid_num < present_num:
        continue

    result += 1

print(result)


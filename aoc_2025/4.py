def get_neighbours(node, curr_dict):
    neighbours = 0
    for next_pos in [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (1,0), (-1, 0), (0, -1)]:
        if curr_dict.get((node[0] + next_pos[0],node[1] + next_pos[1]), ".") == "@":
            neighbours += 1
    return neighbours


inp = open("../input.txt").read().splitlines()

current_grid = {}
row_num = 0
for row in inp:
    col_num = 0
    for col in row:
        current_grid[(row_num, col_num)] = col
        col_num += 1
    row_num += 1

p1 = 0
p2 = 0

rnd = 0
while True:
    rnd += 1
    new_grid = {}
    for k, v in current_grid.items():
        if get_neighbours(k, current_grid) >= 4:
            new_grid[k] = v
        else:
            new_grid[k] = '.'
            if current_grid[k] == '@':
                p2 += 1
                if rnd == 1:
                    p1 += 1
    if current_grid == new_grid:
        break
    current_grid = new_grid
print(p1)
print(p2)

def get_all_neighbours(node):
    neighbours = []
    next_node = (node[0] + 1, node[1])
    if next_node not in current_grid:
        return []
    if current_grid[next_node] == '^':
        adjacent_node = (node[0] + 1, node[1] - 1)
        if adjacent_node in current_grid:
            neighbours.append(adjacent_node)
        adjacent_node = (node[0] + 1, node[1] + 1)
        if adjacent_node in current_grid:
            neighbours.append(adjacent_node)
    else:
        neighbours.append(next_node)
    return neighbours


def depth_search(start_node):
    if start_node in cache:
        return cache[start_node]
    new_v_nodes = 0
    if start_node[0] == len(inp)-1:
        return 1
    for adjacent in get_all_neighbours(start_node):
        cnt = depth_search(adjacent)
        new_v_nodes += cnt
    cache[start_node] = new_v_nodes
    return new_v_nodes


inp = open("../input.txt").read().splitlines()

current_grid = {}
start = ()
cache = {}
row_num = 0
for row in inp:
    col_num = 0
    for col in row:
        if col == 'S':
            start = (row_num, col_num)
        current_grid[(row_num, col_num)] = col
        col_num += 1
    row_num += 1

beams = [start]
result = []
print(depth_search(start))

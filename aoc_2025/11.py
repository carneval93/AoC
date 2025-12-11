from collections import defaultdict

inp = open("../input.txt").read().splitlines()

connections = defaultdict(list)
for i in inp:
    connections[i.split(': ')[0]] = i.split(': ')[1].split(' ')


def get_all_neighbours(node):
    return connections[node]


def depth_search(start_node, end_node):
    key = (start_node, end_node)
    if key in cache:
        return cache[key]
    if start_node == end_node:
        return 1
    new_v_nodes = 0
    for adjacent in get_all_neighbours(start_node):
        cnt = depth_search(adjacent, end_node)
        new_v_nodes += cnt
    cache[key] = new_v_nodes
    return new_v_nodes


cache = {}
print(depth_search('you', 'out'))
print(depth_search('svr', 'fft') * depth_search('fft', 'dac') * depth_search('dac', 'out'))

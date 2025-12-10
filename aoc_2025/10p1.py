import heapq
inp = open("../input.txt").read().splitlines()


def get_neighbours(l, button_list):
    new_l = []
    for but in button_list:
        if isinstance(but, int):
            if l[but] == '.':
                new_l.append((l[:but] + '#' + l[but+1:], 1))
            else:
                new_l.append((l[:but] + '.' + l[but + 1:], 1))
        else:
            new_w = l
            for num in but:
                if new_w[num] == '.':
                    new_w = new_w[:num] + '#' + new_w[num + 1:]
                else:
                    new_w = new_w[:num] + '.' + new_w[num + 1:]
            new_l.append((new_w, 1))

    return new_l


def dijkstra(start_node, end_node, btns):
    visited = {}
    queue = []
    heapq.heappush(queue, (start_node, 0))
    while end_node not in visited.keys():
        queue.sort(key=lambda x: x[1])
        node_to_check, node_cost = heapq.heappop(queue)
        for neighbour in get_neighbours(node_to_check, btns):
            if neighbour[0] in visited.keys() and (neighbour[1] + node_cost) >= visited[neighbour[0]]:
                continue
            visited[neighbour[0]] = (neighbour[1] + node_cost)
            heapq.heappush(queue, (neighbour[0], node_cost + neighbour[1]))
    return visited[end_node]


result = []

for i in inp:
    lights_goal = i.split('[')[1].split(']')[0]
    curr_lights = len(lights_goal) * '.'
    buttons = list(map(eval, i.split('] ')[1].split(' {')[0].split(' ')))
    res = dijkstra(curr_lights, lights_goal, buttons)
    result.append(res)

print(sum(result))


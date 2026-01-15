def get_metadata_entries_p1(node_list):
    node_cnt = node_list[0]
    curr_metadata_cnt = node_list[1]
    curr_metadata_entries = 0
    curr_index = 2
    if node_cnt != 0:
        for i in range(node_cnt):
            new_metadata_entries, new_index = get_metadata_entries_p1(node_list[curr_index:])
            curr_metadata_entries += new_metadata_entries
            curr_index += new_index
    for m in range(curr_metadata_cnt):
        curr_metadata_entries += node_list[curr_index]
        curr_index += 1
    return curr_metadata_entries, curr_index


def get_metadata_entries_p2(node_list):
    node_cnt = node_list[0]
    curr_metadata_cnt = node_list[1]
    curr_metadata_value = 0
    curr_index = 2
    if node_cnt == 0:
        for m in range(curr_metadata_cnt):
            curr_metadata_value += node_list[curr_index]
            curr_index += 1
        return curr_metadata_value, curr_index
    curr_metadata_node_vals = []
    for i in range(node_cnt):
        new_metadata_entries, new_index = get_metadata_entries_p2(node_list[curr_index:])
        curr_metadata_node_vals.append(new_metadata_entries)
        curr_index += new_index
    for m in range(curr_metadata_cnt):
        curr_metadata_entry = node_list[curr_index] - 1
        if len(curr_metadata_node_vals) > curr_metadata_entry:
            curr_metadata_value += curr_metadata_node_vals[curr_metadata_entry]
        curr_index += 1
    return curr_metadata_value, curr_index


inp = list(map(int, open("../input.txt").read().split(' ')))
print(get_metadata_entries_p1(inp)[0])
print(get_metadata_entries_p2(inp)[0])

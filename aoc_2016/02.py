def get_code_from_grid(instr_set, gr):
    curr_pos = (1, 1)
    code = ''
    for line in instr_set:
        for instr in line:
            if instr == 'U':
                next_pos = (curr_pos[0], curr_pos[1] - 1)
                if next_pos in gr:
                    curr_pos = next_pos
            elif instr == 'D':
                next_pos = (curr_pos[0], curr_pos[1] + 1)
                if next_pos in gr:
                    curr_pos = next_pos
            elif instr == 'R':
                next_pos = (curr_pos[0] + 1, curr_pos[1])
                if next_pos in gr:
                    curr_pos = next_pos
            elif instr == 'L':
                next_pos = (curr_pos[0] - 1, curr_pos[1])
                if next_pos in gr:
                    curr_pos = next_pos
        code += str(gr[curr_pos])
    return code


inp = open("../input.txt").read().splitlines()

grid_p1 = {(0,0): 1, (1,0): 2, (2,0): 3, (0,1): 4, (1,1): 5, (2,1): 6, (0,2): 7, (1,2): 8, (2,2): 9}
grid_p2 = {(0,0): 2, (1,0): 3, (2,0): 4, (0,1): 6, (1,1): 7, (2,1): 8, (0,2): 'A', (1,2): 'B', (2,2): 'C', (-1,1): 5, (1,-1): 1, (3,1): 9, (1,3): 'D'}

print(get_code_from_grid(inp, grid_p1))
print(get_code_from_grid(inp, grid_p2))

inp = open("../input.txt").read().splitlines()

current_grid = {}
start = ()
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
while beams:
    new_beams = []
    for b in beams:
        b_row = b[0]
        b_col = b[1]
        while b_row < len(inp)-1:
            b_row += 1
            if current_grid[(b_row,b_col)] == '^':
                if (b_row, b_col + 1) not in new_beams and (b_row, b_col + 1) in current_grid:
                    new_beams.append((b_row, b_col + 1))
                if (b_row, b_col - 1) not in new_beams and (b_row, b_col + 1) in current_grid:
                    new_beams.append((b_row, b_col - 1))
                result.append((b_row,b_col))
                print((b_row,b_col))
                break
    beams = new_beams
print(len(set(result)))
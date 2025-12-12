import math
inp = open("../input.txt").read().splitlines()

operations = []
for line in inp:
    split_line = line
    for i in reversed(range(1,10)):
        split_line = split_line.replace(i*' ', ',')
    if split_line[0] == ',':
        split_line = split_line[1:]
    operations.append(split_line.split(','))

p1 = 0
for j in range(len(operations[0])):
    col_values = []
    for n in operations:
        col_values.append(n[j])
    op_code = col_values[-1]
    numbers = list(map(int,col_values[:-1]))
    if op_code == '+':
        p1 += sum(numbers)
    elif op_code == '*':
        p1 += math.prod(numbers)

p2 = 0
j = len((max(inp, key=len))) - 1
tmp_col_values = []
tmp_op_code = ''
while j >= 0:
    col_values = ''
    for n in inp:
        if j < len(n) and n[j] != ' ':
            if n[j] == '+':
                tmp_op_code = '+'
            elif n[j] == '*':
                tmp_op_code = '*'
            else:
                col_values += (n[j])
    if col_values:
        tmp_col_values.append(col_values)
    else:
        numbers = list(map(int, tmp_col_values))
        if tmp_op_code == '+':
            p2 += sum(numbers)
        elif tmp_op_code == '*':
            p2 += math.prod(numbers)
        tmp_col_values = []
    j -= 1

numbers = list(map(int, tmp_col_values))
if tmp_op_code == '+':
    p2 += sum(numbers)
elif tmp_op_code == '*':
    p2 += math.prod(numbers)

print(p1)
print(p2)

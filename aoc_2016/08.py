inp = open("../input.txt").read().splitlines()

width = 50
height = 6
lit_pixels = set()
for line in inp:
    source = set()
    target = set()
    if 'rect' in line:
        row_num = int(line.split(' ')[1].split('x')[1])
        column_num = int(line.split(' ')[1].split('x')[0])
        for y in range(column_num):
            for x in range(row_num):
                lit_pixels.add((x, y))
    elif 'column' in line:
        which_column = int(line.split('x=')[1].split(' by ')[0])
        by_number = int(line.split('x=')[1].split(' by ')[1])
        for col_values in sorted([t for t in lit_pixels if t[1] == which_column], key=lambda t: t[0], reverse=True):
            source.add(col_values)
            target.add(((col_values[0] + by_number) % height, col_values[1]))
            lit_pixels.add(((col_values[0] + by_number) % height, col_values[1]))
    elif 'row' in line:
        which_row = int(line.split('y=')[1].split(' by ')[0])
        by_number = int(line.split('y=')[1].split(' by ')[1])
        for row_values in sorted([t for t in lit_pixels if t[0] == which_row], key=lambda t: t[1], reverse=True):
            source.add(row_values)
            target.add((row_values[0], (row_values[1] + by_number) % width))
            lit_pixels.add((row_values[0], (row_values[1] + by_number) % width))
    for s in source:
        if s not in target:
            lit_pixels.remove(s)

print(len(lit_pixels))
for row in range(height):
    row_string = ''
    for col in range(width):
        if (row, col) in lit_pixels:
            row_string += '#'
        else:
            row_string += ' '
    print(row_string)

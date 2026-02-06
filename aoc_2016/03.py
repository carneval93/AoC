def check_if_triangle(triangle_sides):
    first = triangle_sides[0]
    second = triangle_sides[1]
    third = triangle_sides[2]
    if first + second <= third or second + third <= first or first + third <= second:
        return False
    return True


inp = open("../input.txt").read().splitlines()

p1 = 0
p2 = 0
numbers_list = []
for i in inp:
    sides = i.split(' ')
    sides = list(map(int, list(filter(None, sides))))
    numbers_list.append(sides)

for normal in numbers_list:
    if check_if_triangle(normal):
        p1 += 1

inverted = list(map(list, zip(*numbers_list)))
for inv in inverted:
    list_of_groups = zip(*(iter(inv),) * 3)
    for l in list_of_groups:
        if check_if_triangle(l):
            p2 += 1

print(p1)
print(p2)

from shapely import Polygon, box
inp = open("../input.txt").read().splitlines()

recs = []
for i in inp:
    recs.append((int(i.split(',')[0]), int(i.split(',')[1])))

polygon = Polygon(recs)

max_area = []

possible_nodes = set()
visited = set()

for rec_row, rec_col in recs:
    for n_rec_row, n_rec_col in recs:
        if (rec_row, rec_col) == (n_rec_row, n_rec_col):
            continue
        if ((n_rec_row, n_rec_col), (rec_row, rec_col)) in visited:
            continue
        visited.add(((rec_row, rec_col),(n_rec_row, n_rec_col)))
        corners = ((rec_row, rec_col), (rec_row, n_rec_col), (n_rec_row, rec_col), (n_rec_row, n_rec_col))
        min_row = (min([x[0] for x in corners]))
        max_row = (max([x[0] for x in corners]))
        min_col = (min([x[1] for x in corners]))
        max_col = (max([x[1] for x in corners]))

        if polygon.contains(box(min_row, min_col, max_row, max_col)):
            low_corner = (min_row, min_col)
            up_corner = (max_row, max_col)
            max_area.append((abs(low_corner[0] - up_corner[0]) + 1) * (abs(low_corner[1] - up_corner[1]) + 1))

print(max(max_area))
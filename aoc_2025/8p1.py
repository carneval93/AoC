def get_pythagoras_result(Xv, Yv, Zv, Xc, Yc, Zc):
    return (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) + (Zv - Zc) * (Zv - Zc)


inp = open("../input.txt").read().splitlines()

curr_boxes = set()
for i in inp:
    x = int(i.split(',')[0])
    y = int(i.split(',')[1])
    z = int(i.split(',')[2])
    curr_boxes.add((x,y,z))

base_boxes = curr_boxes.copy()
packages = set()

processed = set()

distance_list = []
distance_keys = set()

for x_ref, y_ref, z_ref in base_boxes:
    for x_next, y_next, z_next in base_boxes:
        if (x_ref, y_ref, z_ref) == (x_next, y_next, z_next) or ((x_ref, y_ref, z_ref),(x_next, y_next, z_next)) in distance_keys or ((x_next, y_next, z_next), (x_ref, y_ref, z_ref)) in distance_keys:
            continue
        distance = get_pythagoras_result(x_next, y_next, z_next, x_ref, y_ref, z_ref)
        distance_list.append((((x_ref, y_ref, z_ref), (x_next, y_next, z_next)),distance))
        distance_keys.add(((x_ref, y_ref, z_ref), (x_next, y_next, z_next)))

distance_list = sorted(
    distance_list,
    key=lambda x: x[1]
)

cnt = 0
while cnt < 1000:
    ind = 0

    closest = distance_list[cnt][0]

    cnt += 1
    new_packages = set()
    found = set()
    for p in packages:
        if closest[0] in p or closest[1] in p:
            for p_sub in p:
                found.add(p_sub)
        else:
            new_packages.add(p)
    if not found:
        new_packages.add(closest)
    else:
        found.add(closest[0])
        found.add(closest[1])
        new_packages.add(tuple(found))
    packages = new_packages.copy()

result = 1
sorted_package = sorted(list(packages), key=len, reverse=True)
for sp in sorted_package[:3]:
    result *= len(sp)
print(result)

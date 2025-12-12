inp = open("../input.txt").read().splitlines()

recs = set()
for i in inp:
    recs.add((int(i.split(',')[0]), int(i.split(',')[1])))


max_rec = 0
for rec_row, rec_col in recs:
    for n_rec_row, n_rec_col in recs:
        if (abs(rec_row - n_rec_row) + 1) * (abs(rec_col - n_rec_col)+1) > max_rec:
            max_rec = (abs(rec_row - n_rec_row) + 1) * (abs(rec_col - n_rec_col)+1)

print(max_rec)
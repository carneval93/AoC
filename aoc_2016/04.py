inp = open("../input.txt").read().splitlines()

p1 = 0
p2 = 0
for i in inp:
    word = ''.join(i.split('-')[:-1])
    id = int(i.split('-')[-1].split('[')[0])
    lit = i.split('-')[-1].split('[')[1].split(']')[0]
    curr_found = ''
    for cnt in reversed(range(len(word))):
        times = [char for char in set(word) if word.count(char) == cnt]
        if not times:
            continue
        curr_found += ''.join(sorted(times))
        if lit in curr_found:
            p1 += id
            break
    new_word = ''
    for w in word:
        new_word += chr((ord(w) - ord('a') + id) % 26 + ord('a'))
    if new_word == 'northpoleobjectstorage':
        p2 = id

print(p1)
print(p2)

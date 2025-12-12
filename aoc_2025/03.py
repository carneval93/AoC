def get_result(curr_result, word, max_len):
    if len(curr_result) == max_len:
        return curr_result
    for next_max in reversed(sorted(list(set(word)))):
        index = word.index(next_max)
        new_result = curr_result + next_max
        new_word = word[index + 1:]
        ret = get_result(new_result, new_word, max_len)
        if ret:
            return ret
    return ''


inp = open("../input.txt").read().splitlines()
p1 = 0
p2 = 0
for i in inp:
    p1 += int(get_result('', i, 2))
    p2 += int(get_result('', i, 12))

print(p1)
print(p2)

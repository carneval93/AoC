inp = open("../input.txt").read().splitlines()

result = 0
for i in inp:
    state = 'outside'
    inside_cnt = 0
    outside_cnt = 0
    word = list(i)
    while word:
        c = word.pop(0)
        if c == '[':
            state = 'inside'
        elif c == ']':
            state = 'outside'
        else:
            if state == 'inside':
                if len(word) >= 3 and c == word[2] and word[0] == word[1] and len(set([c] + word[0:3])) == 2:
                    inside_cnt += 1
            if state == 'outside':
                if len(word) >= 3 and c == word[2] and word[0] == word[1] and len(set([c] + word[0:3])) == 2:
                    outside_cnt += 1
    if inside_cnt == 0 and outside_cnt > 0:
        result += 1
print(result)
inp = open("../input.txt").read().splitlines()

result = 0
for i in inp:
    state = 'outside'
    outside_list = []
    inside_list = []
    word = list(i)
    while word:
        c = word.pop(0)
        if c == '[':
            state = 'inside'
        elif c == ']':
            state = 'outside'
        else:
            if state == 'outside':
                if len(word) >= 2 and c == word[1] and word[0] != word[1]:
                    outside_list.append(c + word[0] + c)
            if state == 'inside':
                if len(word) >= 2 and c == word[1] and word[0] != word[1]:
                    inside_list.append(word[0] + c + word[0])
    if any(x in inside_list for x in outside_list):
        result += 1
print(result)

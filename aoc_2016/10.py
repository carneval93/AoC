from collections import defaultdict

inp = open("../input.txt").read().splitlines()
p1 = 0
current_chips = defaultdict(list)
instructions = dict()
for i in inp:
    if 'value' in i:
        value = int(i.split('value ')[1].split(' ')[0])
        bot_nr = i.split('to ')[1]
        current_chips[bot_nr].append(value)
    else:
        bot_nr = i.split(' gives')[0]
        low = i.split('low to ')[1].split(' and')[0]
        high = i.split('high to ')[1].split(' and')[0]
        instructions[bot_nr] = [low, high]

while True:
    new_chips = current_chips.copy()
    for i in inp:
        if 'value' in i:
            continue
        bot_nr = i.split(' gives')[0]
        if len(new_chips[bot_nr]) == 2:
            if sorted(new_chips[bot_nr]) == [17,61]:
                p1 = bot_nr
            low_coin, high_coin = sorted(new_chips[bot_nr])
            low_bot, high_bot = instructions[bot_nr]
            new_chips[low_bot].append(low_coin)
            new_chips[high_bot].append(high_coin)
            new_chips[bot_nr] = []
    if new_chips == current_chips:
        break
    current_chips = new_chips.copy()

print(p1)
print(current_chips['output 0'][0] * current_chips['output 1'][0] * current_chips['output 2'][0])

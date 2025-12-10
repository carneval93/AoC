from z3 import *

inp = open("../input.txt").read().splitlines()


solver = Solver()
result = 0
for i in inp:
    solver = Optimize()
    A = Int('A')
    joltage_goal = tuple(map(int, i.split('{')[1].split('}')[0].split(',')))
    buttons = list(map(eval, i.split('] ')[1].split(' {')[0].split(' ')))
    button_variables = []
    for b_num in range(len(buttons)):
        num_button = Int(f'numButton{b_num}')
        button_variables.append(num_button)
        solver.add((num_button >= 0))

    j_num = 0
    for j in joltage_goal:
        relevant_buttons = []
        b_index = 0
        for b in buttons:
            if isinstance(b, int):
                if b == j_num:
                    relevant_buttons.append(button_variables[b_index])
            else:
                if j_num in b:
                    relevant_buttons.append(button_variables[b_index])
            b_index += 1

        solver.add((sum(relevant_buttons) == j))
        j_num += 1
    solver.add((sum(button_variables) == A))
    solver.minimize(A)
    if solver.check() == sat:
        model = solver.model()
        sum_button_num = 0
        for m in button_variables:
            sum_button_num += int(str(model.eval(m)))
        result += sum_button_num
    else:
        print("No solution")

print(result)











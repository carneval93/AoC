
def get_length(wrd):
    tmp_wrd = wrd
    len_output_p1 = 0
    len_output_p2 = 0
    marker = False
    while tmp_wrd:
        if marker:
            marker = False
            marker_string = tmp_wrd.split(')')[0]
            marker_length = int(marker_string.split('x')[0])
            marker_times = int(marker_string.split('x')[1])
            len_output_p1 += marker_length * marker_times
            len_output_p2 += get_length(tmp_wrd.split(')', 1)[1][:marker_length])[1] * marker_times
            tmp_wrd = tmp_wrd.split(')', 1)[1][marker_length:]
        else:
            ch = tmp_wrd[0]
            if ch == '(':
                marker = True
            else:
                len_output_p1 += 1
                len_output_p2 += 1
            tmp_wrd = tmp_wrd[1:]
    return len_output_p1, len_output_p2

inp = open("../input.txt").read()

print(get_length(inp))


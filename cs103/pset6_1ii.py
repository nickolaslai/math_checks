import re
#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters = 'yd'
    combos = [i + j + k + l for i in letters for j in letters for k in letters for l in letters]
    output = open('1iv.txt', 'w');
    for c in combos:
        my_sum = 0
        is_valid = true
        for letter in c:
            if my_sum * my_sum > 4:
                is_valid = false
                break
            elif letter == 'y':
                my_sum += 1
            elif letter == 'd':
                my_sum -= 1

        if is_valid:
            output.write(c + 'A' + '\n')
        else:
            output.write(c + 'R' + '\n')

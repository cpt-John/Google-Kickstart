list_pw =list()
for each in range (-1,10000):list_pw.append(int(2**each))
list_pw = tuple(list_pw)


def claculate(T):
    T = tuple(sorted(T))
    length = len(T)
    total = 0
    for index, each in enumerate(T):
        i = 0
        in_indx = index+i
        while (in_indx) < length :
            total += (T[in_indx]-each)*(list_pw[i])   #2**(i-1)
            i += 1
            in_indx = index+i
    return total


handle = open('A-small-practice.in')

line_inx = 1
output_s = ''
for line in handle:
    if len(line.split()) == 1:continue
    in_list = [int(ele) for ele in line.split()]
    ans = claculate(in_list)
    ans = ans % 1000000007
    output_s += f'Case #{line_inx}: {ans}\n'
    print(f'\nCase #{line_inx}: {ans}\n')
    line_inx += 1

handle.close()
out_file = open('output_large.txt', 'w')
out_file.write(output_s)
out_file.close()

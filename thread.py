# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re

rate = {
}


def read_files(filename):
    f = open(filename)
    return ''.join(f.readlines())


def extract_block(lines: str):
    lines = lines.split('argc=7')
    lines.pop(0)
    for line in lines:
        dataset = re.findall('argv\[2\]=.*', line)[0].split('/')[8].replace(' ', '').replace('sec', '')
        ga = re.findall('dynamic g_inf advanced: .*', line)[0].split(',')
        gai = ga[0].split('=')[1].replace('sec', '')
        gac = ga[1].split('=')[1].replace('sec', '')
        gat = ga[2].split('=')[1].replace('sec', '')
        # print(ga)
        # print(gai, gac, gat)


        gn = re.findall('dynamic g_inf naive: .*', line)[0].split(',')
        gni = gn[0].split('=')[1].replace('sec', '')
        gnc = gn[1].split('=')[1].replace('sec', '')
        gnt = gn[2].split('=')[1].replace('sec', '')
        # print(gn)
        # print(gni, gnc, gnt)
        thread = re.findall('num_thread=.*', line)[0].split(',')[0].split('=')[1]

        if dataset not in rate:
            rate[dataset] = {
                '1': [],
                '8': [],
                '16': [],
                '24': [],
                '32': []
            }
        if thread not in rate[dataset]:
            continue

        rate[dataset][thread].append((gni, gnc, gnt, gai, gac, gat))

    # print(rate)
    for key in rate:
        print(key)

        print('t=,1,8,16,24,32')
        print('g_inf_naive_inf,', ','.join(rate[key][k][0][0] for k in rate[key]))
        print('g_inf_naive_count,', ','.join(rate[key][k][0][1] for k in rate[key]))
        print('g_inf_naive_total,', ','.join(rate[key][k][0][2] for k in rate[key]))
        print('g_inf_advanced_inf,', ','.join(rate[key][k][0][3] for k in rate[key]))
        print('g_inf_advanced_count,', ','.join(rate[key][k][0][4] for k in rate[key]))
        print('g_inf_advanced_total,', ','.join(rate[key][k][0][5] for k in rate[key]))

        print()
        print()
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lines = read_files('result-2021-4-15-vary-t.txt')
    extract_block(lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

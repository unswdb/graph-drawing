# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

rate = {
    'dbpedia': {
        '0.0001': [],
        '0.001': [],
        '0.005': [],
        '0.01': [],
        '0.02': []
    },

    'twitter': {
        '0.0001': [],
        '0.001': [],
        '0.005': [],
        '0.01': [],
        '0.02': []
    }
}

def read_files(filename):
    f = open(filename)
    return ''.join(f.readlines())


def extract_block(lines: str):
    lines = lines.split('argc=7')
    lines.pop(0)
    for line in lines:
        dataset = re.findall('argv\[2\]=.*', line)[0].split('/')[8].replace(' ', '').replace('sec', '')
        ga = re.findall('dynamic g_inf advanced: .*', line)[0].split(',')[2].split('=')[1].replace(' ', '').replace('sec', '')
        gn = re.findall('dynamic g_inf naive: .*', line)[0].split(',')[2].split('=')[1].replace(' ', '').replace('sec', '')
        ARB = re.findall('.*cnt_tmp=.*', line)[0].split(',')[2].split('=')[1].replace(' ', '').replace('sec', '')
        nr = re.findall('dynamic g_inf advanced: .*', line)[0].split(',')[3].split('=')[1].replace(' ', '').replace('sec', '')
        rt = re.findall('sampling rate:.*', line)[0].split(',')[0].split(':')[1].replace(' ', '').replace('sec', '')

        if dataset not in rate:
            rate[dataset] = {
                '0.0001': [],
                '0.001': [],
                '0.005': [],
                '0.01': [],
                '0.02': []
            }
        if rt not in rate[dataset]:
            continue

        rate[dataset][rt].append((ARB, gn, ga, nr))

    for key in rate:
        print(key)
        nrs = [i[3] for i in rate[key][r][0]]
        for r in rate[key]:
            print(r)
            nrs = [i[3] for i in rate[key][r][0]]
            print(",".join(nrs))
            # print(",".join([j for j in i] for i in rate[key][r]))
            # for i in rate[key][r]:
            #     for j in i:
            #         print(j)
            print()
        print()
        print()
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lines = read_files('result-2021-4-12.txt') + read_files('result-2021-4-14.txt')
    extract_block(lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

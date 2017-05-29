from collections import Counter
import re

def solution():
    ret_list = Counter()
    with open('Les_Miserables-Victor_Hugo.txt', 'r') as f:
        data = re.sub(r'\.|\?|!|-|/|,|:|;|"|\(|\)|[0-9]', ' ', f.read())
        data = [raw_word.strip("'").upper() for raw_word in data.split()]
    for word in data:
        ret_list[word] += 1
    del ret_list['']
    ret_list = Counter(ret_list).most_common()
    return ret_list

if __name__ == '__main__':
    solution_list = solution()
    for each in solution_list:
        print(each)

'''
과제 설명
디렉토리를 입력 받아, 그 디렉토리를 기준으로 모든 하위 디렉토리에 있는 txt파일을 찾아 출력하시오.
조건
1. 채점은 리눅스 컴퓨터에서 이루어집니다.
2. 아래의 코드는 예시이며, 아래의 코드를 수정은 자유이나, solution 함수는 반드시 있어야 하며, solution 함수의 전달 되는 정보와 반환형을 수정하시면 안됩니다.
3. txt파일은 절대경로로 출력이 되어야 합니다.
4. os.walk 함수를 사용시 0점 처리 됩니다.
'''
import os, queue

def get_subdir( path, ret_list ) :
    subdir_list = []
    try :
        dir_files = os.listdir(path)
    except :
        return subdir_list
    for each in dir_files :
        full_name = path + '/' + each
        if os.path.isdir(full_name) :
            subdir_list.append(full_name + '/')
        elif full_name[-4:] == ".txt":
            ret_list.append(full_name)
    return subdir_list

def solution( v ) :
    ret_list = []
    dir_queue = queue.Queue()
    dir_queue.put(v)
    while not dir_queue.empty() :
        dir_path = dir_queue.get()
        subdir_path = get_subdir(dir_path, ret_list)
        for each in subdir_path :
            dir_queue.put(each)
    ret_list.sort()
    return ret_list
if __name__ == '__main__' :
    v = input()
    output = solution(v)
    print(output)
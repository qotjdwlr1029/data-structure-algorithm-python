from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0                  # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1         # 검색 범위 맨 뒤 원소의 인덱스

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스

        print('   |', end='')
        if a[pc] == key:
            return pc       # 검색 성공
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1
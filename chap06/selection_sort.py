# 단순 선택 정렬 알고리즘 구현하기

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> int:
    """단순 선택 정렬"""
    exchang = 0
    n = len(a)
    print(f'길이 : {n}')
    for i in range(n-1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
        exchang += 1

    return exchang

if __name__ == '__main__':
    cnt = int(input('배열의 요소수를 입력하세요 : '))

    a = [None] * cnt
    for i in range(cnt):
        a[i] = int(input(f'a[{i}] : '))
    
    exch = selection_sort(a)
    for i in range(cnt):
        print(f'{a[i]:3}', end='')
    print(exch)
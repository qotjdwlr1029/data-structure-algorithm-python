# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a의 값을 입력하세요 '))
b = int(input('정수 b의 값을 입력하세요 '))

if a > b:
    b , a = a , b

sum = 0

for i in range(a, b+1):
    if i < b:
        print(f'{i}+',end='')
    elif i == b:
        print(f'{i}',end='')
    sum = sum + i

print(f'={sum}')
# a부터 b까지 정수의 합 구하기

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a의 합을 입력하세요 : '))
b = int(input('정수 b의 합을 입력하세요 : '))

if a > b:
    b, a = a, b

sum = 0

for i in range(a,b):
    print(f'{i} + ',end='')
    sum = sum + i

for i in range(b,b+1):
    print(f'{i} = ', end='')
    sum = sum + i

print(f'{sum}')
# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('정수 n을 입력하세요 : '))

for i in range(1 , n+1):
    if i % 2:
        print('+',end='')
    else:
        print('-',end='')

print()

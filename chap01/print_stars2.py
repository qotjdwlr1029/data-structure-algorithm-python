# *를 n개 출력하되 w개마다 줄바꿈하기

print('*를 출력합니다.')
n = int(input('몇 개를 출력하시겠습니까?'))
w = int(input('몇 개마다 줄바꿈하시겠습니까?'))

for _ in range( n // w ):
    print('*' * w)

rest = n % w
print('*' * rest)
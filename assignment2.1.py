import random

n=random.randint(1,100)

while True:
    a=int(input('숫자를 입력하세요: '))
    if a>n:
        print('DOWN')
    elif a<n:
        print('UP')
    else:
        print('RIGHT')
        break
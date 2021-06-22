from typing import MutableSequence

def partition(a:MutableSequence) -> None:
    #배열을 분활하여 출력
    n=len(a)
    p1=0  # 왼쪽 커서
    pr=n-1 # 오른쪽 커서
    x=a[n//2] # 피벗(가운데 원소)

    while p1<=pr:
        while a[p1]<x:p1+=1
        while a[pr]>x:pr-=1
        if p1<=pr:
            a[p1],a[pr]=a[pr],a[p1]
            p1+=1
            pr-=1

    print(f'피벗은 {x}입니다')

    print('피벗 이하인 그룹입니다')
    print(*a[0 : p1]) # a[0] ~ a[pl - 1]

    if p1 >  pr+1:
        print('피벗과 일치하는그룹 입니다')
        print(*a[pr+1:p1]) # a[pr + 1] ~ a[pl - 1]

    print('피벗 이상인 그룹입니다')
    print(*a[pr+1:n]) # a[pr + 1] ~ a[n - 1]

if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)         # 배열 x를 나누어서 출력
    

    

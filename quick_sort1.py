from typing import MutableSequence

def qsort(a:MutableSequence, left: int, right: int) -> None:
    #a[left]~a[right]를 퀵으로 정렬
    n=len(a)
    p1=0  # 왼쪽 커서
    pr=n-1 # 오른쪽 커서
    x=a[(left+right)//2] # 피벗(가운데 원소)

    while p1<=pr:
        while a[p1]<x:p1+=1
        while a[pr]>x:pr-=1
        if p1<=pr:
            a[p1],a[pr]=a[pr],a[p1]
            p1+=1
            pr-=1

    if  left< pr:   qsort(a, left, pr)
    if p1< right: qsort(a, p1, right)

def quick_sort(a:MutableSequence)->None:
    #퀵정렬
    qsort(a, 0, len(a)-1)


if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

from typing import MutableSequence

def bubble_sort(a:MutableSequence)->None:
    #버불정렬
    n=len(a)
    for i in range(n-1):
        for j in range(n-1, i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]


if __name__=='__main__':
    print('버불정렬을 수행하세요')
    num=int(input('원소수를 입력하세요'))
    x=[None]*num#원소수가 num인 배열을 생성

    for i in range(num):
        x[i]=int(input(f'x[{i}] : '))

    bubble_sort(x)#배열 x를 버블정렬

    print('오름차순으로 정렬 하여습니다')
    for i in range(num):
        print(f'x[{i}]={x[i]}')
    

    
        


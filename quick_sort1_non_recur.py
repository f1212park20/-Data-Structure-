from stack import Stack  # 실습 4C-1의 파일 import
from typing import MutableSequence

def qsort(a:MutableSequence, left:int,  right:int)-> None:
    """a[left] ~ a [right]를 퀵 정렬(비재귀 버전)"""
    range=Stack(right-left+1) # 스택 생성

    range.push((left, right))#(맨앞 원소, 맨 끈원소),(0,8)

    while not range.is_empty():#스택이 비어 있지 않는 동안 작업을 반복
        p1.pr=left, right=range.pop() # 왼쪽, 오른쪽 커서를 꺼냄,(left, right)대입->p1:0,pr:8,p1:5,pr:8(a[5]~a[6],a[7]~a[8]그룹으로 분활)
        x=a[(left+right)//2] # 피벗(중앙 요소)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:                        # 실습 6-10, 실습 6-11과 같음
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 저장,(0,4),(5,6)
        if pl < right: range.push((pl, right))  # 오른쪽 그룹의 커서를 저장,(5,8),(7,8)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('비재귀적인 퀵 정렬')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')    
    

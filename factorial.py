def factorial(n:int)->int:
    #양의 정수 n개의 factorial재귀적으로 구함
    if n>0:
        #n에전달받은 값이 0보다 크면
        return n*factorial(n-1)
    else:
        return 1

if __name__=='__main__':
    n=int(input('출력한 팩토리얼 값을 입력하세요'))
    print(f'{n}의 팩 토리얼은 {factorial(n)}입니다 ')
    

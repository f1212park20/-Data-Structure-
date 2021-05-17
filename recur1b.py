from  stack import  Stack

def  recur(n:int)->int:
    #제귀를 제거한 recur() 함수
    s=Stack(n)

    while True:
        if n>0:
            s.push(n)#n값 푸시4
            n=n-1
            continue

        if not s.is_empty():# 스택이 비어있지 않으면
            n=s.pop()#저장한 값을 n에 pop
            print(n)
            n=n-2
            continue
        break

x=int(input('정수값을 입력하세요'))
recur(x)
            

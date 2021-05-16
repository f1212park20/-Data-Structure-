def recur(n:int)->int:
    #꼬리 재귀를 제거하는 함수
    while n>0:
        recur(n-1)
        print(n)
        n=n-2#n값을 2감소 시킨뒤 함수 시작 지점으로 돌아 간다

#main
x=int(input('정수값을 입력하세요'))
recur(x)


def move(no:int,  x:int, y:int)->None:
    if no > 1:
        move(no-1,x,6-x-y)#6-x-y.중간 기등 으로 이동
    print(x,y)
    if no > 1:
        move(no-1,6-x-y,y)#6-x-y.중간 기등 에서 3번째로 이동

#main
print('하노이 탑을 구현 하세요')
n=int(input())
print((2**n)-1)
move(n,1,3)#1기둥에 쌓인 원반 n개를 3개 기둥으로 옯김

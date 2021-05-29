pos=[0]*8
flag=[False]*8

def put() -> None:
    #각열에 배치한 퀀의 위치를 출력
    for i in range(8):
        print(f'{pos[i]:2}',end=' ')
    print()

def set(i:int)->None:
    #i열에 알맞은 워치에 퀀 배치
    for j in range(8):
        if not flag[j]:#j행에 퀀을 배치하지 않았으면
            pos[i]=j#퀀을 j행에 배치
            if i==7:
                put()
            else:
                flag[i]=True
                set(i+1)
                flag[i]=False
set(0)                

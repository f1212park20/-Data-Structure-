pos=[0]*8#각 열에서 퀀의 위치를 출력

def put()  -> None:
    #각 열에 배치한 퀀의 위치를 출력
    for i in range(8):
        print(f'{pos[i]:2}',end=' ')
    print()

def set(i: int)->None:
    #i열 퀀을 배치
    for j in range(8):
        pos[i]=j#퀀을 j행에 배치
        if i==7:#모든열에 퀀배치를 종료
            put()
        else:
            set(i+1)#다음 열에 퀸을 배치

set(0)#0열행에 퀀을 배치            
    
    
    







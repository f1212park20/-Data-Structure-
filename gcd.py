def gcd (x:int,  y:int)->int:
    #정수값 x와 y의 최대 공약수를 반환
    if y==0:
        return x
    else:
        return gcd(y,x%y)

if __name__=='__main__':
    print('두 정수값의 최대 공약수를 구합니다')
    x,y=map(int,  input().split())
    
    print(gcd(x,y))
    

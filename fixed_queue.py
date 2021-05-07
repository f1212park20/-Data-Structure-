from  typing import Any

class FixedQueue:
    class Empty(Exception):
        #비어있는  FixedQueue에서 디큐 또는 피크할때 내보내는 예외처리
        pass

    class Full(Exception):
        #가득차 있는 FixedQueue에서 인큐를 처리할때 내보내는 예외처리
        pass

    def __init__(self, capacity:int)->None:
        #큐 초기화
        self.no=0#현재 데이터 개수
        self.front=0#맨 앞 원소 커서
        self.rear=0#맨긑 원소 커서
        self.capacity=capacity#큐의 크기
        self.que=[None]*capacity#큐의 본체


    def  __len__(self) ->int:
        #큐에 있는 모든 데이터 개수를 반환
        return self.no

    def  is_empty(self)->bool:
        #큐가 비어 있는지를 판단
        return self.no<=0

    def  is_full(self)->bool:
        #큐가 가득차 있는지 판단
        return self.no>=self.capacity

    def  enque(self, x:Any) -> None:
        #데이터 x를 인큐
        if self. is_full():
            raise FixedQueue.Full#큐가 가득차있는 경우 예외 처리
        self.que[self.rear]=x
        self.rear+=1
        self.no+=1
        if self.rear==self.capacity:
            self.rear=0
            
    def deque(self)->Any:
        #데이터를 디큐
        if self.is_empty():
            raise FixedQueue.Full#큐가 가득차있는 경우 예외 처리
        x=self.que[self.front]
        self.front+=1
        self.no-=1
        if self.front==self.capacity:
            self.front=0;
        return x

    def peek(self) ->Any:
        #큐에서 데이터를 피크(맨앞에 있는 데이터를 들여다봄)
        if self.is_empty():
            raise FixedQueue.Full#큐가 비어 있는 경우 예외 처리
        return  self.que[self.front]


    def find(self, value:Any)->Any:
        #큐에서 value값을 찾아 인덱스를 반환(없으면 -1을 반환)
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            if self.que[idx]==value:#검색 성공
                return idx
        return -1#검색 실패

    def  count(self, value:Any)->bool:
        #큐에 있는 value의 개수를 반환
        c=0
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            if self.que[idx]==value:#검색 성공
                c+=1#들어있음
        return c

    def __contains__(self,  value: Any) -> bool:
        """큐에 value가 포함되어 있는지 판단합니다"""
        return self.count(value)


    def clear(self)->None:
        #큐의 모든 데이터 지움
        self.no=self.front=self.rear=0

    def dump(self) -> None:
        """모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다"""
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
        
            
        
 

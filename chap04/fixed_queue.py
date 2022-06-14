from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity : int) -> None:
        """큐 초기화"""
        self.no = 0                         # 현재 데이터 개수
        self.front = 0                      # 맨 앞 원소 커서
        self.rear = 0                       # 맨 뒤 원소 커서
        self.capacity = capacity            # 큐의 크기
        self.que = [None] * self.capacity   # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐가 비어있는지 판단"""
        return self.no <= 0

    def is_full(self) -> bool:
        """큐가 가득 차있는지 판단"""
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.front] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

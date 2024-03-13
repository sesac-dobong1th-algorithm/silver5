# 문제가 의도한 바가 이 que를 사용하는 방법이라 deque를 사용한 풀이방법이다.

from collections import deque

def last_card(N):
    # N장의 카드를 준비합니다. 각 카드는 1부터 N까지 번호가 매겨져 있습니다.
    cards = deque(range(1, N+1))
    
    # 카드가 한 장 남을 때까지 반복합니다.
    while len(cards) > 1:
        # 제일 위의 카드를 버립니다.
        cards.popleft()
        # 그 다음 카드를 제일 아래로 옮깁니다.
        cards.rotate(-1)

    # 마지막으로 남은 카드를 반환합니다.
    return cards.pop()

# 예제 실행
print(last_card(int(input())))
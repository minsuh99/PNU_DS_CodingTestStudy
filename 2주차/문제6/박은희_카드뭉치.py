# from collections import deque

# def solution(cards1, cards2, goal):
#     # 큐로 변환 
#     queue1 = deque(cards1)
#     queue2 = deque(cards2)
    
#     for i in goal:
#         if queue1[0] == i: 
#             queue1.popleft()  # cards1에서 제거
#         elif queue2[0] == i:
#             queue2.popleft()  # cards2에서 제거
#         else:
#             return "No"  #제거 안되면 no
    
#     return "Yes"  # 다 제거 되었으면 yes
#  인덱스 에러 


from collections import deque

def solution(cards1, cards2, goal):
    # 큐로 변환 
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    
    for i in goal:
        if queue1 and queue1[0] == i: # 큐원의 값이 있고 큐원의 첫번째가 목표문장과 같다면
            queue1.popleft()  # cards1에서 제거
        elif queue2 and queue2[0] == i:
            queue2.popleft()  # cards2에서 제거
        else:
            return "No"  #제거 안되면 no
    
    return "Yes"  # 다 제거 되었으면 yes
'''
card1 에 card2 값들이 사이사이 들어가면서 goal과 같으면 yes
아니면 no
근데 스택 큐 접근이 아닌거 같아서 다시 생각...

큐 스택 개념 다시 정리
1. 큐는 fifo 선입선출 파이프 모양!
enqueue, dequeue 따로 이루어짐
collections.deque list.pop(0)으로 해결

from collections import deque
queue = deque(["A", "B", "C"])  # 큐 생성
queue.popleft()  # "A" 제거
queue.append("D")  # "D" 추가
print(queue)  # deque(["B", "C", "D"])

2. 스택은 lifo 마지막에 넣은게 먼저 나감 병모양!
push, pop 같은 방향에서 이루어짐
list.append() list.pop()으로 해결
stack = []
stack.append("A")  # A 추가
stack.append("B")  # B 추가
stack.pop()  # B 제거
print(stack)  # ["A"]



문제로 돌아와서...
카드는 앞에서부터 확인하면서
goal 리스트의 단어 순서를 맞춰야함
for i in goal:
    card 1 단어 == goal 단어
    카드1 에서 그 단어 삭제
    card 2 단어 == goal 단어
    카드2 에서 그 단어 삭제
    
이걸 순차적으로 계속 돌면됨

모두 삭제면 yes
삭제 안된거 있으면 no



테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
테스트 25 〉	통과 (0.01ms, 10.1MB)

'''


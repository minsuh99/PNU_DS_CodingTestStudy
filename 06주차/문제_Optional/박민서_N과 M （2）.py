n, m = map(int, input().split())
def backtrack(start, my_list):
    if len(my_list) == m:
        print(" ".join(map(str, my_list)))
        return
    
    for i in range(start, n): # 중복 방지를 위해 (start, n)
        my_list.append(i + 1)
        backtrack(i + 1, my_list)
        my_list.pop()

backtrack(0, [])

'''
메모리: 32412 KB, 시간: 32 ms
'''

# itertools 이용
from itertools import combinations
n, m = map(int, input().split())
for comp in list(combinations(range(1, n + 1), m)):
    print(" ".join(map(str, comp)))
    
'''
메모리: 32412 KB, 시간: 32 ms
'''
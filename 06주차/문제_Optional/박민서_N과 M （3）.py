n, m = map(int, input().split())
def backtrack(start, my_list):
    if len(my_list) == m:
        print(" ".join(map(str, my_list)))
        return
    
    for i in range(n):
        my_list.append(i + 1)
        backtrack(i, my_list)
        my_list.pop()

backtrack(0, [])

'''
메모리: 32412 KB, 시간: 1124 ms
'''

# 검색해보니 product라는 것도 itertools에 있었음
from itertools import product
# product 데카르트 곱

n, m = map(int, input().split())
for comp in product(range(1, n+1), repeat = m):
    print(" ".join(map(str, comp)))
    
'''
메모리: 32412 KB, 시간: 1204 ms
'''
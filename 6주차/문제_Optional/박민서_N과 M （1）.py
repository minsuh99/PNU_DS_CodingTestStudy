# 문제 설명

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
    # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
    # 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
    # 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.


n, m = map(int, input().split())

def backtrack(start, my_list):
    if len(my_list) == m:
        my_list = [str(j) for j in my_list]
        print(" ".join(my_list))
        return
    
    for i in range(n):
        if i + 1 not in my_list:
            my_list.append(i + 1)
            backtrack(start + 1, my_list)
            my_list.pop()
    
backtrack(0, [])

'''
메모리: 32412 KB, 시간: 144 ms
'''

# from itertools import permutations 써도 될 듯

from itertools import permutations

n, m = map(int, input().split())
for comp in list(permutations(range(1, n + 1), m)):
    print(" ".join(map(str, comp)))
    
'''
메모리: 37528 KB, 시간: 96 ms
'''
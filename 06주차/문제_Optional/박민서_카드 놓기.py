n = int(input())
k = int(input())
my_list = []
res = set()
visited = [False for _ in range(n)]
for _ in range(n):
    my_list.append(int(input()))

def backtrack(comb_list):
    if len(comb_list) == k:
        temp = int("".join(map(str, comb_list[:])))
        res.add(temp)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            comb_list.append(my_list[i])
            backtrack(comb_list)
            comb_list.pop()
            visited[i] = False
backtrack([])
print(len(res))

'''
메모리: 32924 KB, 시간: 40 ms
'''
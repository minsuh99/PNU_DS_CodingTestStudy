x = int(input())
my_list = [int(i) for i in str(x)]
visited = [False for _ in range(len(my_list))]
res = 9999999

def backtrack(comb_list):
    global res
    if len(comb_list) == len(my_list):
        temp = int("".join(map(str, comb_list[:])))
        if temp > x:
            res = min(res, temp)
        return
    
    for i in range(len(my_list)):
        if not visited[i]: # 중복 없게끔
            visited[i] = True
            comb_list.append(my_list[i])
            backtrack(comb_list)
            comb_list.pop()
            visited[i] = False

backtrack([])

print(res if res != 9999999 else 0)


'''
메모리: 32412 KB, 시간: 32 ms
'''
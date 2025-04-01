from collections import deque
    
def solution(info, edges):
    tree = [[0,0] for _ in range(len(info))]
    for e in edges:
        if tree[e[0]][0]:
            tree[e[0]][1]=e[1]
        else:
            tree[e[0]][0]=e[1]
            
    def dfs(sheep, wolves, current, path):
        nonlocal max_sheep

        if info[current] == 0:
            sheep += 1
        else:
            wolves += 1

        if wolves >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        for node in path: # Path keeps track of currently accesible nodes
            for next_node in tree[node]: # Paths it can move to
                if next_node not in path: # no use going to an already visited one
                    dfs(sheep, wolves, next_node, path + [next_node])

    max_sheep = 0 # defined before dfs, and accesed as nonlocal
    dfs(0, 0, 0, [0])
    return max_sheep

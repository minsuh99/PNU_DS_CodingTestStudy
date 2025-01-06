directions={"U":(0,-1),"D":(0,1),"R":(1,0),"L":(-1,0)}

def solution(dirs):
    answer = 0
    grid=[[0]*11 for _ in range(0,11)]
    curx=5
    cury=5
    grid[5][5]=1
    answer=1
    prev=0
    for d in dirs:
        cords = directions[d]
        if(curx+cords[0]<0 or cury+cords[1]<0 or curx+cords[0]>10 or cury+cords[1]>100):
            continue
        curx+=cords[0]
        cury+=cords[1]
        if grid[curx][cury]==0:
            grid[curx][cury]=1
            answer+=1
            prev=0
        elif prev==0:
            answer+=1
            prev=1
        else:
            prev=1       
    
    return answer-1

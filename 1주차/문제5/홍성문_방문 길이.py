def solution(dirs):
    
    x, y = 0, 0
    visit = set()
    
    for i in dirs:
        x0, y0 = x, y
        
        if i == 'U':  
            y += 1
        elif i == 'D':  
            y -= 1
        elif i == 'R':  
            x += 1
        elif i == 'L':  
            x -= 1

        if x < -5 or x > 5 or y < -5 or y > 5:
            x, y = x0, y0
            continue

        # 경로 저장 (양방향으로 저장)
        path = ((x0, y0), (x, y))
        reverse_path = ((x, y), (x0, y0))
        visit.add(path)
        visit.add(reverse_path)

    # 지나간 길의 개수 반환 (양방향 저장이므로 2로 나눔)
    return len(visit) // 2

# 중복 경로 피하는건 GPT한테 물어봄..
#메모리: MB, 시간:  ms

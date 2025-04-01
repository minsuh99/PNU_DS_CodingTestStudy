def solution(dirs):
    answer = 0
    coor_list = []
    footprints = []
    
    cur_x = 0
    cur_y = 0
    next_x = 0
    next_y = 0
    
    for dir in dirs:
        cur_x = next_x
        cur_y = next_y
        if dir == 'U' and cur_y != 5:
            next_y += 1
        elif dir == 'D' and cur_y != -5:
            next_y -= 1
        elif dir == 'R' and cur_x != 5:
            next_x += 1
        elif dir == 'L' and cur_x != -5:
            next_x -= 1
        
        footprint = [(cur_x, cur_y), (next_x, next_y)]
        if len(list(set(footprint))) == 1:
            continue

        if footprint not in footprints and footprint[::-1] not in footprints:
            footprints.append(footprint)
    answer = len(footprints)
    return answer

# 메모리: 10.3 MB, 시간: 3.15 ms
# 시간 복잡도 O(N^2)예상

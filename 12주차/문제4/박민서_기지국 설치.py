# 처음 풀이
def solution(n, stations, w):
    answer = 0
    
    my_list = ['0' for _ in range(n)]
    
    for station in stations:
        station_idx = station - 1
        my_list[station_idx] = '1'
        for _w in range(1, w + 1):
            if station_idx + _w < len(my_list):
                my_list[station_idx + _w] = '1'
            if station_idx - _w < len(my_list):
                my_list[station_idx - _w] = '1'
    no_elec = "".join(my_list).split("1")
    no_elec_length = [len(zero) for zero in no_elec if len(zero) > 0]
    
    answer = sum([l // (2 * w + 1) if l % (2 * w + 1) == 0 else l // (2 * w + 1) + 1 for l in no_elec_length])
    return answer
# 전파 받을 수 있으면 1, 아니면 0으로,
# 1로 split 해주면 연속적인 0의 개수가 남으니 다 더하면 될거라 생각

'''
정확성  테스트
테스트 1 〉	실패 (0.01ms, 9.3MB)
테스트 2 〉	통과 (0.01ms, 9.29MB)
테스트 3 〉	통과 (0.01ms, 9.27MB)
테스트 4 〉	통과 (0.01ms, 9.17MB)
테스트 5 〉	통과 (0.01ms, 9.29MB)
테스트 6 〉	통과 (0.01ms, 9.17MB)
테스트 7 〉	통과 (0.01ms, 9.23MB)
테스트 8 〉	통과 (0.01ms, 9.31MB)
테스트 9 〉	통과 (0.01ms, 9.27MB)
테스트 10 〉	통과 (0.01ms, 9.27MB)
테스트 11 〉	통과 (0.01ms, 9.38MB)
테스트 12 〉	통과 (0.01ms, 9.3MB)
테스트 13 〉	통과 (0.01ms, 9.27MB)
테스트 14 〉	통과 (0.01ms, 9.28MB)
테스트 15 〉	통과 (0.01ms, 9.27MB)
테스트 16 〉	통과 (0.03ms, 9.26MB)
테스트 17 〉	통과 (0.03ms, 9.23MB)
테스트 18 〉	통과 (0.02ms, 9.27MB)
테스트 19 〉	통과 (0.03ms, 9.27MB)
테스트 20 〉	통과 (0.02ms, 9.26MB)
테스트 21 〉	통과 (0.08ms, 9.27MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
채점 결과
정확성: 67.1
효율성: 0.0
합계: 67.1 / 100.0
'''

# 다른 풀이
def solution(n, stations, w):
    answer = 0
    
    my_list = [0 for _ in range(n)]
    
    for station in stations:
        left = max(0, station - 1 - w)
        right = min(n - 1, station - 1 + w)
        for i in range(left, right + 1):
            my_list[i] = 1
    
    count_zero = 0
    for i in range(n):
        if my_list[i] == 0:
            count_zero += 1
        else:
            answer += count_zero // (2 * w + 1) if count_zero % (2 * w + 1) == 0 else count_zero // (2 * w + 1) + 1
            count_zero = 0
    if count_zero > 0:
        answer += count_zero // (2 * w + 1) if count_zero % (2 * w + 1) == 0 else count_zero // (2 * w + 1) + 1
    return answer
# 똑같이 전파 배열 만들어주고
# 앞에서부터 세면서 연속적인 0의 개수를 세고 전파 범위로 나누어 계산
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.18MB)
테스트 2 〉	통과 (0.01ms, 9.28MB)
테스트 3 〉	통과 (0.01ms, 9.08MB)
테스트 4 〉	통과 (0.01ms, 9.25MB)
테스트 5 〉	통과 (0.02ms, 9.19MB)
테스트 6 〉	통과 (0.01ms, 9.21MB)
테스트 7 〉	통과 (0.01ms, 9.28MB)
테스트 8 〉	통과 (0.01ms, 9.19MB)
테스트 9 〉	통과 (0.01ms, 9.11MB)
테스트 10 〉	통과 (0.01ms, 9.2MB)
테스트 11 〉	통과 (0.01ms, 9.2MB)
테스트 12 〉	통과 (0.01ms, 9.1MB)
테스트 13 〉	통과 (0.02ms, 9.28MB)
테스트 14 〉	통과 (0.01ms, 9.09MB)
테스트 15 〉	통과 (0.01ms, 9.24MB)
테스트 16 〉	통과 (0.03ms, 9.14MB)
테스트 17 〉	통과 (0.02ms, 9.08MB)
테스트 18 〉	통과 (0.02ms, 9.12MB)
테스트 19 〉	통과 (0.03ms, 9.13MB)
테스트 20 〉	통과 (0.02ms, 9.1MB)
테스트 21 〉	통과 (0.05ms, 9.22MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
채점 결과
정확성: 70.5
효율성: 0.0
합계: 70.5 / 100.0
'''


def solution(n, stations, w):
    answer = 0
    cur_idx = 0
    RANGE = 2 * w + 1
    for station in stations:
        left = max(0, station - 1 - w)
        right = min(n - 1, station - 1 + w)
        if cur_idx < left:
            no_elec = left - cur_idx
            answer += no_elec // RANGE if no_elec % RANGE == 0 else no_elec // RANGE + 1
        cur_idx = right + 1
    if cur_idx < n:
        no_elec = n - cur_idx
        answer += no_elec // RANGE if no_elec % RANGE == 0 else no_elec // RANGE + 1
    return answer

# 위의 작업들을 동시에 수행
# 기지국 위치가 오름차순으로 정렬되어 있으니
# 기지국 마다 전파 범위의 가장 왼쪽을 구하고,
# 현재 위치와 가장 왼쪽의 index의 차이가 연속적인 0의 개수로 계산할 수 있음
# 기지국 마다 계산하니 시간초과 해결

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.19MB)
테스트 2 〉	통과 (0.00ms, 9.24MB)
테스트 3 〉	통과 (0.00ms, 9.34MB)
테스트 4 〉	통과 (0.00ms, 9.21MB)
테스트 5 〉	통과 (0.01ms, 9.34MB)
테스트 6 〉	통과 (0.00ms, 9.26MB)
테스트 7 〉	통과 (0.00ms, 9.23MB)
테스트 8 〉	통과 (0.01ms, 9.2MB)
테스트 9 〉	통과 (0.00ms, 9.34MB)
테스트 10 〉	통과 (0.00ms, 9.27MB)
테스트 11 〉	통과 (0.00ms, 9.27MB)
테스트 12 〉	통과 (0.01ms, 9.27MB)
테스트 13 〉	통과 (0.01ms, 9.27MB)
테스트 14 〉	통과 (0.00ms, 9.26MB)
테스트 15 〉	통과 (0.00ms, 9.25MB)
테스트 16 〉	통과 (0.01ms, 9.23MB)
테스트 17 〉	통과 (0.01ms, 9.21MB)
테스트 18 〉	통과 (0.01ms, 9.34MB)
테스트 19 〉	통과 (0.01ms, 9.14MB)
테스트 20 〉	통과 (0.00ms, 9.2MB)
테스트 21 〉	통과 (0.02ms, 9.12MB)
효율성  테스트
테스트 1 〉	통과 (4.29ms, 9.53MB)
테스트 2 〉	통과 (4.44ms, 9.53MB)
테스트 3 〉	통과 (4.44ms, 9.61MB)
테스트 4 〉	통과 (4.43ms, 9.61MB)
채점 결과
정확성: 70.5
효율성: 29.5
합계: 100.0 / 100.0
'''
# def solution(progresses, speeds):
#     answer = []
#     # 각 작업이 완료될 날짜를 계산
#     end_days = [(100-p)//s +((100-p) % s>0) for p, s in zip(progresses, speeds)]
#     print(end_days)
#     max_end = end_days[0] # 7일
#     count = 0 # 배포 기능 개수
#     for d in end_days: # 7 3 9를 d가 돈다
#         if d <= max_end: # 7일보다 7일이 작거나 같으니
#             count +=1 # 카운트 추가 +1개 배포
#         else: # 7보다 작거나 같지 않은 경우를 만나면
#             answer.append(count)  # 리턴값에 그 카운트 값를 바로 추가함
#             max_end = d # 다음 3으로 넘어감
#     answer.append(count)
#     return answer


def solution(progresses, speeds):
    answer = []
    # 각 작업이 완료될 날짜를 계산
    end_days = [(100-p)//s +((100-p) % s>0) for p, s in zip(progresses, speeds)]
    print(end_days)
    max_end = end_days[0] # 7일
    count = 0 # 배포 기능 개수
    for d in end_days: # 7 3 9를 d가 돈다
        if d <= max_end: # 7일과 3일이 7일보다 작음
            count +=1 # 카운트 추가 +2개 배포
        else: # 7보다 작거나 같지 않은 9일을 만난다.
            answer.append(count)  # 리턴값에 앞서 계산한 카운트 값을 바로 추가함
            max_end = d # 원래 제일 먼저 7일이었는데 다음 최고 값인 9일로 넘어간다.
            count = 1 # 현재 보는 기능을 포함해서 개수를 센다. 뒤에 추가할 값이 없으니 0은 추가 안함 이부분 틀렸었음
    answer.append(count)
    return answer


'''
기능 개선
각 기능이 100 이되면 반영
개발 속도가 다름 뒷 기능이 앞기능보다 먼저 개발될 수 있음
- 이런 경우 앞기능 구현되면 배포
먼저 배포되어야하는 순서대로 작업 진도가 적힌 progresses
개발 속도가 적힌 speeds
배포일 마다 몇개의 기능이 있는지 return


1. 첫번째 기능이 얼마나 됐는지 확인, 얼마나 걸릴지 확인
2. 두번째 기능이 얼마나 됐는지 확인, 얼마나 걸릴지 확인
이거 반복
3. answer에 추가 될 값은 첫번째 기능 배포일 기준 뒤에 완료 될 배포 기능 개수 추가 근데 이거 찾으러 가다 완료 안되는 거 있음 멈추고 answer에 + 배포개수 

남은 기능 없으면 끝

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 9.96MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)


'''
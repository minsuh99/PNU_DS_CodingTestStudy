def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    
    repo_num_dict = {}
    res_dict = {}
    
    for i in id_list:
        repo_num_dict[i] = 0
        res_dict[i] = 0
        
    for rep in list(set(report)):
        _, reported = map(str, rep.split())
        repo_num_dict[reported] += 1
    
    
    ban_list = [name[0] for name in repo_num_dict.items() if name[1] >= k]

    # 처음 코드
    #  for i, uid in enumerate(id_list):
    #     if not ban_list:
    #         break
    #     else:
    #         for ban_id in ban_list:
    #             if " ".join([uid, ban_id]) in list(set(report)):
    #                 answer[i] += 1
    
    new_report = [repo.split() for repo in list(set(report))]
    
    for repo in new_report:
        if not ban_list:
            break
        else:
            if repo[1] in ban_list:
                answer[id_list.index(repo[0])] += 1
    return answer

# 처음 결과
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.19ms, 10MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (0.26ms, 10.1MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (32.90ms, 10.6MB)
테스트 7 〉	통과 (220.86ms, 10.6MB)
테스트 8 〉	통과 (968.16ms, 11MB)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	통과 (6572.82ms, 24.2MB)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (211.10ms, 10.4MB)
테스트 13 〉	통과 (15.56ms, 10.2MB)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	통과 (9.60ms, 10.3MB)
테스트 17 〉	통과 (7.76ms, 10.2MB)
테스트 18 〉	통과 (366.30ms, 10.3MB)
테스트 19 〉	통과 (711.90ms, 10.5MB)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	통과 (0.02ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 70.8
합계: 70.8 / 100.0
'''
# 이후 결과
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (2721.85ms, 89.6MB)
테스트 4 〉	통과 (0.09ms, 10.4MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (1.88ms, 10.6MB)
테스트 7 〉	통과 (3.58ms, 11MB)
테스트 8 〉	통과 (5.48ms, 11.4MB)
테스트 9 〉	통과 (656.60ms, 46.5MB)
테스트 10 〉	통과 (171.04ms, 46.5MB)
테스트 11 〉	통과 (1391.22ms, 89.4MB)
테스트 12 〉	통과 (0.87ms, 10.2MB)
테스트 13 〉	통과 (0.37ms, 10.4MB)
테스트 14 〉	통과 (845.72ms, 37.5MB)
테스트 15 〉	통과 (197.29ms, 55.3MB)
테스트 16 〉	통과 (0.34ms, 10.3MB)
테스트 17 〉	통과 (0.38ms, 10.3MB)
테스트 18 〉	통과 (1.40ms, 10.4MB)
테스트 19 〉	통과 (3.57ms, 10.3MB)
테스트 20 〉	통과 (731.81ms, 37.6MB)
테스트 21 〉	통과 (1286.37ms, 55.2MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.1MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
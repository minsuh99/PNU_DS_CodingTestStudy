def solution(genres, plays):
    answer = []
    genres_play_dict = {}
    
    for i, genre in enumerate(genres):
        if genre not in genres_play_dict:
            genres_play_dict[genre] = plays[i]
        else:
            genres_play_dict[genre] += plays[i]
    genres_play_dict = dict(sorted(genres_play_dict.items(), key = lambda x: -x[1])) 
    # 딕셔너리 정렬 검색,,
    
    for genre in list(genres_play_dict.keys()):
        idx_list = [g[0] for g in list(enumerate(genres)) if g[1] == genre]
        
        temp_plays = [play for play in list(enumerate(plays)) if play[0] in idx_list]
        temp_plays = sorted(temp_plays, key = lambda x: -x[1])
        final_idx = [i[0] for i in temp_plays[:2]]
        answer.extend(final_idx)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.21ms, 10.1MB)
테스트 6 〉	통과 (0.31ms, 10.1MB)
테스트 7 〉	통과 (0.10ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.25ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.19ms, 10.3MB)
테스트 13 〉	통과 (0.20ms, 10.2MB)
테스트 14 〉	통과 (0.24ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
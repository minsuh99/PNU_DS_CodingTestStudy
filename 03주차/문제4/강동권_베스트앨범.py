def solution(genres, plays):
    answer = []
    gp={}
    sorted_songs={}
    songs=zip(genres,plays)
    for i,song in enumerate(songs):
        g,p=song
        if gp.get(g):
            gp[g]=gp[g]+p
            sorted_songs[g].append((i,p))
        else:
            gp[g]=p
            sorted_songs[g]=[(i,p)]
    sorted_gp = list(sorted(gp.items(), key=lambda item: item[1], reverse=True))
    
    sorted_g = [item[0] for item in sorted_gp]
    
    for g in sorted_g:
        genre=sorted_songs[g]
        genre = sorted(genre, key=lambda item: (-item[1], item[0]))
        genre=genre[:2]
        for s in genre:
            answer.append(s[0])
    
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.3MB)
# 테스트 7 〉	통과 (0.06ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.07ms, 10.4MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.04ms, 10.1MB)
# 테스트 13 〉	통과 (0.06ms, 10.3MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)

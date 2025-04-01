# 결과적으로 실패!

def solution(N, stages):
    save = []
    for i in range(1, N+1):
        total = len(stages)
        num = stages.count(i)
        save.append(num / total)
        while i in stages:
            stages.remove(i)
    answer = [i+1 for i, v in sorted(enumerate(save), 
                                   key=lambda x:x[1], reverse=True)]
    # 이 윗 줄은 검색 도움을 받았음
    return answer

# 테스트는 통과했는데, 대부분 런타임 에러 뜸 ㅜ

# GPT 도움도 받았는데.. 더 이해가 안 감.. 내거를 살려달라고 했더니 더 어려움 ㅜ

def solution(enroll, referral, seller, amount):
    # 판매원별 수익금을 저장할 딕셔너리
    answer = {en : 0 for en in enroll}
    
    # 판매원과 추천인을 연결
    DICT = dict(zip(enroll, referral))
    
    for sell, amt in zip(seller, amount):
        amt *= 100
        tips = amt//10
        # 판매자에 수수료를 제외한 수익을 더함
        answer[sell] += (amt-tips)
        refer = DICT[sell]
        # 추천인의 수익은 판매자의 수수료
        amt = tips

        # 추천인이 센터거나 수수료가 0원일때까지 반복
        while refer != "-" and tips != 0:
            tips //= 10
            answer[refer] += (amt-tips)

            refer = DICT[refer]

            # 그냥 한줄 덜 실행하려고 넣음
            if refer == "-":
                break

            amt = tips

    answer = list(answer.values())
    
    return answer

'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 10.2MB)
테스트 2 〉    통과 (0.07ms, 10.3MB)
테스트 3 〉    통과 (0.06ms, 10.1MB)
테스트 4 〉    통과 (0.10ms, 10.1MB)
테스트 5 〉    통과 (0.76ms, 10.2MB)
테스트 6 〉    통과 (1.80ms, 12.4MB)
테스트 7 〉    통과 (2.10ms, 12.5MB)
테스트 8 〉    통과 (3.13ms, 12.5MB)
테스트 9 〉    통과 (12.68ms, 13.2MB)
테스트 10 〉    통과 (104.34ms, 20.9MB)
테스트 11 〉    통과 (90.25ms, 20.3MB)
테스트 12 〉    통과 (91.35ms, 20.5MB)
테스트 13 〉    통과 (93.41ms, 20.4MB)
'''

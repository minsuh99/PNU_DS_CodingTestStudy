def solution(enroll, referral, seller, amount):
    # 딕셔너리: enroll + 0 (최종 결과 딕셔너리)
    enroll_default = [0 for i in range(len(enroll))]
    enroll_dict = dict(zip(enroll, enroll_default))

    # 딕셔너리: enroll + referral
    enroll_referral = dict(zip(enroll, referral))
    
    for i, j in zip(seller, amount):
        j = j * 100
        if enroll_referral[i] == '-':
            enroll_dict[i] += int(j * 0.9)
        else:
            temp_person = i
            temp_amount = j
            while temp_person != '-':
                if temp_amount >= 10:
                    enroll_dict[temp_person] += temp_amount - int(temp_amount * 0.1)
                    temp_person = enroll_referral[temp_person]
                    temp_amount = int(temp_amount * 0.1)
                elif temp_amount < 10:
                    enroll_dict[temp_person] += int(temp_amount)
                    break

    return list(enroll_dict.values())

# 처음에 통과가 안됐음: 이유::: seller들 금액을 모두 합쳐버렸더니 소숫점 문제로 틀림
# 이유를 지피티에 물었음

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.17ms, 10.2MB)
# 테스트 5 〉	통과 (1.44ms, 10.4MB)
# 테스트 6 〉	통과 (2.31ms, 12.5MB)
# 테스트 7 〉	통과 (2.44ms, 12.5MB)
# 테스트 8 〉	통과 (3.93ms, 12.6MB)
# 테스트 9 〉	통과 (20.62ms, 13.5MB)
# 테스트 10 〉	통과 (214.03ms, 21.1MB)
# 테스트 11 〉	통과 (169.01ms, 20.8MB)
# 테스트 12 〉	통과 (160.33ms, 20.8MB)
# 테스트 13 〉	통과 (205.78ms, 20.9MB)
def solution(enroll, referral, seller, amount):
    
    # 수익을 받을 딕셔너리
    income = {}
    for name in enroll:
        income[name] = 0
    # 트리 구조로 저장
    parent = dict(zip(enroll, referral))
    # print(parent)
    # 수익 배분
    for i in range(len(seller)):
        per = seller[i]
        pro = amount[i] * 100
        # print(per, pro)
        # per을 parent의 key에서 찾고
        # key에 해당하는 value가 '-'이면 중단 1원 미만이면 중단
        while per != '-' and pro > 0: # 처음에 or을 사용
            parent_pro = pro //10
            my_pro = pro - parent_pro
            income[per] += my_pro
            
            per = parent[per]
            pro = parent_pro
    answer = []
    for name in enroll:
        answer.append(income[name])
    return answer
    

'''
모든 판매원은 이익의 10%를 계산
자신을 참여시킨 추천인에게 배분
나머지는 자기가 가짐

모든 판매원은 가입시킨 판매원 이익의 10%까지 자기가 가질 수 있음

원 단위 절사
10% 가 1원 미만인 경우에는 이득 분배 없고 판매원이 모두 가짐


판매원 enroll 
판매원을 참여시킨 판매원 refrral
판매량 집계 데이터의 판매원 이름 나열 seller
''판매수량 amount
각 판매원이 득한 이익금을 나열한 배열 return

부모-자식 관계 딕셔너리 저장
현재 자식 노드가 번 돈을 10% 부모노드로 주고
해당 자식 노드가 번 최종 수익을 딕셔너리로 저장
수익 배분을 하면서 부모노드로 올라가도록
상위 추천인이 있으면 반복으로 위로 계속 올라감
'-' 인 경우 루트노드임
1원 미만 중단
1개당 100원



while문에서 or사용 에러
-> 둘 다 만족해야 루프 실행 추천인 있고 수익도 있을 때만
수익이 있으나 추천인이 없을 때 멈춰야 하는데
추천인이 없어도 수익이 있으면 루프를 계속 돌게됨
수익이 없고 추천인이 있을 때도 멈춰야하는데
수익이 없어도 추천인이 있으면 계속 돌게 됨
따라서 and를 사용해야함

'''
# 트리를 재귀 함수로 탐색할 것이기 때문에 런타임 에러가 나지 않게 시스템 재귀 깊이 제한을 풀어줌
import sys
sys.setrecursionlimit(10 ** 6)


# 새 노드를 부모 노드와 연결시켜 트리를 만드는 함수
def make_tree(tree, parent_idx, node):
    idx, x, y = node
    (p_x, p_y), left, right = tree[parent_idx]

    # 새 노드의 x좌표가 부모 노드보다 작을 경우 왼쪽 서브 트리에 연결
    if x < p_x:
        # 부모의 왼쪽 자식 노드가 비어 있는 경우
        if left == 0:
            # 트리의 왼쪽 자식 자리에 새 노드를 연결
            tree[parent_idx][1] = idx
            # 연결된 새 노드에 정보를 저장(아직 자식이 없으므르 좌우 자식을 0으로 초기화)
            tree[idx] = [(x, y), 0, 0]
        # 부모의 왼쪽 자식 노드가 있는 경우
        else:
            # 왼쪽 자식 노드를 부모로하여 재귀
            make_tree(tree, left, node)

    # 오른쪽 서브 트리에 연결
    else:
        if right == 0:
            tree[parent_idx][2] = idx
            tree[idx] = [(x, y), 0, 0]
        else:
            make_tree(tree, right, node)

# 전위 순회 함수
def pre_order(tree, idx):
    res = []
    # 비어 있는 노드일 경우 번호를 저장하지 않음
    if idx == 0:
        return res

    '''
    전위 순회 이므로 루트 -> 왼쪽 자식 -> 오른쪽 자식 순서로 순회
    재귀의 형태인 이유는 왼쪽 자식을 순회한 다음 그 왼쪽 자식의 왼쪽, 오른쪽 자식을 순회한 다음
    루트의 오른쪽 자식을 탐색해야 하기 때문
    '''
    
    # 루트 노드를 저장
    res.append(idx)
    # 왼쪽 자식 저장
    res += pre_order(tree, tree[idx][1])
    # 오른쪽 자식 저장
    res += pre_order(tree, tree[idx][2])
    return res

# 후위 순회 함수
def post_order(tree, idx):
    res = []
    if idx == 0:
        return res

    '''
    후위 순회 이므로 왼쪽 자식 -> 오른쪽 자식 -> 루트 순서로 순회
    '''

    res += post_order(tree, tree[idx][1])
    res += post_order(tree, tree[idx][2])
    res.append(idx)
    return res


def solution(nodeinfo):
    sorted_node = []
    for idx, [x, y] in enumerate(nodeinfo, 1):
        sorted_node.append([idx, x, y])
    # y 좌표가 큰 노드부터 트리 생성
    sorted_node.sort(key=lambda x: -x[2])

    tree = dict()
    root_idx, r_x, r_y = sorted_node.pop(0)
    tree[root_idx] = [(r_x, r_y), 0, 0]

    # 모든 노드가 트리에 연결 될 때까지 레벨이 높은 노드부터 연결
    while sorted_node:
        node = sorted_node.pop(0)
        make_tree(tree, root_idx, node)

    return [pre_order(tree, root_idx), post_order(tree, root_idx)]


'''
정확성  테스트
테스트 1 〉    통과 (0.04ms, 10.1MB)
테스트 2 〉    통과 (0.05ms, 10.1MB)
테스트 3 〉    통과 (0.02ms, 10.3MB)
테스트 4 〉    통과 (0.01ms, 10.3MB)
테스트 5 〉    통과 (0.01ms, 10.2MB)
테스트 6 〉    통과 (151.32ms, 11.2MB)
테스트 7 〉    통과 (100.97ms, 11MB)
테스트 8 〉    통과 (69.62ms, 11.8MB)
테스트 9 〉    통과 (362.07ms, 14.4MB)
테스트 10 〉    통과 (18.79ms, 10.9MB)
테스트 11 〉    통과 (284.57ms, 14.7MB)
테스트 12 〉    통과 (326.42ms, 14.4MB)
테스트 13 〉    통과 (0.56ms, 10.1MB)
테스트 14 〉    통과 (3.48ms, 10.6MB)
테스트 15 〉    통과 (29.56ms, 12.1MB)
테스트 16 〉    통과 (49.49ms, 14.4MB)
테스트 17 〉    통과 (4.13ms, 10.5MB)
테스트 18 〉    통과 (62.37ms, 14.3MB)
테스트 19 〉    통과 (7.69ms, 10.9MB)
테스트 20 〉    통과 (35.03ms, 11.8MB)
테스트 21 〉    통과 (32.47ms, 12.4MB)
테스트 22 〉    통과 (55.80ms, 14MB)
테스트 23 〉    통과 (83.27ms, 14.5MB)
테스트 24 〉    통과 (0.04ms, 10.3MB)
테스트 25 〉    통과 (0.03ms, 10.3MB)
테스트 26 〉    통과 (236.48ms, 11.6MB)
테스트 27 〉    통과 (0.04ms, 10.1MB)
테스트 28 〉    통과 (0.07ms, 10.3MB)
테스트 29 〉    통과 (0.01ms, 10.2MB)
'''

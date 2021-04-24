# union-find 알고리즘은 그래프를 순환이 없는 그래프로 만들기 위해 사용합니다.
# find 함수로 해당 노드의 루트 노드를 찾습니다.
# union 함수로 두 노드의 루트 노드가 다르다면, 두 노드가 포함되어 있는 집합을 하나로 결합합니다.
# 만약, 루트 노드가 동일하다면 두 노드가 동일한 집합에 있는 것으로 판단하여 union 연산을 수행하지 않습니다.

N = int(input()) # 노드 수 입력 받기
M = int(input()) # 정점 수 입력 받기
parent = [0] * (N+1) # 부모 테이블 초기화

# 부모 테이블 상에서 자기 자신을 부모로 설정
for i in range(1, N+1):
    parent[i] = i

def find(a): # a 정점의 루트 노드 탐색
    if parent[a] == a: # a가 루트 노드이면, a 반환
        return a
    p = find(parent[a]) # 루트 노드 탐색
    parent[a] = p # a의 루트 노드 갱신
    return parent[a]

def union(a, b): # a와 b 집합을 병합
    a = find(a) # a의 루트 노드 탐색
    b = find(b) # b의 루트 노드 탐색
    if a == b: # 루트 노드가 동일하면, 동일한 집합
        return
    if rank[a] > rank[b]: # rank가 낮은 집합을 rank가 높은 집합으로 병합
        parent[b] = a # 병합
    else:
        parent[a] = b # 집합 병합
        if rank[a] == rank[b]: # 두 랭크가 동일하면
            rank[b] += 1 # 랭크 +1

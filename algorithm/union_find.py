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

def find(a): # a 노드의 부모 노드 찾기
    if a == parent[a]: # a 노드가 부모 노드이면 a 반환
        return a
    p = find(parent[a]) # a 노드를 따라가면서 부모 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a]

def union(a, b): # a집합과 b집합 합치기
    a = find(a) # a 노드의 부모 노드 찾기
    b = find(b) # b 노드의 부모 찾기

    if a == b: # 이미 동일한 집합이면 연결시에 순환이 발생
        return

    if a < b: # a의 부모가 b 부모보다 상위 루트이면
        parent[b] = a # b의 부모를 a의 부모로 변경
    else: # b의 부모가 a 부모보다 상위 루트이면
        parent[a] = b # a의 부모 변경

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

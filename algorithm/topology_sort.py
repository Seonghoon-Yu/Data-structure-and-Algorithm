from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 진입차수 0으로 초기화
in_degree = [0] * (v+1)
# 빈 인접리스트 그래프 생성
graph = [[] for i in range(v+1)]

# 방향 그래프의 간선 정보 입력 받기
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 갱신
    in_degree[b] += 1
    
# 위상정렬 함수
def topology_sort():
    result = []
    q = deque()
    
    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if in_degree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지 실행
    while q:
        # 진입차수 0인 노드 q에서 꺼내기
        node = q.popleft()
        result.append(node)
        
        # 꺼낸 노드의 간선 제거
        for i in graph[node]:
            in_degree[i] -= 1
            # 진입차수가 0인 새로운 노드 q에 삽입
            if in_degree[i] == 1:
                q.append(i)
    
    # 결과 출력
    for i in result:
        print(i, end=' ')

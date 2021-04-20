# 무향 그래프에서 순환 판별
# 방문한 정점을 기록하면서, 방문한 정점을 또 방문하면 사이클이 존재

V, E = map(int,input().split())
visited = [0] * (V+1) # 방문한 정점 정보를 담을 stack 생성
graph = [[] for i in range(V+1)] # 빈 인접 리스트 그래프 생성

# 그래프 생성
for i in range(E):
    a, b = map(int,input().split()) # 간선 정보 받아오기
    graph[a].append(b)
    graph[b].append(a)
    
# dfs 탐색 함수 생성
def dfs(i):
    visited[i] = 1 # 방문한 정점 정보 갱신
    
    node = graph[i] # 방문할 정점 받아오기
    
    if not node in visited: # 방문하지 않은 정점이면 dfs 진행
        dfs(node)
    elif node in visited: # 다음에 방문할 정점이 visitied에 존재하면 순환이 존재
        return True
    
    return False # 순환이 존재하지 않으면 False

result = False
for i in range(1, V+1): # 모든 정점 호출
    if visited[i] == 0: # 방문하지 않은 정점이면, 탐색 진행
        if dfs(i):
            result = True

print(result) # 순환이 존재하면 True 반환

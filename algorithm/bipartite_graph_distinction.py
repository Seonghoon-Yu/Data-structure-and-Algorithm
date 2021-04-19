# bipartite graph distinction, 무방향 그래프
# 1) dfs
#  정점을 방문하면서 각 정점을 1, -1 그룹으로 분할합니다.
#  이미 방문했던 정점이 현재 정점과 동일한 그룹이면 False를 반환합니다.

# 2) bfs
#  동일한 level에 존재하는 정점을 같은 그룹으로 지정합니다.
#  이미 방문한 정점인 경우, 그룹을 비교하여 현재 정점과 동일한 그룹이면 False를 반환합니다.


### dfs
# 방문하지 않은 점부터 방문, 이때 점을 2개의 그룹으로 나눈다.
# 만약 다음 점이 이미 방문한 점이면, 현재 점의 그룹과 같은지 비교
# 같은 그룹이면 False, 그렇지 않으면 계속 진행

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# dfs
def dfs(v, group):
    visited[v] = group # 방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]: # 방문한 곳인데, 그룹이 동일하면 False
            return False
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프

    bipatite = True

    for i in range(1, V+1):
        if visited[i] == 0: # 방문한 정점이 아니면, dfs 수행
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')


### bfs
import collections
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프


    q = collections.deque()
    group = 1
    bipatite = True
    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문하지 않은 정점이면 큐에 삽입
                        q.append(w)
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False

    print('YES' if bipatite else 'NO')

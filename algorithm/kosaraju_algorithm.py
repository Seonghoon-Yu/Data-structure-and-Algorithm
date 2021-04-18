# dfs를 활용하여 그래프 내의 ssc를 찾는 알고리즘
# 시간 복잡도 O(V+E)
# 정방향 그래프에서 dfs를 실행하여 post가 높은 정점이 ssc의 source가 되고,
# 역방향 그래프에서 dfs를 실행하여 post가 높은 정점이 ssc의 sink가 된다.
# 찾은 source와 sink를 묶어 ssc를 생성한다.

# 작동원리
# (1) 방향 그래프 내에서 dfs를 실행하여, dfs 탐색을 마친 정점을 stack에 삽입한다.
# (2) 역방향 그래프를 생성한다.
# (3) stack에서 정점을 추출하여, 역방향 그래프에서 dfs를 실행한다.
# (4) 방문하는 정점을 ssc 에 삽입한다.
# (5) 탐색이 종료되면, ssc
# (6) stack에서 방문하지 않은 정점을 추출하여, 역방향 그래프에서 dfs를 실행


import collections

V, E = map(int, input().split())
visited = [0] * (V+1) # visitied 초기화
graph = [[] for i in range(V + 1)] # 빈 그래프 생성

# 주어진 간선에 따라 그래프 채워넣기
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

# dfs 재귀 함수
def dfs(v, visited, stack):
    visited[v] = 1

    for w in graph[v]:
        if visited[w] == 0:
            stack.append(w)
            dfs(w, visited, stack)
    stack.append(v) # 탐색을 마친 노드 stack에 저장.

# 역방향 그래프 생성
def reverseGraph():
    reverse_graph = [[] for i in range(V+1)]
    for i in range(1, V+1):
        for j in graph[i]:
            reverse_graph[j].append(i)
    return reverse_graph

# 역방향 그래프에 dfs 진행
def reverseDfs(v, visited,stack):
    visited[v] = 1
    stack.append(v)
    for w in reverse_graph[v]:
        if visited[w] == 0:
            reverseDfs(w, visited, stack)

stack = []
for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack) # stack에 탐색을 마친 정점 순으로 저장

reverse_graph = reverseGraph() # 역방향 그래프 생성

visited = [0] * (V+1) # visited 초기화
results = [] # ssc를 담을 result 생성

while stack:
    ssc = []
    node = stack.pop() # stack에서 ssc의 source 추출
    if visited[node] == 0:
        reverseDfs(node, visited, ssc) # dfs를 진행하면서, ssc의 source부터 탐색을 진행한다. 탐색한 정점은 ssc에 저장
        results.append(sorted(ssc)) # 재귀가 끝난 정점이 ssc의 sink

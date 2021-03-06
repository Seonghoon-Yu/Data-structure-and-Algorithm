# 재귀를 이용한 DFS
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
  
# 스택을 이용한 반복 구조
def iterative_dfs(start_v):
    discoverd = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if not v in discoverd:
            discoverd.append(v)
            for w in graph[v]:
                stack.append(w)
    return discoverd

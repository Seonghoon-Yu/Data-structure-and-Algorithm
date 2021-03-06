# 큐를 이용한 반복 구조
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if not w in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

# 1) 유향 그래프에서 순환 그래프 판별
# 2개의 stack을 이용합니다.
# trace stack은 dfs 탐색 경로를 저장합니다.
# visited stack은 탐색을 마친 노드를 저장합니다. 가지치기의 역할입니다.
# trace stack에 dfs 탐색 경로를 저장하면서, 이미 경로에 포함되어 있는 노드가 또 방문 된다면
# 순환 그래프 인것을 알 수 있습니다.

# 추적 경로를 담을 set 생성
traced = set()
# 방문한 노드를 담을 set 생성
visited = set()

def dfs(v):
    # 이미 탐색을 마친 노드이면 dfs 종료
    if v in visited:
        return True
    # 경로에 포함되어 있는 노드이면 순환 그래프
    if v in traced:
        return False
    # 경로에 v 노드 추가
    traced.add(v)
    for w in graph[v]:
        if not dfs(w):
            return False
    # 경로에 v노드 제거
    traced.remove(v)
    # 방문한 노드에 v 추가
    visited.add(v)
    return True

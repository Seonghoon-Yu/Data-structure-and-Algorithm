# 최단 거리를 찾는 알고리즘
# 시간복잡도 O(VE) V: 정점 수, E: 간선 수
# 방향 그래프에서 음의 가중치를 지닌 간선이 존재할 때 사용
# 음의 순환이 있는 경우에는 최단 거리를 찾지 못함

# 작동 원리
# 시작 노드에 대해서 거리를 0으로 초기화, 나머지 노드는 거리를 무한으로 설정
# 정점 수(n) -1 만큼 다음 과정을 반복
# 매 반복 마다 모든 간선 확인
# 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
# n-1번 반복 이후, n번째 반복에서도 거리 값이 갱신된다면 음수 순환이 존재
# 다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것입니다. 
# 다익스트라는 방문하지 않는 노드 중에서 최단 거리가 가장 가까운 노드만을 방문했습니다.


import sys
import collections
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수 입력 받기
edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 그래프 생성
for _ in range(m):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0 # 시작 노드에 대해서 거리를 0으로 초기화
    for i in range(n): # 정점 수만큼 반복
        for j in range(m): # 매 반복 마다 모든 간선 확인
            node = edges[j][0] # 현재 노드 받아오기
            next_node = edges[j][1] # 다음 노드 받아오기
            cost = edges[j][2] # 가중치 받아오기
            # 현재 간선을 거려서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1: # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])

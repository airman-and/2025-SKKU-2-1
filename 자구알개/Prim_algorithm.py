import sys

# 주어진 edges를 인접 리스트로 변환
edges = [
    (0, 1, 15), (0, 2, 7), (0, 3, 9), (0, 4, 4),
    (1, 2, 10), (1, 3, 3), (1, 6, 6),
    (2, 3, 999),  # 없음
    (3, 4, 8), (3, 5, 1), (3, 6, 7),
    (4, 5, 13),
    (5, 6, 5)
]

# 인접 리스트 생성
N = 7  # 정점 수
g = [[] for _ in range(N)]
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))  # 무방향 그래프이므로 양방향으로 추가

# Prim 알고리즘 초기화
s = 0  # 시작 정점
visited = [False] * N
dist = [sys.maxsize] * N
dist[s] = 0
previous = [None] * N
previous[s] = s

# Prim 알고리즘 실행
for _ in range(N):
    # 방문하지 않은 정점 중 최소 거리를 가진 정점 찾기
    u = -1
    min_dist = sys.maxsize
    for i in range(N):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
    
    visited[u] = True
    
    # 인접한 정점들의 거리 업데이트
    for v, w in g[u]:
        if not visited[v] and w < dist[v]:
            dist[v] = w
            previous[v] = u

# 결과 출력
print('최소신장트리 간선들:')
mst_cost = 0
for i in range(1, N):
    print(f"({i}, {previous[i]})", end=' ')
    mst_cost += dist[i]
print(f'\n최소신장트리 가중치: {mst_cost}')

edges = [
    (0, 1, 15), (0, 2, 7), (0, 3, 9), (0, 4, 4),
    (1, 2, 10), (1, 3, 3), (1, 6, 6),
    (3, 4, 8), (3, 5, 1), (3, 6, 7),
    (4, 5, 13),
    (5, 6, 5)
]

# 가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])

# Union-Find를 위한 초기화
N = 7  # 정점의 수
parent = [i for i in range(N)]
rank = [0] * N

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    
    if root_u == root_v:
        return
        
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

# Kruskal 알고리즘 실행
mst = []
mst_cost = 0
edge_count = 0

for edge in edges:
    u, v, weight = edge
    
    # 사이클이 형성되지 않는 경우에만 간선 추가
    if find(u) != find(v):
        mst.append((u, v))
        mst_cost += weight
        union(u, v)
        edge_count += 1
        
        # MST는 (정점 수 - 1)개의 간선을 가짐
        if edge_count == N - 1:
            break

# 결과 출력
print('최소신장트리 간선들:')
for u, v in mst:
    print(f"{u} - {v}")
print('최소신장트리 가중치:', mst_cost)
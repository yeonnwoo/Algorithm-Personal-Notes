## 기타 그래프

### Disjoint sets (서로소 집합)
- Union-Find
    - 사이클 판별
    
### Spanning Tree (신장 트리)
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

### MST (최소 신장 트리)
- Kruskal Algorithm
    - 모든 간선에 대하여 정렬
    - 사이클 발생 여부 판별
    - False라면 집합에 포함
    - 간선의 개수가 E일때, Time complex=O(ElogE)
    
### Topology Sort (위상 정렬)
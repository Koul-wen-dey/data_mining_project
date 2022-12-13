import numpy as np
from function import find_neighbors, adjacency_matrix

a = np.array([1,2,3])
a[a>1] = 0
def simrank(graph, decay=0.9, iterations=20):
    n = graph.shape[0]
    sim = np.identity(n)
    sim_next = np.identity(n)
    neighbors = find_neighbors(graph)

    for _ in range(iterations):
        for u in range(n):
            for v in range(n):
                if u == v:
                    continue
                sim_value = 0
                for x in neighbors[u]:
                    for y in neighbors[v]:
                        sim_value += sim[x,y]
                lu = len(neighbors[u]) if len(neighbors[u]) > 0 else 1
                lv = len(neighbors[v]) if len(neighbors[v]) > 0 else 1
                sim_next[u,v] = decay / (lu * lv) * sim_value
        sim = sim_next.copy()
        print(sim)
    return sim


if __name__ == '__main__':
    arr = np.loadtxt('./hw3dataset/graph_4.txt',delimiter=',',ndmin=2,dtype=np.uint32)
    mat = adjacency_matrix(arr)
    print(mat)
    np.set_printoptions(suppress=True, precision=3)
    d = simrank(mat)
    print(d)
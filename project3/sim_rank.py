import numpy as np
from function import find_neighbors, adjacency_matrix, std_output

def sim_rank(graph:np.array, decay:float=0.9, iterations:int=100):
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
                lu = len(neighbors[u]) 
                lv = len(neighbors[v])
                if lu == 0 or lv == 0:
                    sim_next[u,v] = 0
                else:
                    sim_next[u,v] = (decay / (lu * lv)) * sim_value
        sim = sim_next.copy()
    return sim


if __name__ == '__main__':
    arr = np.loadtxt('./hw3dataset/graph_1.txt',delimiter=',',ndmin=2,dtype=np.uint32)
    mat = adjacency_matrix(arr)
    np.set_printoptions(suppress=True, precision=3)
    d = sim_rank(mat)
    std_output(d,'sim')
import numpy as np
from function import adjacency_matrix, std_output

def page_rank(graph:np.array, damping_factor:float=0.15, epsilon:float=1.0e-8):
    num_nodes = graph.shape[0]
    L = np.sum(graph,axis=1)
    L[L==0] = 1
    for i,col in enumerate(graph):
        col /= L[i]
    page_ranks = np.full(num_nodes, 1/num_nodes)
    while True:
        next_page_ranks = np.full(num_nodes,damping_factor / num_nodes)
        next_page_ranks += (1 - damping_factor) * np.dot(graph.T, page_ranks)

        if np.sum(np.abs(page_ranks - next_page_ranks)) < epsilon:
            break
        page_ranks = next_page_ranks
    return page_ranks



if __name__ == '__main__':
    arr = np.loadtxt('./hw3dataset/graph_1.txt',delimiter=',',ndmin=2,dtype=np.uint32)
    mat = adjacency_matrix(arr)
    print(mat)
    t = page_rank(mat)
    std_output(t,'page')
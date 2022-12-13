import numpy as np
from function import adjacency_matrix, std_output

def hits(G:np.array, max_iterations:int=100):
    a = np.ones(G.shape[0])
    h = np.ones(G.shape[0])

    for _ in range(max_iterations):
        a = G.T.dot(h)
        h = G.dot(a)
        a /= np.linalg.norm(a, ord=1)
        h /= np.linalg.norm(h, ord=1)
    return {'Authority': a, 'Hub': h}

if __name__ == '__main__':
    arr = np.loadtxt('./hw3dataset/graph_1.txt',delimiter=',',ndmin=2,dtype=np.uint32)
    mat = adjacency_matrix(arr)
    print(mat)
    d = hits(mat,100)
    std_output(d,'hits')
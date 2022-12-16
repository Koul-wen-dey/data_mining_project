import numpy as np

def adjacency_matrix(edges:np.array):
    n = np.max(edges)
    matrix = np.zeros((n, n))
    for i, j in edges:
        matrix[i-1, j-1] = 1
    return matrix

def find_neighbors(mtx:np.array):
    neighbors = {}
    for i in range(mtx.shape[0]):
        neighbors[i] = np.nonzero(mtx.T[i])[0]
    return neighbors

def std_output(arr:np.array,algo:str):
    np.set_printoptions(suppress=True, precision=3)
    if algo == 'hits':
        print('Authority:')
        print(arr['Authority'])
        print('Hub:')
        print(arr['Hub'])

    elif algo == 'page':
        print('Page Rank:')
        print(arr)

    elif algo == 'sim':
        print('SimRank:')
        print(arr)
    
    else:
        pass
    
    print()
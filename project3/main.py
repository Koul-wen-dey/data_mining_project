import numpy as np
from function import adjacency_matrix, std_output
from page_rank import page_rank
from hits import hits

damping_factor = 0.85
decay_factor = 0.7
iterations = 30

if __name__ == "__main__":
    path = './hw3dataset/graph_'
    for i in range(1,7):
        file = path + str(i) + '.txt'
        print(f'graph{i}')
        arr = np.loadtxt(file,delimiter=',',ndmin=2,dtype=np.uint32)
        mat = adjacency_matrix(arr)
        d = hits(mat,iterations)
        std_output(d,'hits')
        np.savetxt(f'./result/graph_{i}/graph_{i}_HITS_authority.txt',d['Authority'],'%.8f',' ',' ')
        np.savetxt(f'./result/graph_{i}/graph_{i}_HITS_hub.txt',d['Hub'],'%.8f',' ',' ')
        e = page_rank(mat,damping_factor)
        std_output(e,'page')
        np.savetxt(f'./result/graph_{i}/graph_{i}_PageRank.txt',e,'%.8f',' ',' ')
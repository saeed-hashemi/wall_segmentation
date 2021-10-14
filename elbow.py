import numpy as np
def find(p):   
    distances = np.zeros(p.shape[1], dtype=np.uint32)
    nothing=True
    for col in range(p.shape[1]):
        if p[0][col]==1:
            for row in range(p.shape[0]):
                if p[row][col]==0:
                    distances[col]=row-1
                    nothing=False
                    break

    # print(np.argmax(distances), np.max(distances), nothing)
    if np.max(distances) != 0:
        all_max_distance_idx = np.argwhere(distances == np.amax(distances))
        if len(all_max_distance_idx)>1:
            if distances[0]<distances[-1]:
                return np.max(distances), all_max_distance_idx.flat[0]
            else:
                return np.max(distances), all_max_distance_idx.flat[-1]
        else:
            return np.max(distances), np.argmax(distances)
    return None
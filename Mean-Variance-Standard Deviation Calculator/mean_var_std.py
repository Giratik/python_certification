import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations  = {}
    flat = np.array(list)
    sh_list = np.array(list)
    matrix = sh_list.reshape(3, 3)

    #mean part
    row = np.mean(matrix, axis=1).tolist()
    col = np.mean(matrix, axis=0).tolist()
    calculations["mean"] = [col, row , np.mean(flat).tolist()]

    #variance part
    row = np.var(matrix, axis=1).tolist()
    col = np.var(matrix, axis=0).tolist()
    calculations["variance"] = [col, row , np.var(flat).tolist()]

    #standard deviation part
    row = np.std(matrix, axis=1).tolist()
    col = np.std(matrix, axis=0).tolist()
    calculations["standard deviation"] = [col, row , np.std(flat).tolist()]

    #max part
    row = np.max(matrix, axis=1).tolist()
    col = np.max(matrix, axis=0).tolist()
    calculations["max"] = [col, row , np.max(flat).tolist()]

    #min part
    row = np.min(matrix, axis=1).tolist()
    col = np.min(matrix, axis=0).tolist()
    calculations["min"] = [col, row , np.min(flat).tolist()]

    #sum part
    row = np.sum(matrix, axis=1).tolist()
    col = np.sum(matrix, axis=0).tolist()
    calculations["sum"] = [col, row , np.sum(flat).tolist()]


    
    return calculations
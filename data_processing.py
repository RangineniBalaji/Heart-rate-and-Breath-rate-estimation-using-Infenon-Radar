import numpy as np

def load_data(file_path):
    with open(file_path, "rb") as f:
        data = np.fromfile(f, dtype="complex128")
    return data

def scale_data(data):
    scaled_data = np.log1p(np.abs(data))
    return scaled_data

def reshape_data(data):
    data = data[155:]
    reshaped_data = data.reshape((450,16384)) 
    return reshaped_data
import numpy as np

data = np.load("./dataset_synthetic_2/hp_sim_sequence_input.npz")["feature"]
print ("[dataset_synthetic_2] data.shape: ", data.shape) # (9000, 12, 896)

data = np.load("./dataset_hp/hp_sequence_input.npz")["feature"]
print ("[dataset_hp] data.shape: ", data.shape) # (4063, 12, 896)

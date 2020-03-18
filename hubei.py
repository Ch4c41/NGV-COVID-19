import matplotlib.pyplot as plt
import numpy as np

data_len = 64

# Growing
healthy = np.zeros(data_len)
dead = np.zeros(data_len)
recovered = np.zeros(data_len)
infected = np.zeros(data_len)
proven = np.zeros(data_len) # Tested and proven infected

# Underlying
infection_rate = 1

# Initial
region = "Norway"
healthy[0] = 5_494_000
infected[0] = 10

# Growth
for i in range(1, data_len):
    

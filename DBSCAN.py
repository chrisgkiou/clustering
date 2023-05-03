import numpy as np
import hashlib
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import pdist, squareform

# Define Nilsimsa function
def nilsimsa(s):
    """
    Compute the Nilsimsa digest of a string.
    """
    h = hashlib.sha256(s.encode()).digest()
    return [int(b) for b in bin(int.from_bytes(h, 'big'))[2:].zfill(256)[:64]]

# Define Hamming distance function
def hamming_distance(x, y):
    """
    Compute the Hamming distance between two arrays of binary digits.
    """
    return np.sum(np.array(x) != np.array(y))

# Example addresses
addresses = ['1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
             '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
             '13igL3tRXJ6GqdYzFjz5B5eRvTpZCkB8Au',
             '1HSJjy8mRk8WbF6UAXc6hCtfE9H2q3mK1N',
             '1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy']

# Convert addresses to digests
digests = np.array([nilsimsa(addr) for addr in addresses])

# Compute pairwise Hamming distance matrix
hamming_mat = squareform(pdist(digests, metric=hamming_distance))

# Apply DBSCAN clustering
dbscan = DBSCAN(metric='precomputed', eps=2, min_samples=2)
labels = dbscan.fit_predict(hamming_mat)

# Print cluster labels for each address
for i, addr in enumerate(addresses):
    print(f'{addr}: Cluster {labels[i]}')

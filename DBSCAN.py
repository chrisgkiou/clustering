import numpy as np
import hashlib
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import pdist, squareform
import nilsimsa

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
addresses = ['1L4D4Fp4kPkVSqw1Bg4jKCLM2wZdSbckYj',
             '12PsgKvG1cDovouzFtmBJoeFWXhkbiKxhN']

# Convert addresses to digests
digests = np.array([nilsimsa(addr) for addr in addresses])

print(digests)

# Compute pairwise Hamming distance matrix
hamming_mat = squareform(pdist(digests, metric=hamming_distance))

print(hamming_mat)



# Apply DBSCAN clustering
dbscan = DBSCAN(metric='precomputed', eps=2, min_samples=2)
labels = dbscan.fit_predict(hamming_mat)

# Print cluster labels for each address
for i, addr in enumerate(addresses):
    print(f'{addr}: Cluster {labels[i]}')


import numpy as np
from scipy.spatial.distance import hamming
from sklearn.cluster import KMeans
import hashlib

def nilsimsa(s):
    """
    Compute the Nilsimsa digest of a string.
    """
    h = hashlib.sha256(s.encode()).digest()
    return [int(b) for b in bin(int.from_bytes(h, 'big'))[2:].zfill(256)[:64]]

addresses = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net', 'https://www.example.co.uk', 'https://www.example.edu']
digests = np.array([nilsimsa(addr) for addr in addresses])

def hamming_distance(x, y):
    return hamming(x, y)

kmeans = KMeans(n_clusters=2, random_state=0, precompute_distances=hamming_distance).fit(digests)

print(kmeans.labels_)

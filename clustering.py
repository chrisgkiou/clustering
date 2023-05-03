from sklearn.cluster import KMeans
import numpy as np

# Define the Nilsimsa function
import hashlib

def nilsimsa(s):
    """
    Compute the Nilsimsa digest of a string.
    """
    h = hashlib.sha256(s.encode()).digest()
    return [int(b) for b in bin(int.from_bytes(h, 'big'))[2:].zfill(256)[:64]]


# List of Bitcoin addresses to cluster
addresses = [
    '1L4D4Fp4kPkVSqw1Bg4jKCLM2wZdSbckYj',
    '12PsgKvG1cDovouzFtmBJoeFWXhkbiKxhN'
]

# Compute Nilsimsa digests for each address
digests = np.array([nilsimsa(addr) for addr in addresses])

# Cluster the digests using KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(digests)

# Print the clusters
for i in range(2):
    cluster = digests[kmeans.labels_ == i]
    print(f'Cluster {i}: {len(cluster)} addresses')
    for j, digest in enumerate(cluster):
        print(f'  Address {j+1}: {" ".join(str(bit) for bit in digest)}')



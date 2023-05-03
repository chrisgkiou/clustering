import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import hashlib


def nilsimsa(s):
    """
    Compute the Nilsimsa digest of a string.
    """
    h = hashlib.sha256(s.encode()).digest()
    return [int(b) for b in bin(int.from_bytes(h, 'big'))[2:].zfill(256)[:64]]

addresses = [
    '1KXfW1AZvKkUMpVgCzgz8RpZKtaCvFemMh',
    '1CLT9dJ9z7PjK2HP2mcAnVUZv1fZ7VUoK6',
    '1L4D4Fp4kPkVSqw1Bg4jKCLM2wZdSbckYj',
    '12PsgKvG1cDovouzFtmBJoeFWXhkbiKxhN',
    '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
]


# Compute Nilsimsa digests for each address and store in a numpy array
digests = np.array([nilsimsa(addr) for addr in addresses])

# Compute WSS for different number of clusters
wss = []
for k in range(1, len(addresses)):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(digests)
    wss.append(kmeans.inertia_)

# Plot WSS as a function of number of clusters
plt.plot(range(1, 5), wss)
plt.xlabel('Number of clusters')
plt.ylabel('WSS')
plt.show()

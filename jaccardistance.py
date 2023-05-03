import hashlib


def nilsimsa(input_string):
    # Convert input string to byte array
    input_bytes = input_string.encode('utf-8')

    # Compute SHA-1 hash of input string
    sha1_hash = hashlib.sha1(input_bytes).digest()

    # Convert SHA-1 hash to binary string
    binary_hash = bin(int.from_bytes(sha1_hash, byteorder='big'))[2:].zfill(160)

    # Initialize Nilsimsa digest
    digest = [0] * 256

    # Compute Nilsimsa digest by XORing adjacent pairs of bits in the binary hash
    for i in range(0, len(binary_hash) - 1, 2):
        index = int(binary_hash[i:i + 2], 2)
        digest[index] = 1

    # Return Nilsimsa digest as a list of 0's and 1's
    return digest


input_string = ('this is another text')
digest = nilsimsa(input_string)
print(digest)


# Define the texts to hash
text1 = "1L4D4Fp4kPkVSqw1Bg4jKCLM2wZdSbckYj"
text2 = "12PsgKvG1cDovouzFtmBJoeFWXhkbiKxhN"

# Calculate the hashes
hash1 = nilsimsa.Nilsimsa(text1.encode()).hexdigest()
hash2 = nilsimsa.Nilsimsa(text2.encode()).hexdigest()
print(hash1)
print(hash2)

# Convert the hashes to binary strings
binary_hash1 = bin(int(hash1, 16))[2:].zfill(256)
binary_hash2 = bin(int(hash2, 16))[2:].zfill(256)
print(binary_hash1)
print(binary_hash2)

# Check if the binary strings match the hashes
if binary_hash1 == "0110100101011110011010010011010101001101101111010111101111100011111011111000100110011010110001110100100110000011011110010100001111101101011100111111011111111000111101111101011111011101010111110001011110011100111001011111111001011110111011001011111001101011":
    print("Binary hash 1 matches the given hash")
else:
    print("Binary hash 1 does not match the given hash")

if binary_hash2 == "0110100111110001111110111110101011101111010101011100011001110100011100010101111110110101101011110110111011110011011110111110110110111111010011101110011100011011101010110011100000100111001111011100000101010101111110010010110001011101000111111111000110100100":
    print("Binary hash 2 matches the given hash")
else:
    print("Binary hash 2 does not match the given hash")
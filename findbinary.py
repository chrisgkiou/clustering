import nilsimsa

hash1 = "695e69354dbd7be3ef899ac749837943ed73f7f8f7d7dd5f179ce5fe5eecbe6b"
hash2 = "69f1fbeaef55c674715fb5af6ef37bedbf4ee71bab38273dc155f92c5d1ff1a4"

# Convert the hashes to binary strings
bin_hash1 = bin(int(hash1, 16))[2:].zfill(256)
bin_hash2 = bin(int(hash2, 16))[2:].zfill(256)

print(bin_hash1)
print(bin_hash2)

# Compute the Hamming distance
hamming_dist = sum(ch1 != ch2 for ch1, ch2 in zip(bin_hash1, bin_hash2))

print(f"The Hamming distance between the two hashes is {hamming_dist}")

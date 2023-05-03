import nilsimsa

text = "1L4D4Fp4kPkVSqw1Bg4jKCLM2wZdSbckYj"
text2 = "12PsgKvG1cDovouzFtmBJoeFWXhkbiKxhN"
hash1 = nilsimsa.Nilsimsa(text).hexdigest()
hash2 = nilsimsa.Nilsimsa(text2).hexdigest()

print(hash1)
print(hash2)

normalized_distance = (128 - nilsimsa.compare_digests(hash1, hash2, is_hex_1=True, is_hex_2=True)) / 128.
distance = (128 - nilsimsa.compare_digests(hash1, hash2, is_hex_1=True, is_hex_2=True))

print(distance)
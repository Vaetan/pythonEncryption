from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

message = "Hello"
key = DSA.generate(640)
hash = SHA.new(message).digest()
k = random.StrongRandom().randint(1, key.q - 1)
sig = key.sign(hash, k)

if key.verify(hash, sig):
    print("OK")
else:
    print("Incorrect Signature")

    # NOTES:
    # Generate function int must be a multiple of 64, between 512-1024

from Crypto.Cipher import AES
from Crypto import Random

# ------------------------------------------------------
# 16 Bit Encryption

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Here is a sixteen bit encryption')

print("Ciphertext: " + msg)

plaintext = cipher.decrypt(msg)

# Remove initial 16 bytes off string

plaintext = plaintext[16:]

print(plaintext + "\n")

# ------------------------------------------------------
# 24 Bit Encryption

key2 = b'qwertyuiopasdfghjklzxcvb'
iv2 = Random.new().read(AES.block_size)
cipher2 = AES.new(key2, AES.MODE_CFB, iv2)
msg2 = iv2 + cipher2.encrypt(b'Here is a twenty four bit encryption')

print("Ciphertext: " + msg2)

plaintext2 = cipher2.decrypt(msg2)

# Remove initial 16 bytes off string

plaintext2 = plaintext2[16:]

print(plaintext2 + "\n")

# ------------------------------------------------------
# 32 Bit Encryption

key3 = b'qwertyuiopasdfghjklzxcvbnmqwerty'
iv3 = Random.new().read(AES.block_size)
cipher3 = AES.new(key3, AES.MODE_CFB, iv3)
msg3 = iv3 + cipher3.encrypt(b'Here is a thirty two bit encryption')

print("Ciphertext: " + msg3)

plaintext3 = cipher3.decrypt(msg3)

# Remove initial 16 bytes off string

plaintext3 = plaintext3[16:]

print(plaintext3 + "\n")

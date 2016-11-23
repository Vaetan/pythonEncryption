from Crypto.Cipher import ARC2
from Crypto import Random

#------------------------------------------------------
#16 Bit Encryption
key = b'Sixteen byte key'
iv = Random.new().read(ARC2.block_size)
cipher = ARC2.new(key, ARC2.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')

print(msg + "\n")

plaintext = cipher.decrypt(msg)

#Remove initial 8 bytes off string

plaintext = plaintext[8:]

print(plaintext + "\n")

#------------------------------------------------------
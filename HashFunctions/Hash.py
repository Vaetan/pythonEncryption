from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import SHA256

# ------------------------------------------------------
# MD5 Hash

h = MD5.new()
h.update(b'MD5 Hash Plaintext!')
print h.hexdigest()

# ------------------------------------------------------
# SHA Hash

h = SHA.new()
h.update(b'SHA Hash Plaintext!')
print h.hexdigest()

# ------------------------------------------------------
# SHA-256 Hash

h = SHA256.new()
h.update(b'SHA-256 Hash Plaintext!')
print h.hexdigest()


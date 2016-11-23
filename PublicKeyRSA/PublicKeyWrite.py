from Crypto.PublicKey import RSA

key = RSA.generate(2048)
print("Key Generated")
print("Saving Key...")

fileName = raw_input("Please enter a key name: ")
f = open(fileName + '.pem', 'w')
f.write(key.exportKey('PEM', passphrase='password'))
f.close()

print("Generating Public Key...")
pubkey = key.publickey()
f = open('public.pem', 'w')
f.write(pubkey.exportKey('PEM'))
f.close()


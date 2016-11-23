from Crypto.PublicKey import RSA

fileName = raw_input("Please enter the file name for the key: ")
print("Reading Key...")
f = open(fileName + '.pem', 'r')

lines = f.read().splitlines()
for line in lines:
    # print line
    if "Proc-Type" in line:
        print("Password required...")
        # userPass = raw_input("Please enter password: ")
        break

f.seek(0,0)

key = RSA.importKey(f.read(), passphrase="password")
print("Key read successful. Storing it in a safe place...")
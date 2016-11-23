from Crypto.Hash import SHA256

userInput = raw_input("Enter a password you want hashed!: ")

h = SHA256.new()
h.update(userInput)
print ("Here's your hashed sentence!: " + h.hexdigest())

userInputVerification = raw_input("Now, verify your password: ")

h = SHA256.new()
h.update(userInputVerification)
print ("Here's your hashed sentence!: " + h.hexdigest())

if userInputVerification == userInput:
    print("Password verified!")
else:
    print("Password verification failed...")

import rsa

# Reload public key from file for testing
with open("password.txt", "rb") as passwordFile:
    encPass = passwordFile.read()

print('encrypted: ', encPass)

# Reload private key from file for testing
with open("RustyPrivate.pem", "rb") as privateFile:
    privateKeyData = privateFile.read()

privateKeyFromFile = rsa.PrivateKey.load_pkcs1(privateKeyData)

# Decrypt encPass and print out decPass
decPass = rsa.decrypt(encPass, privateKeyFromFile)
print(decPass.decode('utf8'))
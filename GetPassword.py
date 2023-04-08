# Import module for getpass and rsa
import rsa
import getpass

# Get the password from the user
password = getpass.getpass(prompt='Password: ').encode('utf8')

# Reload public key from file for testing
with open("MatthewPublic.pem", "rb") as publicFile:
    publicKeyData = publicFile.read()

publicKeyFromFile = rsa.PublicKey.load_pkcs1(publicKeyData)

# Encrypt a password with publicKeyFromFile
encPass = rsa.encrypt(password, publicKeyFromFile)

print(encPass)

# Write encrypted password to file
with open("password.txt", "wb") as passwordKeyFile:
    passwordKeyFile.write(encPass)
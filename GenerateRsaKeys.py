# Pre-requisites
# pip install rsa (or install it into your virtual environment using your IDE)
import getpass
import rsa

# Generate new public and private RSA keys
(publicKey, privateKey) = rsa.newkeys(2048)

# Export public key in PKCS#1, PEM encoded
publicKeyPkcsPem = publicKey.save_pkcs1().decode('utf8')
print(publicKeyPkcsPem)

publicKeyFile = open("public_key.pem", "w")
publicKeyFile.write(publicKeyPkcsPem)
publicKeyFile.close()

# Export private key in PKCS#1, PEM encoded
privateKeyPkcsPem = privateKey.save_pkcs1().decode('utf8')
print(privateKeyPkcsPem)

privateKeyFile = open("private_key.pem", "w")
privateKeyFile.write(privateKeyPkcsPem)
privateKeyFile.close()



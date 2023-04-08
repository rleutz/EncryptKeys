# Pre-requisites
# pip install rsa (or install it into your virtual environment using your IDE)
import getpass

# Import modules
import rsa

# Generate new public and private RSA keys
(publicKey, privateKey) = rsa.newkeys(2048)

# Export public key in PKCS#1, PEM encoded
publicKeyPkcsPem = publicKey.save_pkcs1().decode('utf8')
print(publicKeyPkcsPem)

# Export private key in PKCS#1, PEM encoded
privateKeyPkcsPem = privateKey.save_pkcs1().decode('utf8')
print(privateKeyPkcsPem)

# Get the password from the user
#password = getpass.getpass(prompt='Password: ').encode('utf8')

# Encrypt a key
#encPass = rsa.encrypt(password, publicKey)

# Print out plain text and encrypted passwords
#print(password)
#print(encPass)



from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import serialization
import base64

# Base64-encoded ciphertext
base64_encoded_ciphertext = "EDDGxGCNH1NdNOaeAbEb2g=="

# Convert the base64-encoded ciphertext to bytes
ciphertext = base64.b64decode(base64_encoded_ciphertext)

# AES key and initialization vector (IV)
key = b"BPJSHealthkhaton2023"

# Create a Cipher object with AES encryption algorithm and CBC mode
cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())

# Create a decryption context
decryptor = cipher.decryptor()

# Decrypt the ciphertext
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Output the decrypted plaintext
print("Decrypted plaintext:", plaintext.decode('utf-8'))
Make sure you have the cryptography library installed. You can install it using pip:

Copy code
pip install cryptography
Replace "BPJSHealthkhaton2023" with the correct AES key used for encryption. This script assumes that AES-256 encryption was used with CFB mode; if different encryption parameters were used, you'll need to adjust the Cipher and modes accordingly.






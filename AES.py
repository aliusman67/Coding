from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode,b64decode
import hashlib

#secretkey harus meiliki panjang 16, 24 atau 32 byte
secret_key = hashlib.sha256(b'SecretKey1234567').digest()[:16]

#input data
data = str(input("Masukan Data: "))

#cek block size 
block_size = 16
padding_lenght = block_size - (len(data) % block_size)
char_padded = data + chr(padding_lenght) * padding_lenght

#Generate Random IV
iv = get_random_bytes(16)
chiper = AES.new(secret_key, AES.MODE_CBC, iv)
#enkrip data
chiper_text = chiper.encrypt(char_padded.encode('utf-8'))
#kombinasikan IV dan chipertext dan encode ke base64
chiper_text_iv = iv + chiper_text
chiper_text_base64 = b64encode(chiper_text_iv)

print("Chipertext: ",chiper_text_base64.decode('utf-8'))

#dekrip data dari chipertext
chiper_text_decode = b64decode(chiper_text_base64)
iv_dec = chiper_text_decode[:16]
chipertext_decode = chiper_text_decode[16:]

#membuat chiper object baru untuk dekripsi
dechiper = AES.new(secret_key, AES.MODE_CBC, iv_dec)

#melakukan dekripsi dan mengahpus padding PKCS
padding_data = dechiper.decrypt(chipertext_decode)
padding_panjang = padding_data[-1]
data = padding_data[:-padding_panjang].decode('utf-8')

print("Plaintext: ",data)
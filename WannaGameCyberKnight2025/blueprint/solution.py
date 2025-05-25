from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b"\x50\x45\x54\x45\x52\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0"
iv = b"\xe7\xf1\x70\x88\x28\xfe\x82\x93\xc2\xe7\xbb\xa0\xb2\xdb\xdc\x15"
ciphertext = open("user.json.enc", "rb").read()

cipher = AES.new(key, AES.MODE_CBC, iv)


try:
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(plaintext.decode())
except ValueError as e:
    print("Decryption failed:", str(e))


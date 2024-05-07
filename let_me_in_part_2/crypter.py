from Crypto.Util.number import GCD, inverse
from random import randint

def encrypt(message, a, b, n):
    encrypted = b''
    for char in message:
        encrypted += bytes([(a * char + b) % n])
    return encrypted

def decrypt(message, a, b, n):
    decrypted = b''
    inv = inverse(a, n)
    for char in message:
        decrypted += bytes([inv * (char - b) % n])
    return decrypted

n = 256
a = randint(2, n)
b = randint(2, n)
while GCD(a, n) != 1:
    a = randint(2, n)
message = b"H3xTEL{Affine_Cipher_1nTr0DUC3S_TH3_M0duL4R_1NV3RSE!!}"
encrypted = encrypt(message, a, b, n)
decrypted = decrypt(encrypted, a, b, n)
print(encrypted, "\n", decrypted)


from Crypto.Util.number import GCD, inverse

def decrypt_brute_force(encrypted, n):
    decrypted_messages = []
    for a in range(2, n):
        if GCD(a, n) == 1:
            inv = inverse(a, n)
            for b in range(2, n):
                decrypted = b''
                for char in encrypted:
                    decrypted += bytes([inv * (char - b) % n])
                decrypted_messages.append((decrypted, a, b))
    return decrypted_messages

encrypted_message = b"+^\xdbW\xa0\x8ff\x8f^w\xaah^\xaa\xacA\x1c\x1c\xaa7R7\xacA\xaa\x150W\xaa\xc70\xc7^\xaa+\xd3\xe2\xaa\x94\xd30\xaa\xee7A\xaa\xa5^7\xc7\xaa7\x8f\x8f\xaa\xd3y\xaaW+\xac~\xaa\xc7^\xee\xa5\x94\xf3W^\xc7\xaa~W0yy\xb1M\xee\x18"

n = 256

decrypted_messages = decrypt_brute_force(encrypted_message, n)

for decrypted, a, b in decrypted_messages:
    print("Clave probada (a, b):", a, ",", b)
    print("Mensaje descifrado: ", decrypted)
    print("\n")


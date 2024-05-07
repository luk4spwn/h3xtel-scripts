def decrypt(message, key):
    decrypted = b''
    for char in message:
        decrypted += bytes([(char - key) % 256])
    return decrypted

for i in range(0, 256):
    message = b"=(mI:ApA(iTB(T&C\x16\x16T?JHITA&@(TI](TB(B(T)AH%T<%%9T7GJI(;%G8&C<T9J9(0\x1er"
    key = i
    decrypted = decrypt(message, key)
    print(decrypted)

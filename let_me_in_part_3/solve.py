def decrypt(message, key):
    decrypted = b''
    for i in range(len(message)):
        decrypted += bytes([(message[i] - key[i % len(key)]) % 256 ])
    return decrypted

message = b"\xdb\\\xb1\xb5V<\xf5\x01Z\x9c\x94p;\xe8\xc3\xa0\xa7\xc0a\\\xae\xc4\x97\x8d\x94\x89D\xd9\xc7\x9d\xad\x95t;\xd9\xf5\x9bi\x82\x8e"
key = b"\x93)9a\x11\xf0z"
decrypted = decrypt(message, key)
print(decrypted)

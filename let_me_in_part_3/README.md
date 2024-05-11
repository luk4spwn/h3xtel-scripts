We are provided with the following statement.

```
Title: LET ME IN! - Part III

Description: What happens if we don't have the key in a Vigenere cipher?
Author: D-Cryp7

Encrypted flag: db5cb1b5563cf5015a9c94703be8c3a0a7c0615caec4978d948944d9c79dad95743bd9f59b69828e
Key Generation: key = os.urandom(7)
```
In the description we are given the hint that the flag was encrypted using the Vigenere cipher.

The Vigenère cipher is a cipher based on different series of characters or letters of the Caesar cipher forming these characters into a table, called the Vigenère table, which is used as a key. The Vigenère cipher is a polyalphabetic and substitution cipher. Here is a graphical example of how a text is encrypted using Vigenère.

![](https://i.imgur.com/gnSlwD8.png)

The key is used and repeated until the text to be encrypted is finished, basically this is how Vigenere works.

They also tell us that the key was created using os.urandom(7), this means that the key is 7 bytes long.

When I started this challenge the first thing I thought of was brute force, but brute forcing a 7 byte key would be a long, tedious job and require a lot of computational power. Doing some research I came across the known plaintext attack.

The known plaintext attack is that if you know some part of the ciphertext content it is possible to get the key, in this case I knew that the flag started with `H3xTEL{` so I could do the reverse operation to get it, so I programmed this script.

``` python
flag_in_bytes = bytes.fromhex("db5cb1b5563cf5015a9c94703be8c3a0a7c0615caec4978d948944d9c79dad95743bd9f59b69828e")

print(bytes([(flag_in_bytes[0] - ord("H")) % 256]))
print(bytes([(flag_in_bytes[1] - ord("3")) % 256]))
print(bytes([(flag_in_bytes[2] - ord("x")) % 256]))
print(bytes([(flag_in_bytes[3] - ord("T")) % 256]))
print(bytes([(flag_in_bytes[4] - ord("E")) % 256]))
print(bytes([(flag_in_bytes[5] - ord("L")) % 256]))
print(bytes([(flag_in_bytes[6] - ord("{")) % 256]))
```

When we execute it, it gives us the key.

![](https://i.imgur.com/Fggtge5.png)

`\x93)9a\x11\xf0z`

Then, I programmed a Python script that would decrypt the flag.

``` python
def decrypt(message, key):
    decrypted = b''
    for i in range(len(message)):
        decrypted += bytes([(message[i] - key[i % len(key)]) % 256 ])
    return decrypted

message = b"\xdb\\\xb1\xb5V<\xf5\x01Z\x9c\x94p;\xe8\xc3\xa0\xa7\xc0a\\\xae\xc4\x97\x8d\x94\x89D\xd9\xc7\x9d\xad\x95t;\xd9\xf5\x9bi\x82\x8e"
key = b"\x93)9a\x11\xf0z"
decrypted = decrypt(message, key)
print(decrypted)
```

> The flag in the script is in bytes, this was achieved with the bytes.fromhex('FLAG') method.

![](https://i.imgur.com/EluXamB.png)

`H3xTEL{n1c3_Kn0wn_Pl41nT3xT_4tt4cK_br0!}`

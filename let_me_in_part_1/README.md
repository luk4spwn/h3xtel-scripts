
We are provided with the following statement.

```
Description: What happens if we don't have the key in a Caesar cipher?
Author: D-Cryp7

Encrypted flag: b'=(mI:ApA(iTB(T&C\x16\x16T?JHITA&@(TI](TB(B(T)AH%T<%%9T7GJI(;%G8&C<T9J9(0\x1er'
```

It tells us what we can think of if we do not have the key in the cesar cipher, what I did was to mount the following script and do brute force.

``` python
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
```

First we create a function called decrypt that takes as arguments the message and a key, then a for loop where we implement the mathematical operation of the Caesar cipher.

![](https://i.imgur.com/aT8cHAk.png)

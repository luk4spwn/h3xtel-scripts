
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

``` python
for char in message:
        decrypted += bytes([(char - key) % 256])
    return decrypted
```

![](https://i.imgur.com/aT8cHAk.png)

> n is 256, this number refers to the characters available in the ASCII table.

And finally another for loop where I use Python's range() function to brute force the key.

``` python
for i in range(0, 256):
    message = b"=(mI:ApA(iTB(T&C\x16\x16T?JHITA&@(TI](TB(B(T)AH%T<%%9T7GJI(;%G8&C<T9J9(0\x1er"
    key = i
    decrypted = decrypt(message, key)
    print(decrypted)
```
We execute the script and using grep we can obtain the flag 🥳

![](https://i.imgur.com/YKdhGU5.png)

`H3xTEL{L3t_M3_1N!!_JUST_L1K3_Th3_M3M3_4LS0_G00D_BRUT3F0RC1NG_DUD3;)}`

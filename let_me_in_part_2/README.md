We are provided with the following statement.

```
Title: LET ME IN! - Part II

Description: What happens if we don't have the key in a Affine cipher?
Author: D-Cryp7

Encrypted flag: b'+^\xdbW\xa0\x8ff\x8f^w\xaah^\xaa\xacA\x1c\x1c\xaa7R7\xacA\xaa\x150W\xaa\xc70\xc7^\xaa+\xd3\xe2\xaa\x94\xd30\xaa\xee7A\xaa\xa5^7\xc7\xaa7\x8f\x8f\xaa\xd3y\xaaW+\xac~\xaa\xc7^\xee\xa5\x94\xf3W^\xc7\xaa~W0yy\xb1M\xee\x18'
```

They give us a hint that the flag is encrypted with the [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher).

The first thing to know is that the Affine cipher is a substitution cipher, meaning that each letter of the alphabet is assigned a numerical equivalent, using the following formula to be encrypted.

![](https://i.imgur.com/YY1bUJW.png)

> if you want to see a script that encrypts a string using the affine cipher you can click [here](https://gist.github.com/D-Cryp7/391f170e6e57b16b4750203e39379297#file-1-introduction-to-cryptography-ipynb)

Once I understood how the Affine cipher worked I programmed a python script that would screen print the possible keys with which the string was encrypted to see how to implement brute force.

``` python
from random import randint

while True:
    n = 256
    a = randint(2, n)
    b = randint(2, n)
    print(a, b)
```

When executing the script I could see that the numbers were between the range 2, and 256. With this I could program a brute force script.

``` python
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

```

From the Crypto.Util.number library, we import GCD (to calculate the greatest common divisor) and inverse.

``` python
from Crypto.Util.number import GCD, inverse
```
We then create a function called decrypted_brute_force which using a for creates a variable called a that iterates over the range 2, `n`. This function calculates if the greatest common divisor between a and n is equal to 1 to continue with the operations.

``` python
inv = inverse(a, n)
            for b in range(2, n):
                decrypted = b''
                for char in encrypted:
                    decrypted += bytes([inv * (char - b) % n])
                decrypted_messages.append((decrypted, a, b))
```

We run the script and using grep we can get the flag.

![](https://i.imgur.com/Yf3KhUA.png)

The keys used to encrypt the string were `217` and `35`.

`H3xTEL{L3t_M3_1N!!_4G41N_BUT_DUD3_H0W_Y0U_C4N_R34D_4LL_0F_TH1S_D3CRYPT3D_STUFF>:C}`

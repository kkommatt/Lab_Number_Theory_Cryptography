import random
from sympy import isprime, mod_inverse
from math import gcd


def generate_keypair(keysize):
    p = q = 1
    while not isprime(p):
        p = random.randrange(2 ** (keysize - 1), 2 ** keysize)
    while not isprime(q) or p == q:
        q = random.randrange(2 ** (keysize - 1), 2 ** keysize)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

def rsa():
    print("Rivest–Shamir–Adleman Crypto System")

    try:
        keysize = int(input("Enter the keysize: "))
        public, private = generate_keypair(keysize)

        print("Public key: ", public)
        print("Private key: ", private)

        message = input("Enter message to encrypt: ")
        encrypted_msg = encrypt(public, message)
        print("Encrypted message: ", encrypted_msg)

        decrypted_msg = decrypt(private, encrypted_msg)
        print("Decrypted message: ", decrypted_msg)

    except Exception as x:
        print(f"{x}")

import os, sys
from AESfile import AESCipher
from DESfile import DESCipher
from RC4file import RC4Cipher

if __name__ == '__main__':
    a = AESCipher("Vikas")
    cipher = a.encrypt(a)
    message = a.decrypt(cipher)   
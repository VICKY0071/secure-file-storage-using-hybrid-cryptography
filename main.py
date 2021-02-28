import os, sys
from AESfile import AESCipher
from DESfile import DESCipher
from RC4file import RC4Cipher
from videotobase64 import mp4ToBase64

def encrypt_text(file, key):
    ss = file.read()
    s1 = ss[0:len(ss) // 2]
    s2 = ss[len(ss) // 2:]
    a = AESCipher(key)
    b = DESCipher(key)
    t1 = a.encrypt(s1)
    t2 = b.encrypt(s2)
    file1 = open('files\\file1.txt', 'w')
    file2 = open('files\\file2.txt', 'w')
    file1.write(t1)
    file2.write(t2)

def decrypt_text(file1, file2, key):
    a = AESCipher(key)
    b = DESCipher(key)
    return a.decrypt(file1.read()) + b.decrypt(file2.read())

if __name__ == '__main__':
    print(decrypt_text(open('files\\file1.txt', 'r'), open('files\\file2.txt', 'r'), 'password'))
import os, sys
from AESfile import AESCipher
from DESfile import DESCipher
from RC4file import RC4Cipher
from videotobase64 import mp4ToBase64

def encrypt_text(file):
    ss = file.read()
    s1 = ss[0:len(ss) // 2]
    s2 = ss[len(ss) // 2:]
    print(s1)
    a = AESCipher("password")
    b = DESCipher("password")
    t1 = a.encrypt(s1)
    t2 = b.encrypt(s2)
    file1 = open('files/file1.txt', 'w')
    file2 = open('files/file2.txt', 'w')
    file1.write(t1)
    file2.write(t2)


if __name__ == '__main__':)
import os, sys
from AESfile import AESCipher
from DESfile import DESCipher
# from RC4file import RC4Cipher
from videotobase64 import mp4ToBase64
from base64 import b64encode, b64decode

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

def encrypt_video(file, key):
    x = file.read()
    hex_str = x.hex()
    a = AESCipher(key)
    b = DESCipher(key)
    p1 = a.encrypt(hex_str[0:len(hex_str) // 2])
    p2 = b.encrypt(hex_str[len(hex_str) // 2:])
    f1 = open('files/part1.txt', 'w')
    f2 = open('files/part2.txt', 'w')
    f1.write(p1)
    f2.write(p2)
    # f = open('files/output.mp4', 'wb')
    # f.write(bytes.fromhex(s))


if __name__ == '__main__':
    encrypt_video(open('video file.mp4', 'rb'), 'password')    

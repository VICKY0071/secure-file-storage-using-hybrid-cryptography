from AESfile import AESCipher
from DESfile import DESCipher

p2 = open('part2.txt', 'r').read()

p1 = open('part1.txt', 'r').read() 

a = AESCipher('password')
b = DESCipher('password')

f = open('output.mp4', 'wb')
f.write(bytes.fromhex(a.decrypt(p1) + b.decrypt(p2)))
class RC4Cipher:
	def __init__(self, key):
		self.key = [ord(c) for c in key]

	def KSA(self):
	    keylength = len(self.key)

	    S = [_ for _ in range(256)]

	    j = 0
	    for i in range(256):
	        j = (j + S[i] + self.key[i % keylength]) % 256
	        S[i], S[j] = S[j], S[i]  # swap

	    return S

	def PRGA(self, S):
	    i = 0
	    j = 0
	    while True:
	        i = (i + 1) % 256
	        j = (j + S[i]) % 256
	        S[i], S[j] = S[j], S[i]  # swap

	        K = S[(S[i] + S[j]) % 256]
	        yield K
	
	def encrypt(self, plaintext, a):
		l = a.KSA()
		z = a.PRGA(l)
		cipher = ""
		for i in plaintext :
			cipher += str("%02X" % (ord(i) ^ z.__next__()))
		return cipher

	# decryption is not working still have to figure that out.

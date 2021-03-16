import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
hash = 'SHA-256'

class RSACipher:
	def newkeys(self, keysize):
		random_generator = Random.new().read
		key = RSA.generate(keysize, random_generator)
		private, public = key, key.publickey()
		return public, private

	def importKey(self, externkey):
		return RSA.importKey(externKey)

	def getPublicKey(self, priv_key):
		return priv_key.publickey()

	def encrypt(self, message, pub_key):
		cipher = PKCS1_OAEP.new(pub_key)
		return cipher.encrypt(message)

	def decrypt(self, ciphertext, priv_key):
	   cipher = PKCS1_OAEP.new(priv_key)
	   return cipher.decrypt(ciphertext)

	def sign(self, message, priv_key, hashAlg = "SHA-256"):
	   global hash
	   hash = hashAlg
	   signer = PKCS1_v1_5.new(priv_key)
	   if (hash == "SHA-512"):
	      digest = SHA512.new()
	   elif (hash == "SHA-384"):
	      digest = SHA384.new()
	   elif (hash == "SHA-256"):
	      digest = SHA256.new()
	   elif (hash == "SHA-1"):
	      digest = SHA.new()
	   else:
	      digest = MD5.new()
	   digest.update(message)
	   return signer.sign(digest)

	def verify(self, message, signature, pub_key):
	   signer = PKCS1_v1_5.new(pub_key)
	   if (hash == "SHA-512"):
	      digest = SHA512.new()
	   elif (hash == "SHA-384"):
	      digest = SHA384.new()
	   elif (hash == "SHA-256"):
	      digest = SHA256.new()
	   elif (hash == "SHA-1"):
	      digest = SHA.new()
	   else:
	      digest = MD5.new()
	   digest.update(message)
	   return signer.verify(digest, signature)

if __name__ == '__main__':
	a = RSACipher()
import base64

class mp4ToBase64:
	def __init__(self, file):
		self.text = base64.b64encode(file.read())

	def to_64(self):
		return self.text

	def to_mp4(self, t):
		file = open('output_video.mp4', 'wb')
		file.write(base64.b64decode(t))
		file.close()

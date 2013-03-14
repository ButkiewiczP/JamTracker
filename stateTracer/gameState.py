class gameState:
	def __init__(self, filename, findValue):
		self.targetValue = findValue
		self.filename = filename
		self.lineDict = {}
		self.offsets = []
		self.stateReader = stateReader(filename)
		#self.readStateForValue(self.targetValue)
		print 'State File: ' + str(self.filename)

		
	def readStateForValue(self, targetVal):
		self.stateReader.directCompareToState(targetVal, 1, 0)

	def printDecompressedState(self):
		decompressedString = self.stateReader.decompressedStateString()
		print decompressedString

	def printStreams(self):
		count = 0
		for i, data in self.stateReader.zipstreams(self.filename):
			print (i, len(data))
			
			saveFileName = self.filename + "dcm"
			fp = open(saveFileName, 'wb')
			fp.write(data)

	def debug(self):
		hexObj = hexObject(self.targetValue)
		hexObj.debug()
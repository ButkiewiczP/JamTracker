import sys
import zlib

class stateManager:
	def __init__(self):
		self.SS_MSB_FIRST_FLAG = 0x02
		self.HEADER_SIZE = 32
		self.BYTES_TO_READ = 1
		self.COMPRESSION_LEVEL = 6

	def offsetsForValue(self, data, targetVal, DEBUG=1, offset=0):
		hexObj = hexObject(targetVal)
		headerBytes = ""
		headerText = ""
		bytesRead = 0
		offsets = []

		with open(self.stateFilename, "rb") as fp:
			fp.seek(offset)
			while True:
				piece = data[lastOffset:lastOffset+self.BYTES_TO_READ]

				if piece == "":
					break # end of file
				
				hexLine = binascii.hexlify(piece).upper()
				if hexObj.compare(hexLine) is True:
					offsets.append(bytesRead + offset) 
	
				bytesRead = bytesRead + self.BYTES_TO_READ
				lastOffset = bytesRead + offset
				#if bytesRead >= 1979701:
				#	break
		fp.close()

		return offsets

	def decompressState(self, fileP):
		headerData = fileP.read(self.HEADER_SIZE)
		sys.stderr.write("State Header: " + headerData + "\n")

		for offset, data in self.zipstreams(fileP):
			return headerData, data

	def zipstreams(self, fileP):
		data = fileP.read()
		i = 0
		while i < len(data):
			try:
				zo = zlib.decompressobj()
				yield i, zo.decompress(data[i:])
				i += len(data[i:]) - len(zo.unused_data)
			except zlib.error:
				i += 1

	def compressState(self, fileP):
		sys.stderr.write("Compress State\n")
		return zlib.compress(fileP.read(), self.COMPRESSION_LEVEL)

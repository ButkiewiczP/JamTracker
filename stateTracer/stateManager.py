import binascii
import sys
import zlib

class stateManager:
	def __init__(self):
		self.SS_MSB_FIRST_FLAG = 0x02
		self.HEADER_SIZE = 32
		self.BYTES_TO_READ = 1
		self.COMPRESSION_LEVEL = 6

	def offsetsForValue(self, fileP, targetVal, offset=0):
		hexTarget = hex(int(targetVal))[2:]

		if len(hexTarget) < 2:
			hexTarget = "0" + hexTarget	# make sure byte we're looking for is atleast 2 bytes

		bytesRead = 0
		offsets = []
		lastOffset = offset
		index = 0

		with open(fileP, "rb") as fp:
			fp.seek(offset, 0)
			hexDataToSearch = binascii.hexlify(fp.read())

			while index < len(hexDataToSearch):
				index = hexDataToSearch.find(hexTarget, index)
				if index == -1:
					break

				offsets.append(index)
				index += len(hexTarget)

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

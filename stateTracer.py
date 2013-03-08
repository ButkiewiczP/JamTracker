#!/usr/bin/python
import os
import sys
import binascii

class hexObject:
	def __init__(self, intValue):
		self.intVal = intValue
		self.hex = self.hexValueForMachineValue(self.intVal)
		self.revHex = self.reverseHexValueForMachineValue(self.intVal)
		self.revBHex = self.reverseByteHexValueForMachineValue(self.intVal)
		self.iHex = self.inverseHexValueForMachineValue(self.intVal)
		self.irbHex = self.reverseByteInverseHexValueForMachineValue(self.intVal)
		self.irHex = self.reverseInverseHexValueForMachineValue(self.intVal)

	def debug(self):
		print "############ DEBUG OUTPUT ############"
		print "Target Value => " + str(self.intVal)
		print "hexValueForMachineValue => " + str(self.hexValueForMachineValue(self.intVal))
		print "reverseHexValueForMachineValue => " + str(self.reverseHexValueForMachineValue(self.intVal))
		print "reverseByteHexValueForMachineValue => " + str(self.reverseByteHexValueForMachineValue(self.intVal))
		print "inverseHexValueForMachineValue => " + str(self.inverseHexValueForMachineValue(self.intVal))
		print "reverseByteInverseHexValueForMachineValue => " + str(self.reverseByteInverseHexValueForMachineValue(self.intVal))
		print "reverseInverseHexValueForMachineValue => " + str(self.reverseInverseHexValueForMachineValue(self.intVal))

	def compare(self, byte):
		byte = byte.upper()

		if str(self.hex).upper() in byte:
			return True
		elif str(self.revHex).upper() in byte:
			return True
		elif str(self.revBHex).upper() in byte:
			return True
		elif str(self.iHex).upper() in byte:
			return True
		elif str(self.irbHex).upper() in byte:
			return True
		elif str(self.irHex).upper() in byte:
			return True

		return False

	def hexValueForMachineValue(self,intValue):
		hexVal = str(hex(intValue))[2:]
		pad = 4 - len(hexVal) 

		i = 0
		while i < pad:
			hexVal = str(0) + hexVal
			i = i + 1

		return hexVal

	def reverseByteHexValueForMachineValue(self,intValue):
		hex = str(self.hexValueForMachineValue(intValue))
		hexbyte1 = hex[0] + hex[1]
		hexbyte2 = hex[2] + hex[3]
		newhex = hexbyte2 + hexbyte1
		return newhex

	def reverseHexValueForMachineValue(self,intValue):
		hex = str(self.hexValueForMachineValue(intValue))
		newhex = hex[3] + hex[2] + hex[1] + hex[0]
		return newhex

	def inverseHexValueForMachineValue(self,intValue):
		hexa = str(self.hexValueForMachineValue(intValue))
		hexstr = hex(int(hexa, 16) ^ int(str("FFFF"), 16))
		return str(hexstr)[2:]

	def reverseByteInverseHexValueForMachineValue(self,intValue):
		hexa = self.inverseHexValueForMachineValue(intValue)
		hexbyte1 = hexa[0] + hexa[1]
		hexbyte2 = hexa[2] + hexa[3]
		newhex = hexbyte2 + hexbyte1
		return newhex

	def reverseInverseHexValueForMachineValue(self,intValue):
		hex = self.inverseHexValueForMachineValue(intValue)
		newhex = hex[3] + hex[2] + hex[1] + hex[0]
		return newhex


class state:
	def __init__(self, filename, findValue):
		self.targetValue = findValue
		self.filename = filename
		self.lineDict = {}
		self.offsets = []
		self.readStateForValue(self.targetValue)
		print 'State Constructed'
		print 'State File: ' + str(self.filename)
		print 'Lines Read: ' + str(len(self.lineDict))
		print 'Matched Offsets: ' + str(len(self.offsets))
		
	def readStateForValue(self, targetVal):
		hexObj = hexObject(targetVal)
		headerBytes = ""
		headerText = ""
		i = 1
		with open(self.filename, "rb") as fp:
			while True:
				piece = fp.read(2)

				if piece == "":
					break # end of file
				
				hexLine = binascii.hexlify(piece).upper()
				if hexObj.compare(hexLine) is True:
					self.lineDict[str(i)] = hexLine #line.upper().replace(" ", "")
					self.offsets.append(i) 

				# Print out the header of the state
				if i < 10:
					headerBytes = headerBytes + hexLine
					headerText = headerText + piece
				elif i == 10:
					print "Rom Header: "
					print headerBytes
					print headerText
		

				i = i + 1
		fp.close()
		#print self.offsets

	def debug(self):
		hexObj = hexObject(self.targetValue)
		hexObj.debug()



#######################################################################################
#######################################################################################
##################################### Start main ######################################
#######################################################################################
#######################################################################################

if len(sys.argv) > 2:
	if sys.argv[1] == "-h" and sys.argv[2]:
		hexObj = hexObject(int(sys.argv[2]))
		hexObj.debug()
		exit()
	else:
		print "Usage: python stateTracer"
		print "Usage 2: python stateTracer -h [intValue]    --- Use this to convert an int to multiple hex forms"
		exit()



states = []	# Holds on to the state objects to compare their sets of matching lines
ans = ""	# Holds on to users answer whether to keep searching files
while ans is not "n":

	#Read in file, and integer to look for
	fileN = raw_input("Enter Save-State Filename To Analyze: ") 
	iVal = raw_input("Integer Value To Find: ") 

	#Create state
	newState = state(str(fileN), int(iVal)) 
	states.append(newState)
	newSet = set(newState.offsets)
	newState.debug()
	ans = raw_input("Read another state file? (y/n)")

setOfOffsets = set()
for s in states:
	if len(setOfOffsets) == 0:
		setOfOffsets = set(s.offsets)
	else:
		setOfOffsets = setOfOffsets.intersection(set(s.offsets))

print setOfOffsets
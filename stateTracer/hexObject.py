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
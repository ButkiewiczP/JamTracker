#!/usr/bin/python
import argparse
import binascii
import hexObject
import os
import gameState
import stat
import stateManager
import sys

# Global Variables
# Default files to read/write to is the system IO.
#   Allows piping and redirecting into the script
inputFile = sys.stdin
outputFile = sys.stdout
logFile = sys.stderr
APP_NAME = 'stateTracer'
VERSION_STRING = '0.5.0'

# Global Helper Functions
# Log function. Simplifies writing to the log.
def log(logString):
    try:
        logFile.write(logString + "\n")
    except IOError:
        pass

# Output function. Writes to the outfile
def output(outString):
    try:
        outputFile.write(outString)
    except IOError:
        pass

# Create parser to handle arguments passed into the script at run time
parser = argparse.ArgumentParser(description='Process and search MAME save states')
parser.add_argument('-x', '--hex', help='Encode string to hex', action='store_true', default=False, dest='hex', required=False)
parser.add_argument('-p', '--compare', help='Compare decompressed states for changes in hex', action='store_true', default=False, dest='compare', required=False)
parser.add_argument('-c', '--compress', help='Compress a state for reuse', action='store_true', default=False, dest='compress', required=False)
parser.add_argument('-d', '--decompress', help='Decompress a save state file', action='store_true', default=False, dest='decompress', required=False)
parser.add_argument('-D', '--Debug', help='Set debug mode to true', action='store_true', dest='debugMode', required=False)
parser.add_argument('-s', "--source", dest='input', help="Source file/string (Or use piping/redirect)", default=None, required=False)
parser.add_argument('-o', "--dest", dest='output', help="Destination file/string (Or use piping/redirect)", default=None, required=False)
parser.add_argument('-l', "--log", dest='log', help="File to write the log to (Default is STDERR)", default=None, required=False)
parser.add_argument('-v', '--version', help='Outputs the script version to STDOUT', action='store_true', default=False, dest='version', required=False)
args = vars(parser.parse_args())

###################################################################
# Option: -v
# Outputs the script's version to STDOUT. Cancels all other options
###################################################################
if args['version']:
    output(APP_NAME + "-" + VERSION_STRING + "\n")
    exit()

#################################################################
# Option: -l <file>
# Option: -D
# Both options open stderr. -l will write to a file. -D writes
#   to console. By default, stderr is pointed at /dev/null
#################################################################
if not (args['debugMode'] or args['log']):
    logFile = open('/dev/null', 'w')
else:
    if args['log']:
        try:
            tryLogFile = open(args['log'], 'w')
            logFile = tryLogFile
        except IOError:
            logFile.write("Error opening file for logging: " + str(args['log']))

    if args['debugMode']:
        log("Debug Mode Enabled\n")    

# After directing the logfile, start writing.
log("Program Arguments: " + str(args))

###############################
# Option: -s <file>
# Handle File Input / stdin
#
###############################
if args['input'] is not None:
    try:
        if args['hex']:
            inputFile = open(str(args['input']), 'r')
        else:
            inputFile = open(str(args['input']), 'rb')
    except IOError:
        logFile.write("No source file exists, using stdin")
else:
    logFile.write("No source file exists, using stdin")

###############################
# Option: -o <file>
# Handle File Output / stdout
#
###############################
if args['output'] is not None:
    try:
        log("Destination Exists. Redirecting output to file")
        outputFile = open(str(args['output']), 'wb')
    except IOError:
        log("No destination file exists, using stdout")
else:
    log("No destination file exists, using stdout")


#######################
# Option: -x
# Perform ASCII to Hex
#
#######################
if args['hex'] is True:
    if (args['compress'] or args['decompress']):
        log("Error: OHex mode and compression mode can't be used together")
        exit()
    else:
        log("Converting ascii to hex")
        fp = inputFile
        convertedData = binascii.hexlify(fp.read())
        output(binascii.hexlify(convertedData))


###########################################################
# Option: -d
# Decompress MAME save state file
# MAME uses zlib to compress states before writing to disk 
###########################################################
if args['decompress'] is True:
    log("Decompressing save state")
    stateMan = stateManager.stateManager()
    header, saveData = stateMan.decompressState(inputFile)
    output(saveData)
    outFileName = outputFile.name + ".hdr"

    with open(outFileName, 'wb') as fp:
        fp.write(header)
    log("Decompressed state successfully")


#####################################################################
# Option: -c
# Compress a previously decompressed save back into a usable state
#   Adds header data, compresses save data, and writes to file
# TODO!
#####################################################################
if args['compress'] is True:
    logFile.write("Attempting to compress " + inputFile.name)
    stateMan = stateManager.stateManager()
    stateFileName = inputFile.name
    headerFileName = inputFile.name + ".hdr"
    with open(headerFileName, 'rb') as headerP:
        output(headerP.read())
    headerP.close()
    output(stateMan.compressState(inputFile))
    log("Compressed save state successfully")

#####################################################################
# Option: -c
# Compress a previously decompressed save back into a usable state
#   Adds header data, compresses save data, and writes to file
# TODO!
#####################################################################
if args['compare']:
    pass
    states = []    # Holds on to the state objects to compare their sets of matching lines
    ans = ""    # Holds on to users answer whether to keep searching files
    while ans is not "n":

        #Read in file, and integer to look for
        fileN = raw_input("Enter Save-State Filename To Analyze: ")
        iVal = raw_input("Integer Value To Find: ")

        #Create state
        newState = gameState(str(fileN), iVal) #int(iVal)) 
        newSet = set(newState.stateReader.directCompareToState(int(iVal)))
        states.append(newSet)
        newState.debug()

        ans = raw_input("Read another state file? (y/n)")

    setOfOffsets = set()
    for s in states:
        if len(setOfOffsets) == 0:
            setOfOffsets = set(s)
        else:
            setOfOffsets = setOfOffsets.intersection(set(s))

    print setOfOffsets

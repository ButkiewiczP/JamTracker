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
APP_NAME = 'stateTracer'
VERSION_STRING = '0.6.3'
ARG_HEX_DEST = "hex"
ARG_HEX_DEST

#I/O Vars
inputFile = sys.stdin
outputFile = sys.stdout
logFile = sys.stderr
headerFile = None

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
#Required Arguments
parser.add_argument('-x', '--hex', help='Encode string to hex', action='store_true', default=False, dest='hex', required=False)
parser.add_argument('-xb', '--hexb', help='Encode binary string to hex', action='store_true', default=False, dest='hexb', required=False)
parser.add_argument('-p', '--compare', help='Add file to collection of files to compare', action='append', default=[], dest='compare', required=False)
parser.add_argument('-c', '--compress', help='Compress a state for reuse', action='store_true', default=False, dest='compress', required=False)
parser.add_argument('-d', '--decompress', help='Decompress a save state file', action='store_true', default=False, dest='decompress', required=False)
#I/O Arguments
parser.add_argument('-s', "--source", dest='input', help="Source file/string (Or use piping/redirect)", default=None, required=False)
parser.add_argument('-o', "--dest", dest='output', help="Destination file/string (Or use piping/redirect)", default=None, required=False)
#Debug Options
parser.add_argument('-D', '--Debug', help='Enable log writing to console', action='store_true', dest='debugMode', required=False)
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
            log("Error opening file for logging: " + str(args['log']))

    if args['debugMode']:
        log("Debug Mode Enabled")    

log("Program Arguments: " + str(args))

###############################
# Option: -s <file>
# Handle File Input / stdin
#
###############################
if args['input'] is not None:
    inputFile = open(str(args['input']), 'rb')
else:
    log("No source file exists, using stdin")

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
# Option: -xb
# Perform ASCII to Hex
#
#######################
if args['hexb'] is True:
        fp = inputFile
        convertedData = binascii.hexlify(fp.read().rstrip())
        output(binascii.hexlify(convertedData))
        log("Converted Binary to Hex")

if args['hex'] is True:
        data = inputFile.read().rstrip()
        if data.isdigit() is True:
            outputFile.write(str(hex(int(data))))
        else:
            for b in data:
                if b is not "\n":
                    outputFile.write(hex(int(str(ord(b))))) 
        output("\n")
        log("Converted ASCII to Hex")


###########################################################
# Option: -d
# Decompress MAME save state file
# MAME uses zlib to compress states before writing to disk 
###########################################################
if args['decompress'] is True:
    log("Decompressing save state")
    stateMan = stateManager.stateManager()
    header, saveData = stateMan.decompressState(inputFile)
    
    with open(outputFile.name + ".hdr", 'wb') as fp:
        fp.write(header) # Writes header to separate file

    output(saveData)
    log("Decompressed state successfully")

#####################################################################
# Option: -c
# Compress a previously decompressed save back into a usable state
#   Adds header data, compresses save data, and writes to file
# 
#####################################################################
if args['compress'] is True:
    log("Attempting to compress " + inputFile.name)
    stateMan = stateManager.stateManager()

    headerFileName = inputFile.name + ".hdr"
    with open(headerFileName, 'rb') as headerP:
        output(headerP.read())
    headerP.close()

    output(stateMan.compressState(inputFile))
    log("Compressed save state successfully")

#####################################################################
# Option: -p <file1> -p <file2>
# Compare multiple files for matching offset changes
#   
#####################################################################
if args['compare']:
    offsetArray = []
    log("Attempting to compare " + str(len(args['compare'])) + " files")
    for f in args['compare']:
        stateMan = stateManager.stateManager()
        iVal = raw_input("Integer Value To Find for file <" + f + ">: ")
        ofsts = stateMan.offsetsForValue(f, iVal)
        offsetArray.append(ofsts)

    log("Attempting to compare " + str(len(args['compare'])) + " sets")
    setOfOffsets = set()
    for s in offsetArray:
        if len(setOfOffsets) == 0:
            setOfOffsets = set(s)
        else:
            setOfOffsets &= set(s)

    log(str(len(setOfOffsets)) + " offsets matched")
    for i in setOfOffsets:
        output(str(hex(int(i)) + "\n"))

log("Finished")

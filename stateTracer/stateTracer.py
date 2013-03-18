#!/usr/bin/python
import argparse
import binascii
import hexObject
import os
import stat
import stateManager
import sys

# Global Variables
APP_NAME = 'stateTracer'
VERSION_STRING = '0.6.3'
ARG_HEX_DEST = "hex"
ARG_HEXB_DEST = "hexb"
ARG_COMPARE_DEST = "compare"
ARG_COMPRESS_DEST = "compress"
ARG_DECOMPRESS_DEST = "decompress"
ARG_SOURCE_DEST = "input"
ARG_OUTPUT_DEST = "output"
ARG_DEBUG_DEST = "debugMode"
ARG_LOG_DEST = "log"
ARG_VERSION_DEST = "version"

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
parser.add_argument('-x', '--hex', help='Encode string to hex', action='store_true', default=False, dest=ARG_HEX_DEST, required=False)
parser.add_argument('-xb', '--hexb', help='Encode binary string to hex', action='store_true', default=False, dest=ARG_HEXB_DEST, required=False)
parser.add_argument('-p', '--compare', help='Add file to collection of files to compare', action='append', default=[], dest=ARG_COMPARE_DEST, required=False)
parser.add_argument('-c', '--compress', help='Compress a state for reuse', action='store_true', default=False, dest=ARG_COMPRESS_DEST, required=False)
parser.add_argument('-d', '--decompress', help='Decompress a save state file', action='store_true', default=False, dest=ARG_DECOMPRESS_DEST, required=False)
#I/O Arguments
parser.add_argument('-s', "--source", dest=ARG_SOURCE_DEST, help="Source file/string (Or use piping/redirect)", default=None, required=False)
parser.add_argument('-o', "--dest", dest=ARG_OUTPUT_DEST, help="Destination file/string (Or use piping/redirect)", default=None, required=False)
#Debug Options
parser.add_argument('-D', '--Debug', help='Enable log writing to console', action='store_true', dest=ARG_DEBUG_DEST, required=False)
parser.add_argument('-l', "--log", dest=ARG_LOG_DEST, help="File to write the log to (Default is STDERR)", default=None, required=False)
parser.add_argument('-v', '--version', help='Outputs the script version to STDOUT', action='store_true', default=False, dest=ARG_VERSION_DEST, required=False)
args = vars(parser.parse_args())

###################################################################
# Option: -v
# Outputs the script's version to STDOUT. Cancels all other options
###################################################################
if args[ARG_VERSION_DEST]:
    output(APP_NAME + "-" + VERSION_STRING + "\n")
    exit()

#################################################################
# Option: -l <file>
# Option: -D
# Both options open stderr. -l will write to a file. -D writes
#   to console. By default, stderr is pointed at /dev/null
#################################################################
if not (args[ARG_DEBUG_DEST] or args[ARG_LOG_DEST]):
    logFile = open('/dev/null', 'w')
else:
    if args[ARG_LOG_DEST]:
        try:
            tryLogFile = open(args[ARG_LOG_DEST], 'w')
            logFile = tryLogFile
        except IOError:
            log("Error opening file for logging: " + str(args[ARG_LOG_DEST]))

    if args[ARG_DEBUG_DEST]:
        log("Debug Mode Enabled")    

log("Program Arguments: " + str(args))

###############################
# Option: -s <file>
# Handle File Input / stdin
#
###############################
if args[ARG_SOURCE_DEST] is not None:
    inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')
else:
    log("No source file exists, using stdin")

###############################
# Option: -o <file>
# Handle File Output / stdout
#
###############################
if args[ARG_OUTPUT_DEST] is not None:
    try:
        log("Destination Exists. Redirecting output to file")
        outputFile = open(str(args[ARG_OUTPUT_DEST]), 'wb')
    except IOError:
        log("No destination file exists, using stdout")
else:
    log("No destination file exists, using stdout")

#######################
# Option: -xb
# Perform Binary to Hex
#
#######################
if args[ARG_HEXB_DEST] is True:
        fp = inputFile
        convertedData = binascii.hexlify(fp.read().rstrip())
        output(binascii.hexlify(convertedData))
        log("Converted Binary to Hex")

#######################
# Option: -x
# Perform ASCII to Hex
#
#######################
if args[ARG_HEX_DEST] is True:
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
if args[ARG_DECOMPRESS_DEST] is True:
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
if args[ARG_COMPRESS_DEST] is True:
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
if args[ARG_COMPARE_DEST]:
    offsetArray = []
    log("Attempting to compare " + str(len(args[ARG_COMPARE_DEST])) + " files")
    for f in args[ARG_COMPARE_DEST]:
        stateMan = stateManager.stateManager()
        iVal = raw_input("Integer Value To Find for file <" + f + ">: ")
        ofsts = stateMan.offsetsForValue(f, iVal)
        offsetArray.append(ofsts)

    log("Attempting to compare " + str(len(args[ARG_COMPARE_DEST])) + " sets")
    setOfOffsets = set()
    for s in offsetArray:
        if len(setOfOffsets) == 0:
            setOfOffsets = set(s)
        else:
            setOfOffsets &= set(s)

    log(str(len(setOfOffsets)) + " offsets matched")
    for i in setOfOffsets:
        output(str(hex(int(i))) + "\n")

log("Finished")

#!/usr/bin/python
import argparse
import logging
import JamReader
import JamGame
import JamServer
import offsets
import os
import stat
import stateTracer.stateManager
import sys
import time
import utilities

# Global Variables
APP_NAME = 'JamTracker'
VERSION_STRING = '0.9.9'
ARG_SOURCE_DEST = "source"
ARG_DEBUG_DEST = "debugMode"
ARG_LOG_DEST = "log"
ARG_VERSION_DEST = "version"
#I/O
inputFile = ""
#setup logging
log = logging.getLogger('JamTracker')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)

# Create parser to handle arguments passed into the script at run time
parser = argparse.ArgumentParser(description='Monitor a state file to dump stats')
parser.add_argument('-i', "--source", dest=ARG_SOURCE_DEST, help="Source file/string (Or use piping/redirect)", default=None, required=False)
parser.add_argument('-D', '--Debug', help='Enable log writing to console', action='store_true', dest=ARG_DEBUG_DEST, required=False)
parser.add_argument('-l', "--log", dest=ARG_LOG_DEST, help="File to write the log to (Default is STDERR)", default=None, required=False)
parser.add_argument('-v', '--version', help='Outputs the script version to STDOUT', action='store_true', default=False, dest=ARG_VERSION_DEST, required=False)
args = vars(parser.parse_args())

################################
# Option: -v
# Outputs the script's version
################################
if args[ARG_VERSION_DEST]:
    print APP_NAME + "-" + VERSION_STRING
    exit()

#################################################################
# Option: -l <file>
# Option: -D
# Both options open stderr. -l will write to a file. -D writes
#   to console. By default, stderr is pointed at /dev/null
#################################################################
if not (args[ARG_DEBUG_DEST] or args[ARG_LOG_DEST]):
    logFile = open('/dev/null', 'w')    # Needs to be modified for windows
else:
    if args[ARG_DEBUG_DEST]:
        log.info("Debug Mode Enabled")
        #TODO set handler stream to output everything

    if args[ARG_LOG_DEST]:
        try:    # TODO set handler stream to write to file
            tryLogFile = open(args[ARG_LOG_DEST], 'w')
            logFile = tryLogFile
        except IOError:
            log("Error opening file for logging: " + str(args[ARG_LOG_DEST]))


###############################
# Option: -s <file>
# Handle File Input / stdin
#
###############################
if args[ARG_SOURCE_DEST] is not None:
    inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')
else:
    log.critical("No save file specified")
    exit()

log.debug("Arguments: " + str(args))
##################################################################################

jReader = JamReader.JamReader(inputFile, logging.debug)
jServer = JamServer.JamServer()

utilities.lowerPriority()

while (1):
  inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')
  jReader = JamReader.JamReader(inputFile)
  jGame = jReader.readGameObject() 
  print jGame.description()
  inputFile.close()
  if args[ARG_DEBUG_DEST]:
    log.debug("Debug mode only runs once")
    exit();
  else:
    time.sleep(10)

log.warn("Script reached the end. Something probably went wrong")
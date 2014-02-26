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
import mame

import win32api, win32gui, win32con, win32file, time 

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
    logFile = open('NUL', 'w')
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
utilities.lowerPriority()   # Lower the priority of this script
inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')  # Open the file
getSaveStateMsg = win32api.RegisterWindowMessage(mame.MAME_MESSAGE_GET_SAVE_STATE)
didSaveStateMsg = win32api.RegisterWindowMessage(mame.MAME_MESSAGE_DID_SAVE_STATE)
lastSavedGame = ""

# Start running the main loop
while (1):
  log.debug("Running Main Loop")

  # Make sure we have a mame window and we're playing NBA Jam TE
  mameWindow = win32gui.FindWindowEx(0,0,0, mame.MAME_WINDOW_NAME)
  jamWindow = win32gui.FindWindowEx(0,0,0, mame.MAME_WINDOW_NAME_JAM)
  if mameWindow == 0:
    log.debug("Mame window not found. Sleeping %d seconds", mame.MAME_NOT_FOUND_SLEEP_INTERVAL)
    time.sleep(mame.MAME_NOT_FOUND_SLEEP_INTERVAL)
    continue
  if jamWindow == 0:
    log.debug("NBA Jam window not found. Sleeping %d seconds", mame.MAME_NOT_FOUND_SLEEP_INTERVAL)
    time.sleep(mame.MAME_NOT_FOUND_SLEEP_INTERVAL)
    continue
  
  # Close the save state file before MAME can write it
  inputFile.close()
  
  # Post the message to MAME to save a new state and briefly wait for write
  win32api.PostMessage(mameWindow, getSaveStateMsg, 0, 0)
  time.sleep(0.5)
  
  # Open the state file again and read it into jam objects
  inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')  # Open the file
  jReader = JamReader.JamReader(inputFile)
  jGame = jReader.readGameObject() 
  print jGame.description()

  # Wait for the game to be over before the next read
  timeToWaitForNextRead = jGame.timeLeftInFullGame()

  if jGame.isComplete() AND jGame != lastSavedGame:
    log.debug("Saving new game")
    saved = jServer.addGameToDatabase(jGame)
    if saved == True:
      lastSavedGame = jGame
      log.debug("Saved Jam Game")
    else:
      log.debug("Failed to save game: %s", jGame.description())
  else:
    sleepTime = mame.MAME_NOT_FOUND_SLEEP_INTERVAL if (timeToWaitForNextRead == 0) else timeToWaitForNextRead
    time.sleep(sleepTime)

# If we get down here, we somehow broke the infinite loop
log.warn("Script reached the end. Something probably went wrong")
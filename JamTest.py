#!/usr/bin/python
import argparse
import logging
import JamReader
import JamGame
import offsets
import os
import stat
import stateTracer.stateManager
import sys
import time
import utilities
import mame

# Globals
ARG_SOURCE_DEST = "source"

# Set up logging
log = logging.getLogger('JamTracker')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)

# Create parser to handle arguments passed into the script at run time
parser = argparse.ArgumentParser(description='Dump the game stats from a save state')
parser.add_argument('-i', "--source", dest=ARG_SOURCE_DEST, help="Source file/string (Or use piping/redirect)", default=None, required=False)
args = vars(parser.parse_args())

###############################
# Option: -s <file>
# Handle File Input / stdin
#
###############################
if args[ARG_SOURCE_DEST] is not None:
  inputFile = open(str(args[ARG_SOURCE_DEST]), 'rb')
  jReader = JamReader.JamReader(inputFile, logging.debug)
  jGame = jReader.readGameObject() 
  print jGame.description()
  log.debug("Finished Running")
  exit()
else:
  log.critical("No save file specified")
  exit()
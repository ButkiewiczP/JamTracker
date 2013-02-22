#!/usr/bin/python/

import datetime
import ImageGrab
import gameUtilities
import JamGame
import JamPlayer
import JamServer
import OCRTester
import os
import time

class Logger:
  def __init__(self, filename, debug_level):
    self.logFilename = filename
    self.logLevel = int(debug_level)
    self.log("== Starting Jam Log on " + datetime.datetime.now().strftime("%x") + " ==", 5)

  def log(self, message, level):
    if level >= self.logLevel:
      tMessage = '[' + datetime.datetime.now().strftime("%H:%M") + '] ' + message 
      with open(self.logFilename, 'a') as logFile:
        logFile.write(tMessage + '\r\n')
      logFile.close()

def main():

  ############# VARIABLES #################
  server = JamServer.JamServer()
  log = Logger("jam.log", 3)
  sleepTimeBetweenScreenGrabs = 2.5
  testImageDir = os.getcwd() + '\\testImages\\'
  tests = OCRTester.OCRTester(testImageDir)
  tests.bigTest()
  asdx = raw_input("press a key")
  exit()
  #########################################
  
  while gameUtilities.gameIsStillRunning():
    gameScreenGrab = "" # ImageGrab.grab()
    saved = False
  
    if gameUtilities.gameScreenIsStatsScreen(gameScreenGrab):
      log.log("Found Stat Screen. Beginning to parse stats", 3)
      newGame = JamGame.JamGame(gameScreenGrab)  # Creates new game object. game object parses S.S.
      
      log.log("Adding game to database", 4)
      saved = server.addGameToDatabase(newGame)
    
      if saved == True:
        log.log("Game stats saved successfully", 3)
      else:
        log.log("Error saving stats", 5)
    else: #Else, not on the stats page
      time.sleep(sleepTimeBetweenScreenGrabs)
  
    break # temporary 'don't-get-stuck-in-an-infinite-loop' fix  
  #End While-Loop
  
  log.log("Jam exited. Closing process", 2)  
  
    
if __name__ == "__main__":
    main()
